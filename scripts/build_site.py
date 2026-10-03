#!/usr/bin/env python3
"""
Simple and minimal PDF Notes builder.
Compiles main.typ master files to PDF and generates a clean, simple course overview site.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


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
                    data[k.strip()] = v.strip().strip("'\"")
    except Exception:
        pass
    return data


def format_file_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


class CourseScanner:
    def __init__(self, root_dir: Path):
        self.root = root_dir.resolve()

    def get_category_info(self, course_path: Path, info: dict = None):
        if info and "category" in info:
            cat_title = info["category"]
            cat_id = info.get("category_id", re.sub(r'[^a-zA-Z0-9]+', '-', cat_title.lower()).strip('-'))
            cat_weight = int(info.get("category_weight", 50))
            return cat_id, cat_title, cat_weight

        rel_parts = course_path.relative_to(self.root).parts
        if not rel_parts:
            return "other", "Other Courses", 99

        top = rel_parts[0]
        if top == "bulme":
            if len(rel_parts) >= 2:
                sub = rel_parts[1]
                year_match = re.search(r'(\d+)', sub)
                year_num = year_match.group(1) if year_match else sub
                return f"bulme-{sub}", f"BULME (Year {year_num})", 10 + int(year_num if year_num.isdigit() else 0)
            return "bulme", "BULME", 10

        elif top == "tug":
            if len(rel_parts) == 2:
                return "tug", "TU Graz", 30
            elif len(rel_parts) >= 3:
                sub = rel_parts[1]
                sem_match = re.search(r'(?:sem(?:ester)?|jahr|year)[-_]?(\d+)', sub, re.IGNORECASE)
                if sem_match:
                    sem_num = int(sem_match.group(1))
                    return f"tug-sem-{sem_num}", f"TU Graz (Semester {sem_num})", 30 + sem_num
                clean_sub = sub.replace("-", " ").replace("_", " ").title()
                return f"tug-{sub}", f"TU Graz ({clean_sub})", 30
            return "tug", "TU Graz", 30

        return "other", "Other Courses", 99

    def find_courses(self):
        courses = []
        seen = set()

        for base_name in ["bulme", "tug"]:
            base_dir = self.root / base_name
            if not base_dir.is_dir():
                continue
            for p in base_dir.rglob("*"):
                if p.is_dir() and not p.name.startswith(".") and p.name not in ["lessons", "figures", "scripts"]:
                    if (p / "info.yaml").exists() or (p / "info.yml").exists() or (p / "main.typ").exists():
                        res = p.resolve()
                        if res not in seen:
                            seen.add(res)
                            info = {}
                            for fname in ["info.yaml", "info.yml"]:
                                if (res / fname).exists():
                                    info = parse_simple_yaml(res / fname)
                                    break

                            cat_id, cat_title, cat_weight = self.get_category_info(res, info)
                            short = info.get("short", res.name.upper())
                            title = info.get("title", res.name.upper())

                            courses.append({
                                "path": res,
                                "name": res.name,
                                "short": short,
                                "title": title,
                                "category_id": cat_id,
                                "category_title": cat_title,
                                "category_weight": cat_weight,
                            })

        return sorted(courses, key=lambda c: (c["category_weight"], c["short"]))


def compile_typst(src: Path, out: Path, root: Path) -> bool:
    out.parent.mkdir(parents=True, exist_ok=True)
    res = subprocess.run([
        "typst", "compile",
        "--root", str(root),
        str(src),
        str(out)
    ], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[WARN] Typst compilation failed for {src.name}:")
        print(res.stderr.strip()[:300])
        return False
    return True


def build_all(root_dir: Path, site_dir: Path, base_url: str = None, run_hugo: bool = False):
    print(f"[INFO] Building PDF notes overview")
    print(f"       Root: {root_dir}")
    print(f"       Site: {site_dir}")

    static_pdfs_dir = site_dir / "static" / "pdfs"
    content_docs_dir = site_dir / "content" / "docs"

    scanner = CourseScanner(root_dir)
    courses = scanner.find_courses()
    print(f"[INFO] Found {len(courses)} courses")

    categories = {}
    for c in courses:
        cat_id = c["category_id"]
        if cat_id not in categories:
            categories[cat_id] = {
                "title": c["category_title"],
                "weight": c["category_weight"],
                "courses": []
            }
        categories[cat_id]["courses"].append(c)

    # 1. Compile or copy main.pdf for each course
    for c in courses:
        c_path = c["path"]
        target_pdf_dir = static_pdfs_dir / c["category_id"] / c["name"]
        target_pdf_dir.mkdir(parents=True, exist_ok=True)

        main_typ = c_path / "main.typ"
        out_main_pdf = target_pdf_dir / "main.pdf"
        main_compiled = False

        if main_typ.exists():
            print(f"[BUILD] {c['short']}: compiling main.typ -> main.pdf")
            main_compiled = compile_typst(main_typ, out_main_pdf, root_dir)

        if not main_compiled and (c_path / "main.pdf").exists():
            src_pdf = c_path / "main.pdf"
            shutil.copy2(src_pdf, out_main_pdf)
            main_compiled = True
            print(f"[COPY]  {c['short']}: using existing main.pdf")

        if main_compiled and out_main_pdf.exists():
            st = out_main_pdf.stat()
            c["has_pdf"] = True
            c["pdf_url"] = f"pdfs/{c['category_id']}/{c['name']}/main.pdf"
            c["pdf_size"] = format_file_size(st.st_size)
            c["pdf_mtime"] = datetime.fromtimestamp(st.st_mtime).strftime("%d.%m.%Y")
        else:
            c["has_pdf"] = False
            c["pdf_url"] = None
            c["pdf_size"] = "-"
            c["pdf_mtime"] = "-"

        c["course_url"] = f"docs/{c['category_id']}/{c['name']}/"

    # 2. Generate Hugo Content
    content_docs_dir.mkdir(parents=True, exist_ok=True)

    # A. Landing page (site/content/_index.md)
    landing_page = site_dir / "content" / "_index.md"
    generate_landing_page(landing_page, courses)

    # B. Category and Course pages
    cat_weight = 10
    for cat_id, cat_info in categories.items():
        cat_dir = content_docs_dir / cat_id
        cat_dir.mkdir(parents=True, exist_ok=True)

        generate_category_index(cat_dir, cat_id, cat_info, cat_weight)
        cat_weight += 10

        course_weight = 10
        for c in cat_info["courses"]:
            generate_course_page(cat_dir, c, course_weight)
            course_weight += 10

    # C. Docs root (_index.md)
    generate_docs_index(content_docs_dir)

    print(f"[OK] Generated pages for {len(courses)} courses")

    # 3. Build Hugo if requested
    if run_hugo:
        hugo_bin = shutil.which("hugo") or str(Path.home() / ".local" / "bin" / "hugo")
        if not Path(hugo_bin).is_file() and not shutil.which(hugo_bin):
            print("[WARN] Hugo binary not found. Skipping hugo build.")
            return

        print("[BUILD] Compiling static site with Hugo...")
        cmd = [str(hugo_bin), "--source", str(site_dir), "--destination", "public", "--minify"]
        if base_url:
            cmd.extend(["--baseURL", base_url])
        subprocess.run(cmd, check=True)
        print("[OK] Hugo build finished: site/public/")


def generate_landing_page(path: Path, courses: list):
    clean_courses = []
    for c in courses:
        clean_courses.append({
            "name": c["name"],
            "short": c["short"],
            "title": c["title"],
            "category_id": c["category_id"],
            "category_title": c["category_title"],
            "course_url": c["course_url"],
            "has_pdf": c["has_pdf"],
            "pdf_url": c["pdf_url"],
            "pdf_size": c["pdf_size"],
            "pdf_mtime": c["pdf_mtime"],
        })

    frontmatter = {
        "title": "Course Notes",
        "courses": clean_courses,
        "last_updated": datetime.now().strftime("%d.%m.%Y"),
    }
    content = json.dumps(frontmatter, indent=2) + "\n\n"
    path.write_text(content, encoding="utf-8")


def generate_course_page(cat_dir: Path, c: dict, weight: int):
    page_path = cat_dir / f"{c['name']}.md"
    frontmatter = {
        "title": f"{c['short']} — {c['title']}",
        "course_title": c["title"],
        "short": c["short"],
        "category_id": c["category_id"],
        "category_title": c["category_title"],
        "has_pdf": c["has_pdf"],
        "pdf_url": c["pdf_url"],
        "pdf_size": c["pdf_size"],
        "pdf_mtime": c["pdf_mtime"],
        "weight": weight,
    }
    content = json.dumps(frontmatter, indent=2) + "\n\n"
    page_path.write_text(content, encoding="utf-8")


def generate_category_index(cat_dir: Path, cat_id: str, cat_info: dict, weight: int):
    idx_path = cat_dir / "_index.md"
    frontmatter = {
        "title": cat_info["title"],
        "weight": weight,
        "category_id": cat_id,
    }
    content = json.dumps(frontmatter, indent=2) + "\n\n"
    idx_path.write_text(content, encoding="utf-8")


def generate_docs_index(content_docs_dir: Path):
    idx_path = content_docs_dir / "_index.md"
    frontmatter = {
        "title": "Course Directory",
        "weight": 1,
    }
    content = json.dumps(frontmatter, indent=2) + "\n\n"
    idx_path.write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Build Typst PDFs and simple site")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help="Repository root")
    parser.add_argument("--site-dir", type=Path, default=None, help="Hugo site directory")
    parser.add_argument("--baseURL", type=str, default=None, help="Hugo baseURL override")
    parser.add_argument("--build-hugo", action="store_true", help="Run hugo compiler after PDF generation")
    args = parser.parse_args()

    root_dir = args.root.resolve()
    site_dir = (args.site_dir or (root_dir / "site")).resolve()

    build_all(root_dir, site_dir, base_url=args.baseURL, run_hugo=args.build_hugo)


if __name__ == "__main__":
    main()
