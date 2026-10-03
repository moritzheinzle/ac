#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

# Paths
BASE_DIR = Path("/home/mo/ac")
ROOT = Path(os.environ.get("TYPST_COURSES_ROOT", str(BASE_DIR / "bulme" / "year-4")))
CURRENT_COURSE_SYMLINK = Path(os.environ.get("TYPST_CURRENT_COURSE", str(BASE_DIR / "current-course")))
CURRENT_COURSE_WATCH_FILE = Path("/tmp/current_course")
TEMPLATE_PATH = BASE_DIR / "template.typ"

# Editor and terminal detection
TERMINAL = os.environ.get("TERMINAL")
if not TERMINAL:
    for term in ["alacritty", "foot", "kitty", "xterm"]:
        if shutil.which(term):
            TERMINAL = term
            break
if not TERMINAL:
    TERMINAL = "alacritty"

EDITOR = os.environ.get("EDITOR", "nvim")
PDF_VIEWER = os.environ.get("PDF_VIEWER", "zathura")

DATE_FORMAT = "%d.%m.%Y"
AUTHOR = "Moritz"
SCHOOL = "BULME"
CLASS = "4AHET"
