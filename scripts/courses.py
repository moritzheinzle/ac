#!/usr/bin/env python3
import os
import re
import subprocess
from pathlib import Path
from config import ROOT, CURRENT_COURSE_SYMLINK, CURRENT_COURSE_WATCH_FILE, BASE_DIR

def parse_simple_yaml(path: Path) -> dict:
    data = {}
    if not path.is_file():
        return data
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if ":" in line:
                    k, v = line.split(":", 1)
                    k = k.strip()
                    v = v.strip().strip("'\"")
                    data[k] = v
    except Exception:
        pass
    return data

class Course:
    def __init__(self, path: Path):
        self.path = path.resolve()
        self.name = self.path.name
        self.info = self._read_info()
        self._lectures = None

    def _read_info(self) -> dict:
        for fname in ["info.yaml", "info.yml"]:
            info_file = self.path / fname
            if info_file.is_file():
                info = parse_simple_yaml(info_file)
                if info:
                    info.setdefault("title", self.name.upper())
                    info.setdefault("short", self.name.upper())
                    return info
        return {"title": self.name.upper(), "short": self.name.upper()}

    @property
    def title(self) -> str:
        return self.info.get("title", self.name)

    @property
    def short(self) -> str:
        return self.info.get("short", self.name.upper())

    @property
    def main_file(self) -> Path:
        return self.path / "main.typ"

    @property
    def lectures(self):
        from lectures import Lectures
        if self._lectures is None:
            self._lectures = Lectures(self)
        return self._lectures

    def __eq__(self, other):
        if not isinstance(other, Course):
            return False
        return self.path == other.path

    def __str__(self):
        return f"{self.short: <5} │ {self.title}"

class Courses(list):
    def __init__(self):
        super().__init__(self.read_courses())

    def read_courses(self):
        courses = []
        seen = set()

        # 1. Primary configured root
        if ROOT.is_dir():
            for p in ROOT.iterdir():
                if p.is_dir() and not p.name.startswith(".") and p.name not in ["lessons", "figures", "scripts"]:
                    res = p.resolve()
                    if res not in seen:
                        seen.add(res)
                        courses.append(Course(res))

        # 2. Extensible search across other branches (e.g. bulme/year-5, tug/...)
        for base in [BASE_DIR / "bulme", BASE_DIR / "tug"]:
            if base.is_dir():
                for p in base.rglob("*"):
                    if p.is_dir() and not p.name.startswith(".") and p.name not in ["lessons", "figures", "scripts"]:
                        if (p / "info.yaml").exists() or (p / "info.yml").exists() or (p / "main.typ").exists():
                            res = p.resolve()
                            if res not in seen and res != BASE_DIR and res != ROOT:
                                seen.add(res)
                                courses.append(Course(res))

        return sorted(courses, key=lambda c: c.short)

    @property
    def current(self) -> Course:
        if CURRENT_COURSE_SYMLINK.is_symlink() or CURRENT_COURSE_SYMLINK.exists():
            resolved = CURRENT_COURSE_SYMLINK.resolve()
            for c in self:
                if c.path == resolved:
                    return c
            # If path resolved to a directory not in current list
            if resolved.is_dir():
                return Course(resolved)
        if len(self) > 0:
            return self[0]
        return None

    @current.setter
    def current(self, course: Course):
        if CURRENT_COURSE_SYMLINK.is_symlink() or CURRENT_COURSE_SYMLINK.exists():
            CURRENT_COURSE_SYMLINK.unlink()
        
        CURRENT_COURSE_SYMLINK.symlink_to(course.path)
        
        try:
            CURRENT_COURSE_WATCH_FILE.write_text(f"{course.short}\n")
        except Exception:
            pass

        try:
            subprocess.run([
                "notify-send",
                "-a", "Typst Castel",
                "-i", "accessories-text-editor",
                "Aktives Fach gewechselt",
                f"{course.short} — {course.title}"
            ], check=False)
        except Exception:
            pass
