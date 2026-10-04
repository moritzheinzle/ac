#!/usr/bin/env python3
import os
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from config import TERMINAL, EDITOR, PDF_VIEWER, TEMPLATE_PATH, DATE_FORMAT, AUTHOR, BASE_DIR

def filename_to_number(name: str) -> int:
    match = re.search(r'(\d+)', name)
    if match:
        return int(match.group(1))
    return 0

class Lecture:
    def __init__(self, file_path: Path, course):
        self.file_path = file_path.resolve()
        self.course = course
        self.number = filename_to_number(self.file_path.stem)
        self.title, self.date = self._parse_metadata()

    def _parse_metadata(self):
        title = ""
        date_str = ""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                content = f.read()

            lesson_match = re.search(r'#lesson\(\s*["\']([^"\']+)["\'](?:\s*,\s*date:\s*["\']([^"\']+)["\'])?', content)
            if lesson_match:
                title = lesson_match.group(1)
                if lesson_match.group(2):
                    date_str = lesson_match.group(2)

            if not title:
                heading_match = re.search(r'^\s*=\s+([^\n]+)', content, re.MULTILINE)
                if heading_match:
                    title = heading_match.group(1).strip()

            if not date_str:
                date_match = re.search(r'(\d{2}\.\d{2}\.\d{4})', content)
                if date_match:
                    date_str = date_match.group(1)

        except Exception:
            pass

        if not title:
            title = self.file_path.stem.replace("_", " ").title()
        if not date_str:
            mtime = os.path.getmtime(self.file_path)
            date_str = datetime.fromtimestamp(mtime).strftime(DATE_FORMAT)

        return title, date_str

    def edit(self):
        cmd = []
        is_gui_editor = any(g in EDITOR for g in ["code", "zed", "subl", "gedit", "kate"])
        
        if is_gui_editor or not TERMINAL:
            cmd = [EDITOR, str(self.file_path)]
        else:
            if "alacritty" in TERMINAL:
                cmd = [TERMINAL, "-e", EDITOR, str(self.file_path)]
            elif "foot" in TERMINAL:
                cmd = [TERMINAL, EDITOR, str(self.file_path)]
            else:
                cmd = [TERMINAL, "-e", f"{EDITOR} '{self.file_path}'"]

        subprocess.Popen(cmd, cwd=str(self.course.path))

    def __str__(self):
        return f"{self.number:02d}. {self.title} ({self.date})"

class Lectures(list):
    def __init__(self, course):
        self.course = course
        self.root = course.path
        self.lessons_dir = self.root / "lessons"
        self.master_file = self.root / "main.typ"
        super().__init__(self.read_files())

    def read_files(self):
        if not self.lessons_dir.is_dir():
            return []
        files = list(self.lessons_dir.glob("lesson_*.typ")) + list(self.lessons_dir.glob("lec_*.typ"))
        lectures = [Lecture(f, self.course) for f in files]
        return sorted(lectures, key=lambda l: l.number)

    def ensure_course_setup(self):
        self.lessons_dir.mkdir(parents=True, exist_ok=True)
        (self.root / "figures").mkdir(parents=True, exist_ok=True)

        template_symlink = self.root / "template.typ"
        if not template_symlink.exists() and TEMPLATE_PATH.exists():
            try:
                rel_target = os.path.relpath(TEMPLATE_PATH, self.root)
                template_symlink.symlink_to(rel_target)
            except Exception:
                pass

        if not self.master_file.exists():
            course_title = self.course.title
            course_short = self.course.short
            content = f"""#import "template.typ": *

#show: project.with(
  title: "{course_title}",
  course: "{course_short}",
  author: "{AUTHOR}",
)

"""
            self.master_file.write_text(content, encoding="utf-8")

    def new_lecture(self, title: str = None, date_str: str = None) -> Lecture:
        self.ensure_course_setup()

        existing_numbers = [l.number for l in self]
        next_num = max(existing_numbers, default=0) + 1

        if not title:
            title = f"Lecture {next_num}"
        if not date_str:
            date_str = datetime.today().strftime(DATE_FORMAT)

        filename = f"lesson_{next_num:02d}.typ"
        file_path = self.lessons_dir / filename

        lesson_content = f"""#import "../template.typ": *

#lesson("{title}", date: "{date_str}")

== Introduction

"""
        file_path.write_text(lesson_content, encoding="utf-8")

        include_stmt = f'#include "lessons/{filename}"'
        master_content = self.master_file.read_text(encoding="utf-8")
        if include_stmt not in master_content:
            with open(self.master_file, "a", encoding="utf-8") as f:
                if not master_content.endswith("\n"):
                    f.write("\n")
                f.write(f"{include_stmt}\n")

        self.clear()
        self.extend(self.read_files())

        created = next((l for l in self if l.file_path == file_path), Lecture(file_path, self.course))
        return created

    def compile_master(self):
        self.ensure_course_setup()
        pdf_path = self.master_file.with_suffix(".pdf")
        res = subprocess.run(
            ["typst", "compile", "--root", str(BASE_DIR), str(self.master_file), str(pdf_path)],
            cwd=str(self.root),
            capture_output=True,
            text=True
        )
        return res.returncode, pdf_path, res.stderr

    def open_viewer(self):
        self.ensure_course_setup()
        pdf_path = self.master_file.with_suffix(".pdf")
        subprocess.run(["typst", "compile", "--root", str(BASE_DIR), str(self.master_file), str(pdf_path)], cwd=str(self.root))
        subprocess.Popen(["typst", "watch", "--root", str(BASE_DIR), str(self.master_file), str(pdf_path)], cwd=str(self.root))
        subprocess.Popen([PDF_VIEWER, str(pdf_path)], cwd=str(self.root))
