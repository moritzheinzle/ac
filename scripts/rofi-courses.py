#!/usr/bin/env python3
import sys
import subprocess
from courses import Courses
from rofi import rofi

def main():
    courses = Courses()
    if not courses:
        print("Keine Kurse gefunden.")
        return

    current = courses.current

    options = []
    current_index = 0
    for i, c in enumerate(courses):
        marker = "● " if (current and c.path == current.path) else "  "
        options.append(f"{marker}{c.short: <5} │ {c.title}")
        if current and c.path == current.path:
            current_index = i

    rofi_args = [
        "-lines", str(min(12, len(courses))),
        "-a", str(current_index),
    ]

    key, index, selected = rofi("Fach wählen", options, rofi_args)

    if key == 0 and index >= 0:
        chosen = courses[index]
        courses.current = chosen

        if "-c" in sys.argv or "--chain" in sys.argv:
            from lectures import Lectures
            subprocess.Popen([sys.executable, str(sys.path[0] + "/rofi-lectures.py")])

if __name__ == "__main__":
    main()
