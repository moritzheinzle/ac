# Typst University & School Note-Taking Setup

Inspiriert von **Gilles Castel's** legendärem Vorlesungs-Setup, optimiert für **Typst** und **Rofi (Wayland)** unter Linux.

---

## 🚀 Übersicht & Schnellstart

Dieses Setup ermöglicht es dir, blitzschnell Notizen in Vorlesungen und im Unterricht mit Typst zu erstellen und zu verwalten:

* **Minimalistisches Typst-Template (`template.typ`)**:
  * Sauberes A4-Layout mit deutscher Spracheinstellung und nativer Seitenzählung (`Seite X von Y`).
  * Elegante Kopfzeile mit Fach- und Vorlesungstitel.
  * Schnelle, schlanke Callout-Boxen (`#note`, `#definition`, `#theorem`, `#law`, etc.).
  * Voll kompatibel mit Typst 0.15+.
* **Rofi-Menüs (Wayland-nativ)**:
  * `rofi-courses`: Schnelles Wechseln des aktiven Fachs.
  * `rofi-lectures`: Vorlesung auswählen oder mit `Strg+N` sofort eine neue Lektion beginnen.
  * `rofi-notes`: Zentrales Schnellmenü (Neue Lektion, Lektion öffnen, Fach wechseln, Live-Vorschau, Kompilieren).
* **CLI-Kommando (`new-lesson`)**:
  * Erstellt eine nummerierte Lektionsdatei (`lesson_02.typ`), bindet sie automatisch in `main.typ` ein und öffnet sie in Neovim (`nvim`).
* **Automatischer Symlink**:
  * `/home/mo/ac/current-course` zeigt immer auf das aktuell aktive Fach.
  * `/tmp/current_course` enthält das Kürzel (z. B. für Waybar/Polybar).

---

## 📁 Ordnerstruktur

```text
/home/mo/ac/
├── template.typ                  # Zentrales Typst-Template
├── current-course -> ...         # Symlink auf das aktive Fach
├── scripts/                      # Python- & Rofi-Skripte
│   ├── config.py                 # Konfiguration (Pfade, Editor, Terminal)
│   ├── courses.py                # Fächerverwaltung & YAML-Parser
│   ├── lectures.py               # Lektionsverwaltung & Typst-Integration
│   ├── rofi.py                   # Rofi-Wrapper (Wayland-kompatibel)
│   ├── rofi-courses.py           # Fachauswahl via Rofi
│   ├── rofi-lectures.py          # Lektionsauswahl via Rofi
│   ├── rofi-notes.py             # Dashboard-Menü
│   └── new-lesson.py             # CLI-Ersteller
└── bulme/year-4/                 # Fächerverzeichnis
    ├── am/                       # Angewandte Mathematik
    │   ├── info.yaml             # Metadaten (Titel & Kürzel)
    │   ├── template.typ -> ...   # Symlink zum Template
    │   ├── main.typ              # Master-Dokument
    │   └── lessons/              # Einzelne Lektionen
    │       ├── lesson_01.typ
    │       └── lesson_02.typ
    ├── wir3/                     # Wirtschaft und Recht 3
    ├── hwe/                      # Hardwareentwicklung
    └── ...
```

---

## ⌨️ Niri-Tastenkombinationen

In deiner `~/.config/niri/config.kdl` sind folgende Tastenkombinationen aktiv:

```kdl
// Rofi & System
Mod+D         hotkey-overlay-title="App-Launcher: rofi"   { spawn "rofi" "-show" "drun"; }
Mod+Shift+D   hotkey-overlay-title="Befehl ausführen"     { spawn "rofi" "-show" "run"; }
Mod+Tab       hotkey-overlay-title="Fenster wechseln"     { spawn "rofi-windows"; }
Alt+Tab       hotkey-overlay-title="Fenster wechseln"     { spawn "rofi-windows"; }
Mod+BackSpace hotkey-overlay-title="Power-Menü"           { spawn "rofi-power"; }
Mod+Return    hotkey-overlay-title="Terminal: alacritty"  { spawn "alacritty"; }

// Gilles Castel Typst & Inkscape Setup
Mod+N            hotkey-overlay-title="Typst: Lektion öffnen / neu" { spawn "rofi-lectures"; }
Mod+Shift+N      hotkey-overlay-title="Typst: Fach wechseln"        { spawn "rofi-courses"; }
Mod+Alt+N        hotkey-overlay-title="Typst: Notizen-Menü"          { spawn "rofi-notes"; }
Mod+Alt+F        hotkey-overlay-title="Typst: Inkscape-Figuren"     { spawn "rofi-figures"; }
Mod+Shift+Return hotkey-overlay-title="Terminal im aktiven Fach"    { spawn "ac-term"; }
Mod+E            hotkey-overlay-title="Neovim im aktiven Fach"      { spawn "ac-nvim"; }
```

