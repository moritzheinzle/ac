// ==============================================================================
// Academic Mathematics Framework for Typst
// Clean, professional, and free of oversaturated "AI-slop" color palettes.
// ==============================================================================

// --- Internal Helper for Theorem-like Environments ---
#let _parse-env-args(args) = {
  let pos = args.pos()
  let named = args.named()
  let title = named.at("title", default: none)
  let body = none

  if pos.len() == 1 {
    body = pos.at(0)
  } else if pos.len() >= 2 {
    title = pos.at(0)
    body = pos.at(1)
  }

  (title: title, body: body)
}

#let _academic-block(
  label: "",
  title: none,
  accent: rgb("#1e3a5f"),
  bg: rgb("#f8fafc"),
  border: rgb("#e2e8f0"),
  body,
) = {
  let has-title = title != none and title != "" and title != []
  let header = [
    #text(weight: "bold", fill: accent)[#label]
    #if has-title [
      #text(weight: "bold", fill: rgb("#334155"))[(#title)]
    ]
  ]

  block(
    fill: bg,
    stroke: (
      left: 2.5pt + accent,
      rest: 0.5pt + border,
    ),
    inset: (x: 10pt, top: 8pt, bottom: 8pt),
    radius: (right: 3pt),
    width: 100%,
    breakable: true,
  )[
    #header \
    #v(2pt)
    #body
  ]
}

// ==============================================================================
// Core Academic Environments
// ==============================================================================

// 1. Definition: Rigorous introduction of a mathematical term, concept, or set.
#let definition(..args) = {
  let (title, body) = _parse-env-args(args)
  _academic-block(
    label: "Definition",
    title: title,
    accent: rgb("#0f172a"), // Deep charcoal
    bg: rgb("#f8fafc"),
    border: rgb("#e2e8f0"),
    body,
  )
}

// 2. Theorem: Major, fundamental mathematical statement proven to be true.
#let theorem(..args) = {
  let (title, body) = _parse-env-args(args)
  _academic-block(
    label: "Theorem",
    title: title,
    accent: rgb("#1e3a5f"), // Academic Prussian Navy
    bg: rgb("#f8fafc"),
    border: rgb("#cbd5e1"),
    body,
  )
}

// 3. Lemma: Subsidiary / auxiliary stepping-stone used to prove a larger theorem.
#let lemma(..args) = {
  let (title, body) = _parse-env-args(args)
  _academic-block(
    label: "Lemma",
    title: title,
    accent: rgb("#2b4c7e"), // Subdued Steel Navy
    bg: rgb("#f8fafc"),
    border: rgb("#e2e8f0"),
    body,
  )
}

// 4. Corollary: Immediate or direct consequence that follows naturally from a theorem.
#let corollary(..args) = {
  let (title, body) = _parse-env-args(args)
  _academic-block(
    label: "Corollary",
    title: title,
    accent: rgb("#475569"), // Slate Gray
    bg: rgb("#f8fafc"),
    border: rgb("#e2e8f0"),
    body,
  )
}

// 5. Proposition: Significant mathematical statement of independent interest (less monumental than a theorem).
#let proposition(..args) = {
  let (title, body) = _parse-env-args(args)
  _academic-block(
    label: "Proposition",
    title: title,
    accent: rgb("#1e3a5f"), // Academic Navy
    bg: rgb("#f8fafc"),
    border: rgb("#cbd5e1"),
    body,
  )
}

// 6. Axiom: Fundamental postulate accepted without proof as a foundation for reasoning.
#let axiom(..args) = {
  let (title, body) = _parse-env-args(args)
  _academic-block(
    label: "Axiom",
    title: title,
    accent: rgb("#0f172a"),
    bg: rgb("#f8fafc"),
    border: rgb("#e2e8f0"),
    body,
  )
}

// 7. Example: Concrete application, calculation, or instance illustrating concepts.
#let example(..args) = {
  let (title, body) = _parse-env-args(args)
  _academic-block(
    label: "Example",
    title: title,
    accent: rgb("#64748b"), // Muted Slate
    bg: rgb("#fafafa"),     // Soft Neutral
    border: rgb("#e5e7eb"),
    body,
  )
}

// 8. Remark / Note: Explanatory note, intuitive insight, warning, or historical context.
#let remark(..args) = {
  let (title, body) = _parse-env-args(args)
  let has-title = title != none and title != "" and title != []
  block(
    stroke: (left: 2pt + rgb("#94a3b8")),
    inset: (left: 10pt, top: 4pt, bottom: 4pt, right: 4pt),
    width: 100%,
    breakable: true,
  )[
    #text(weight: "bold", style: "italic", fill: rgb("#334155"))[Remark#if has-title [ (#title)]:]
    #h(4pt)
    #body
  ]
}

// 9. Proof: Step-by-step rigorous logical demonstration, ending with the standard open Q.E.D. tombstone.
#let proof(title: "Proof", body) = {
  let has-custom-title = title != none and title != "" and title != "Proof"
  block(
    stroke: (left: 1.5pt + rgb("#cbd5e1")),
    inset: (left: 10pt, top: 4pt, bottom: 4pt, right: 4pt),
    width: 100%,
    breakable: true,
  )[
    #text(weight: "bold", style: "italic", fill: rgb("#334155"))[
      Proof#if has-custom-title [ (#title)] else [. ]
    ]
    #body
    #align(right)[#text(fill: rgb("#64748b"))[$square$]]
  ]
}

