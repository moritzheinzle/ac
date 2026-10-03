#!/usr/bin/env python3
import os
import re
import sys
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

AC_DIR = Path("/home/mo/ac")
CURRENT_COURSE_LINK = AC_DIR / "current-course"
INKSCAPE_TEMPLATE = Path.home() / ".config" / "inkscape" / "templates" / "default.svg"

FALLBACK_SVG = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" width="160mm" height="100mm" viewBox="0 0 160 100" version="1.1">
  <defs>
    <style type="text/css">
      text { font-family: "Libertinus Serif", "Linux Libertine", serif; font-size: 11pt; }
    </style>
  </defs>
  <g id="layer1" />
</svg>
"""

def slugify(text: str) -> str:
    replacements = {
        "ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss",
        "Ä": "ae", "Ö": "oe", "Ü": "ue",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[-\s]+", "-", text)
    return text if text else "figure"

def find_figures_dir(hint_path: Path = None) -> Path:
    candidates = []
    if hint_path:
        hp = hint_path.resolve()
        candidates.extend([hp / "figures", hp.parent / "figures", hp])

    cwd = Path.cwd().resolve()
    candidates.extend([cwd / "figures", cwd.parent / "figures"])

    if CURRENT_COURSE_LINK.exists():
        candidates.append(CURRENT_COURSE_LINK.resolve() / "figures")

    for c in candidates:
        if c.is_dir() and c.name == "figures":
            return c

    if CURRENT_COURSE_LINK.exists():
        target = CURRENT_COURSE_LINK.resolve() / "figures"
    else:
        target = cwd / "figures"
    target.mkdir(parents=True, exist_ok=True)
    return target

def rofi_input(prompt: str) -> str:
    args = ["rofi", "-dmenu", "-p", prompt, "-lines", "0"]
    proc = subprocess.run(args, input="", text=True, capture_output=True)
    if proc.returncode == 0 and proc.stdout.strip():
        return proc.stdout.strip()
    return ""

def rofi_select(prompt: str, options: list) -> int:
    if not options:
        return -1
    args = ["rofi", "-dmenu", "-i", "-p", prompt, "-format", "i", "-lines", str(min(12, len(options)))]
    proc = subprocess.run(args, input="\n".join(options), text=True, capture_output=True)
    if proc.returncode == 0 and proc.stdout.strip():
        try:
            return int(proc.stdout.strip())
        except ValueError:
            return -1
    return -1

def notify(summary: str, body: str = ""):
    if shutil.which("notify-send"):
        subprocess.run(["notify-send", "-a", "Typst Inkscape", summary, body], check=False)

def copy_to_clipboard(text: str):
    if shutil.which("wl-copy"):
        subprocess.run(["wl-copy"], input=text, text=True, check=False)

def auto_fit_canvas(svg_path: Path):
    try:
        subprocess.run(
            ["inkscape", "--batch-process", f"--actions=select-all:all;page-fit-to-selection;export-filename:{svg_path};export-do", str(svg_path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False
        )
    except Exception:
        pass

def create_figure(title: str = None, hint_dir: Path = None, wait: bool = False):
    if not title:
        title = rofi_input("Figur-Titel:")
        if not title:
            return None

    slug = slugify(title)
    figures_dir = find_figures_dir(hint_dir)
    figures_dir.mkdir(parents=True, exist_ok=True)

    target_file = figures_dir / f"{slug}.svg"
    counter = 1
    while target_file.exists():
        target_file = figures_dir / f"{slug}_{counter}.svg"
        counter += 1

    if INKSCAPE_TEMPLATE.exists():
        shutil.copyfile(INKSCAPE_TEMPLATE, target_file)
    else:
        target_file.write_text(FALLBACK_SVG, encoding="utf-8")

    initial_mtime = target_file.stat().st_mtime
    initial_size = target_file.stat().st_size

    if wait:
        subprocess.run(["inkscape", str(target_file)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if not target_file.exists():
            sys.exit(1)

        curr_mtime = target_file.stat().st_mtime
        curr_size = target_file.stat().st_size
        is_modified = curr_mtime > initial_mtime or curr_size != initial_size

        if is_modified:
            auto_fit_canvas(target_file)

            rel_img_path = f"../figures/{target_file.name}"
            typst_code = f"""#figure(
  image("{rel_img_path}", width: 80%),
  caption: [{title}],
) <fig:{slug}>"""

            copy_to_clipboard(typst_code)
            print(typst_code)
            notify("Figur gespeichert & eingefügt", f"{title}\nTypst-Markup im Clipboard kopiert!")
            return target_file
        else:
            try:
                target_file.unlink()
            except Exception:
                pass
            sys.exit(1)
    else:
        subprocess.Popen(["inkscape", str(target_file)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        rel_img_path = f"../figures/{target_file.name}"
        typst_code = f"""#figure(
  image("{rel_img_path}", width: 80%),
  caption: [{title}],
) <fig:{slug}>"""
        copy_to_clipboard(typst_code)
        print(typst_code)
        notify("Figur erstellt & in Inkscape geöffnet", f"{title}\nTypst-Markup im Clipboard kopiert!")
        return target_file

def edit_figure(hint_dir: Path = None):
    figures_dir = find_figures_dir(hint_dir)
    if not figures_dir.exists():
        notify("Kein Figuren-Ordner", f"{figures_dir} existiert nicht.")
        return

    svg_files = sorted(figures_dir.glob("*.svg"), key=lambda f: f.stat().st_mtime, reverse=True)
    if not svg_files:
        choice = rofi_select("Keine Figuren vorhanden", ["Neue Figur erstellen"])
        if choice == 0:
            create_figure(hint_dir=hint_dir, wait=True)
        return

    options = []
    for f in svg_files:
        mtime = datetime.fromtimestamp(f.stat().st_mtime).strftime("%d.%m.%Y %H:%M")
        name = f.stem.replace("-", " ").title()
        options.append(f"{name: <30} ⟨{f.name} │ {mtime}⟩")

    idx = rofi_select("Figur bearbeiten", options)
    if idx >= 0 and idx < len(svg_files):
        target = svg_files[idx]
        subprocess.run(["inkscape", str(target)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        auto_fit_canvas(target)
        notify("Figur aktualisiert", f"{target.name} angepasst.")

def open_figures_folder(hint_dir: Path = None):
    figures_dir = find_figures_dir(hint_dir)
    opener = "nautilus" if shutil.which("nautilus") else "xdg-open"
    subprocess.Popen([opener, str(figures_dir)])

def interactive_menu():
    actions = [
        ("Neue Figur erstellen", "create"),
        ("Figur bearbeiten...", "edit"),
        ("Figuren-Ordner öffnen", "folder"),
    ]
    options = [a[0] for a in actions]
    idx = rofi_select("Typst Figuren (Inkscape)", options)
    if idx == 0:
        create_figure(wait=True)
    elif idx == 1:
        edit_figure()
    elif idx == 2:
        open_figures_folder()

def main():
    args = sys.argv[1:]
    if not args:
        interactive_menu()
        return

    wait = False
    if "-w" in args:
        wait = True
        args.remove("-w")
    if "--wait" in args:
        wait = True
        args.remove("--wait")

    if not args:
        interactive_menu()
        return

    cmd = args[0].lower()
    if cmd in ["-h", "--help", "help"]:
        print("Usage: inkscape-figures [create [--wait] <title> | edit | folder | menu]")
        print("  create [--wait] <title>  Create a new figure and open Inkscape (wait blocks until exit)")
        print("  edit                     Select and edit an existing figure via Rofi")
        print("  folder                   Open figures folder")
        print("  menu                     Open interactive Rofi menu")
        return

    if cmd in ["create", "new", "-c"]:
        title = " ".join(args[1:]) if len(args) > 1 else None
        create_figure(title=title, wait=wait)
    elif cmd in ["edit", "open", "-e"]:
        edit_figure()
    elif cmd in ["folder", "dir"]:
        open_figures_folder()
    elif cmd in ["menu", "-m"]:
        interactive_menu()
    else:
        create_figure(title=" ".join(args), wait=wait)

if __name__ == "__main__":
    main()
