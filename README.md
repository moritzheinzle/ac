# Academic Notes & Course Management

A lightweight academic note-taking and static site generation workflow built for Typst, Neovim, Rofi (Wayland), and Hugo.

---

## Overview

This repository provides an integrated environment for drafting, structuring, and publishing academic lecture notes:

- **Typst Documents**: Fast typesetting with native A4 layout, headers, definitions, and theorems.
- **Master Script Architecture**: Each subject maintains a central `main.typ` that compiles into a complete `main.pdf`.
- **Desktop Workflow**: Wayland-native Rofi menus and Neovim keybindings for course switching, lesson creation, and Inkscape vector sketches.
- **Academic Web Portal**: A clean static web index in classic academic directory style (Times New Roman / Georgia serif) with PDF preview, table/grid views, search, and school/semester tag filters.

---

## Directory Structure

```text
ac/
├── template.typ                  # Central Typst template and macros
├── current-course -> ...         # Symlink pointing to the currently active course
├── scripts/                      # Management scripts and build pipeline
│   ├── build_site.py             # Compiles Typst PDFs and generates the Hugo portal
│   ├── config.py                 # Paths, editor, and terminal configuration
│   ├── courses.py                # Course scanning and metadata parsing
│   ├── lectures.py               # Lesson management and Typst includes
│   ├── rofi.py                   # Rofi Wayland interface wrapper
│   ├── rofi-courses.py           # Course selection menu
│   ├── rofi-lectures.py          # Lesson selector and creator
│   ├── rofi-notes.py             # Central quick-access dashboard
│   ├── rofi-figures.py           # Inkscape figure manager
│   └── new-lesson.py             # CLI lesson generator
├── bulme/year-4/                 # BULME Graz courses (Semester 8)
│   ├── am/                       # Applied Mathematics
│   │   ├── info.yaml             # Course metadata (title, short code)
│   │   ├── template.typ -> ...   # Symlink to global template
│   │   ├── main.typ              # Master document
│   │   └── lessons/              # Individual lecture source files
│   ├── auro/                     # Automation and Robotics
│   ├── dic/                      # Digital Technology
│   ├── fsst/                     # Software Systems
│   ├── gp/                       # Project Management
│   ├── hwe/                      # Hardware Engineering
│   ├── pbe3/                     # Microcontrollers / Embedded Systems
│   └── wir3/                     # Economics and Law
├── tug/                          # Graz University of Technology courses (future-proofed)
└── site/                         # Hugo portal directory
    ├── config.toml / hugo.toml   # Hugo configuration
    ├── content/                  # Generated pages, landing page, Impressum
    ├── layouts/                  # Academic index layouts and templates
    └── static/                   # Compiled PDFs, CSS, and JS controllers
```

---

## Desktop Workflow & Keybindings

### Window Manager (Niri / Wayland)

The following hotkeys are defined in `~/.config/niri/config.kdl`:

| Keybinding | Action | Description |
|---|---|---|
| `Mod+N` | `rofi-lectures` | Open lesson picker or create a new lesson |
| `Mod+Shift+N` | `rofi-courses` | Switch active course |
| `Mod+Alt+N` | `rofi-notes` | Open central notes dashboard |
| `Mod+Alt+F` | `rofi-figures` | Open Inkscape figure manager |
| `Mod+Shift+Return` | `ac-term` | Launch terminal in active course directory |
| `Mod+E` | `ac-nvim` | Open Neovim in active course directory |

### Neovim Shortcuts

| Keybinding | Action |
|---|---|
| `<Leader>tp` | Toggle PDF preview with Zathura |
| `<Leader>tm` | Pin master document (`main.typ`) in Tinymist LSP |
| `<Leader>if` | Create a new Inkscape vector figure and insert reference |
| `<Leader>ie` | Select and edit existing Inkscape figure |

### Inkscape Vector Drawing

Vector figures are stored as `.svg` in each course's `figures/` folder and included directly in Typst without intermediate compilation:

- `s`: Selection tool
- `d`: Bezier pen (curves & lines)
- `e`: Circle / ellipse
- `r`: Rectangle
- `t`: Text tool
- `a`: Node edit tool
- `f`: Fill and stroke dialog
- `x`: Align and distribute dialog
- `w`: Toggle snapping
- `q` / `Esc`: Deselect all

---

## Web Portal & Build Pipeline

The publishing pipeline generates a static web portal showcasing all compiled master scripts.

### Features

- **Classic Academic Index Design**: Styled in classic serif typography with dark mode support.
- **Direct Master PDF Viewer**: Embedded in-browser PDF reader with download and full-window links.
- **Layout Switcher**: Toggle between table view and responsive grid view.
- **Instant Search**: Real-time filtering by course title, code, and section.
- **Tag Filtering**: Filter courses by institution (BULME, TU Graz) and semester (Semester 8, etc.) using interactive bracketed tag chips.
- **Impressum**: Austrian legal notice and contact information.

### Local Build Commands

```bash
# Compile all Typst documents to PDF and generate Hugo content
python3 scripts/build_site.py --build-hugo

# Start local Hugo development server
hugo server -s site
```

### Automated Deployment

Pushes to the `main` branch trigger a GitHub Actions workflow (`.github/workflows/deploy.yml`) that runs `scripts/build_site.py`, builds the site with Hugo, and publishes the static output to GitHub Pages.