---

## 📊 Statusleiste (Noctalia)

Das aktive Fach wird in deiner Noctalia-Statusbar über das native Plugin `mo/current-course:bar` angezeigt:
* **Anzeige**: `📚 <KÜRZEL>` (z. B. `📚 AM`).
* **Interaktiv**: Ein Klick auf das Widget öffnet sofort `rofi-courses` zur Fachauswahl.
* **Synchronisation**: Bei jedem Fachwechsel aktualisieren sich `/tmp/current_course` und die Bar automatisch in Echtzeit.

---

## 🎨 Gilles Castel Inkscape-Setup (Optimiert für Typst)

Das Setup ermöglicht blitzschnelles Zeichnen mathematischer und technischer Skizzen während des Unterrichts:

* **Neovim-Keymaps**:
  * `<Leader>if`: Neue Inkscape-Figur erstellen (Titel eingeben $\to$ SVG wird erzeugt, `#figure(...)` Code wird direkt an den Cursor eingefügt, Inkscape öffnet sich).
  * `<Leader>ie`: Bestehende Figuren über Rofi durchsuchen und in Inkscape öffnen.
  * Snippet `incfig` oder `fig`: Schnelles Einfügen von Figuren-Blöcken.
* **Typst-Optimierung**:
  * Nativer Vektor-SVG-Import ohne Zwischenkompilierung (`#figure(image("../figures/...svg"))` oder `#incfig("slug")`).
  * Default-Schriftart im SVG ist `Libertinus Serif` / `Linux Libertine` (identisch zum Dokumententext).
* **Ergonomische Inkscape-Tastenkürzel** (`~/.config/inkscape/keys/default.xml`):
  * `s` $\to$ Auswahl-Werkzeug (Select)
  * `d` $\to$ Bézier-Stift (Pen / Kurven & Linien)
  * `e` $\to$ Kreis / Ellipse (Arc)
  * `r` $\to$ Rechteck (Rect)
  * `t` $\to$ Text
  * `a` $\to$ Knoten bearbeiten (Node)
  * `z` $\to$ Zoom
  * `f` $\to$ Füllung und Kontur (Dialog)
  * `x` $\to$ Ausrichten und Verteilen (Dialog)
  * `w` $\to$ Einrasten / Snapping umschalten
  * `q` / `Esc` $\to$ Alles abwählen (Deselect)
* **Rofi-Figuren-Manager**:
  * `Mod+Alt+F` oder `rofi-figures`: Dashboard zum Erstellen, Bearbeiten und Öffnen des Figuren-Ordners.

---

## 📝 Verwendung

### 1. Über Rofi
* Drücke `Mod+N` (oder `rofi-lectures`): Lektion auswählen oder mit `➕ Neue Lektion erstellen` direkt anlegen.
* Drücke `Mod+Shift+N` (oder `rofi-courses`): Fach wechseln.
* Drücke `Mod+Alt+N` (oder `rofi-notes`): Notizen-Dashboard (Lektion, Fach, Inkscape-Figuren, Live-Vorschau, Master-Kompilierung).
* Drücke `Mod+Alt+F` (oder `rofi-figures`): Figuren anlegen und bearbeiten.

### 2. Über Neovim
* `<Leader>tp`: Live-Vorschau mit Zathura starten / stoppen.
* `<Leader>if`: Neue Inkscape-Figur anlegen und Code einfügen.
* `<Leader>ie`: Figur bearbeiten.
* `<Leader>tm`: Hauptdokument (`main.typ`) in Tinymist pinnen.

---

## 📄 Aufbau einer Lektion (`lesson_01.typ`)

Eine Lektion ist bewusst so einfach und sauber wie möglich gehalten:

```typst
#import "../template.typ": *

#lesson("Einführung in Vektorräume", date: "02.10.2026")

== Grundbegriffe

Ein Vektorraum $V$ über einem Körper $K$ erfüllt...

#note(title: "Wichtige Eigenschaft")[
  Die Vektoraddition ist kommutativ und assoziativ.
]
```

## 📄 Aufbau des Master-Dokuments (`main.typ`)

```typst
#import "template.typ": *

#show: project.with(
  title: "Angewandte Mathematik",
  course: "AM",
  author: "Moritz",
)

// Inkludierte Lektionen (werden automatisch durch new-lesson hinzugefügt)
#include "lessons/lesson_01.typ"
```
