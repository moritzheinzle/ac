#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path
from courses import Courses, Course
from config import ROOT, CURRENT_COURSE_SYMLINK

def get_target_course():
    cwd = Path.cwd().resolve()
    # Check if cwd is inside a course directory
    for parent in [cwd] + list(cwd.parents):
        if (parent / "info.yaml").exists() or (parent / "info.yml").exists() or (parent / "main.typ").exists():
            if parent != ROOT and parent != ROOT.parent:
                return Course(parent)

    # Fallback to current course
    courses = Courses()
    return courses.current

def main():
    parser = argparse.ArgumentParser(description="Create a new Typst lecture note")
    parser.add_argument("title", nargs="?", default=None, help="Title of the lecture")
    parser.add_argument("-n", "--no-open", action="store_true", help="Do not open editor after creation")
    args = parser.parse_args()

    course = get_target_course()
    if not course:
        print("Fehler: Kein aktives Fach gefunden.")
        sys.exit(1)

    title = args.title
    if not title:
        try:
            title = input(f"Titel der Lektion für [{course.short}]: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAbgebrochen.")
            sys.exit(0)

    lec = course.lectures.new_lecture(title=title if title else None)
    print(f"✓ Lektion erstellt: {lec.file_path}")
    print(f"✓ Zu {course.main_file.name} hinzugefügt.")

    if not args.no_open:
        lec.edit()

if __name__ == "__main__":
    main()
