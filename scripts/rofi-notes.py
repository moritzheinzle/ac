#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path
from courses import Courses
from rofi import rofi, rofi_input

def main():
    courses = Courses()
    current = courses.current

    curr_tag = f"[{current.short}]" if current else "[Kein Fach]"

    menu_items = [
        ("Neue Lektion beginnen", "new"),
        (f"Lektion öffnen {curr_tag}", "lectures"),
        (f"Fach wechseln (aktuell: {current.short if current else 'keins'})", "courses"),
        (f"Figuren verwalten / Neu {curr_tag} (Inkscape)", "figures"),
        (f"Live-Vorschau {curr_tag} (Typst + Zathura)", "preview"),
        (f"Master kompilieren {curr_tag}", "compile"),
    ]

    labels = [item[0] for item in menu_items]
    key, idx, selected = rofi(f"Typst Notizen {curr_tag}", labels, ["-lines", str(len(labels))])

    if key != 0 or idx < 0:
        return

    action = menu_items[idx][1]
    scripts_dir = Path(__file__).parent

    if action == "new":
        title = rofi_input("Titel der neuen Lektion:")
        if title is not None:
            new_lec = current.lectures.new_lecture(title=title.strip() if title.strip() else None)
            new_lec.edit()
    elif action == "lectures":
        subprocess.run([sys.executable, str(scripts_dir / "rofi-lectures.py")])
    elif action == "courses":
        subprocess.run([sys.executable, str(scripts_dir / "rofi-courses.py")])
    elif action == "figures":
        subprocess.run([sys.executable, str(scripts_dir / "inkscape-figures.py")])
    elif action == "preview":
        if current:
            current.lectures.open_viewer()
    elif action == "compile":
        if current:
            code, pdf, err = current.lectures.compile_master()
            if code == 0:
                subprocess.run([
                    "notify-send", "-a", "Typst Castel",
                    "Kompilierung erfolgreich",
                    f"{pdf.name} erstellt."
                ], check=False)
            else:
                subprocess.run([
                    "notify-send", "-a", "Typst Castel",
                    "-u", "critical",
                    "Kompilierungsfehler",
                    err[:200] if err else "Unbekannter Fehler"
                ], check=False)

if __name__ == "__main__":
    main()