// 10. Formula: Elegant callout box for highlighting key mathematical equations.
#let formula(title: none, body) = {
  block(
    fill: rgb("#f8fafc"),
    stroke: 0.5pt + rgb("#cbd5e1"),
    inset: (x: 10pt, y: 8pt),
    radius: 3pt,
    width: 100%,
    breakable: true,
  )[
    #if title != none and title != "" [
      #text(weight: "bold", fill: rgb("#1e293b"))[#title] \
      #v(2pt)
    ]
    #body
  ]
}

// ==============================================================================
// Exercise / Übung Environment
// English academic format with:
// - Task / Problem Statement (Angabe)
// - Working Steps / Derivation (Rechenweg)
// - Final Solution / Answer (Solution)
// ==============================================================================

#let _parse-uebung-args(args) = {
  let pos = args.pos()
  let named = args.named()

  let title = named.at("title", default: none)
  let task = named.at("task", default: named.at("statement", default: named.at("problem", default: named.at("angabe", default: none))))
  let steps = named.at("steps", default: named.at("working", default: named.at("work", default: named.at("derivation", default: named.at("rechenweg", default: none)))))
  let solution = named.at("solution", default: named.at("loesung", default: named.at("answer", default: named.at("result", default: none))))

  let p = pos
  if task == none and p.len() > 0 {
    if p.len() == 1 {
      task = p.at(0)
    } else if p.len() == 2 {
      if type(p.at(0)) == str {
        if title == none { title = p.at(0) }
        task = p.at(1)
      } else {
        task = p.at(0)
        if steps == none and solution == none {
          steps = p.at(1)
        } else if steps != none and solution == none {
          solution = p.at(1)
        }
      }
    } else if p.len() == 3 {
      if type(p.at(0)) == str {
        if title == none { title = p.at(0) }
        task = p.at(1)
        if steps == none { steps = p.at(2) }
      } else {
        task = p.at(0)
        if steps == none { steps = p.at(1) }
        if solution == none { solution = p.at(2) }
      }
    } else if p.len() >= 4 {
      if title == none { title = p.at(0) }
      task = p.at(1)
      if steps == none { steps = p.at(2) }
      if solution == none { solution = p.at(3) }
    }
  }

  (title: title, task: task, steps: steps, solution: solution)
}

#let uebung(..args) = {
  let parsed = _parse-uebung-args(args)
  let title = parsed.title
  let task = parsed.task
  let steps = parsed.steps
  let solution = parsed.solution

  let has-title = title != none and title != "" and title != []

  block(
    fill: rgb("#f8fafc"),
    stroke: (
      left: 2.5pt + rgb("#1e3a5f"), // Academic Navy Accent
      rest: 0.5pt + rgb("#cbd5e1"), // Clean hairline border
    ),
    inset: (x: 11pt, top: 9pt, bottom: 9pt),
    radius: (right: 3pt),
    width: 100%,
    breakable: true,
  )[
    // Header
    #text(weight: "bold", fill: rgb("#1e3a5f"))[Exercise]
    #if has-title [
      #text(weight: "bold", fill: rgb("#334155"))[--- #title]
    ] \
    #v(3pt)

    // 1. Task / Problem Statement (Angabe)
    #if task != none [
      #task
    ]

    // 2. Working Steps (Rechenweg) - rendered only if provided
    #if steps != none [
      #v(6pt)
      #line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))
      #v(3pt)
      #text(weight: "bold", size: 0.93em, fill: rgb("#475569"))[Working Steps:] \
      #v(2pt)
      #steps
    ]

    // 3. Solution (Solution) - rendered in a clean, high-contrast sub-box if provided
    #if solution != none [
      #v(6pt)
      #block(
        fill: rgb("#ffffff"),
        stroke: 0.5pt + rgb("#cbd5e1"),
        inset: (x: 9pt, y: 7pt),
        radius: 2.5pt,
        width: 100%,
      )[
        #text(weight: "bold", size: 0.93em, fill: rgb("#0f172a"))[Solution:]
        #h(4pt)
        #solution
      ]
    ]
  ]
}

// Alias for English preference
#let exercise = uebung

// 11. Homework: Clean, professional assignment box (backwards compatible)
#let homework(deadline: none, body) = {
  block(
    fill: rgb("#f8fafc"),
    stroke: (
      left: 2.5pt + rgb("#334155"),
      rest: 0.5pt + rgb("#cbd5e1"),
    ),
    inset: (x: 10pt, top: 8pt, bottom: 8pt),
    radius: (right: 3pt),
    width: 100%,
    breakable: true,
  )[
    #text(weight: "bold", fill: rgb("#1e293b"))[Homework Assignment]
    #if deadline != none [
      #h(1fr)
      #text(size: 8.5pt, style: "italic", fill: rgb("#64748b"))[Due: #deadline]
    ] \
    #v(3pt)
    #body
  ]
}
