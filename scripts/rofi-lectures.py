#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path
from courses import Courses
from rofi import rofi, rofi_input

def main():
    courses = Courses()
    current = courses.current
    if not current:
        # Prompt to select course first
        scripts_dir = Path(__file__).parent
        subprocess.run([sys.executable, str(scripts_dir / "rofi-courses.py")])
        courses = Courses()
        current = courses.current
        if not current:
            return

    lectures = current.lectures
    sorted_lectures = sorted(lectures, key=lambda l: -l.number)

    # Top option for creating new lecture
    new_opt = "➕ Neue Lektion erstellen  (Strg+N)"
    options = [new_opt]

    for l in sorted_lectures:
        options.append(f"{l.number:02d}. {l.title: <35} ⟨{l.date}⟩")

    prompt = f"Lektionen [{current.short}]"
    rofi_args = [
        "-lines", str(min(12, len(options))),
        "-kb-custom-1", "Control+z"
    ]

    key, index, selected = rofi(prompt, options, rofi_args)

    # User pressed Ctrl+N or selected the new option
    if key == 1 or (key == 0 and index == 0):
        title = rofi_input("Titel der Lektion (Enter für Standard):")
        if title is None:
            return  # Escaped
        title = title.strip()
        new_lec = lectures.new_lecture(title=title if title else None)
        new_lec.edit()
    elif key == 0 and index > 0:
        target_lec = sorted_lectures[index - 1]
        target_lec.edit()

if __name__ == "__main__":
    main()
