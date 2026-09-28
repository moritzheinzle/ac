// Global academic preamble
#let conf(title, author: "Moritz", doc) = {
  set page(paper: "a4", margin: 2.5cm)
  set text(font: "New Computer Modern", size: 11pt)
  set heading(numbering: "1.1")
  set math.equation(numbering: "(1)")
  set par(justify: true)

  align(center)[
    #text(size: 20pt, weight: "bold")[#title] \
    #v(1em)
    #text(size: 14pt)[#author] \
    #v(2em)
  ]

  doc
}

// Automatic lesson counter
// Automatic lesson counter
#let lesson_counter = counter("lesson")

#let lesson(title, date: datetime.today().display()) = {
  lesson_counter.step()
  v(2em)
  block(
    fill: luma(248),
    inset: 12pt,
    radius: 4pt,
    width: 100%,
    stroke: luma(220),
  )[
    #text(weight: "bold", size: 14pt)[
      Lesson #context lesson_counter.display(): #title
    ]
    #h(1fr)
    #text(style: "italic", fill: luma(120))[#date]
  ]
  v(1em)
}

// Math and Assignment Environments
#let definition(term, body) = {
  block(
    fill: rgb("fdfdfd"),
    stroke: (left: 2pt + rgb("ffaa33")),
    inset: (left: 8pt, top: 8pt, bottom: 8pt),
    width: 100%
  )[
    #text(weight: "bold")[Definition (#term):] #body
  ]
}

#let theorem(title: none, body) = {
  block(
    stroke: (left: 2pt + black),
    inset: (left: 8pt, top: 8pt, bottom: 8pt),
    width: 100%
  )[
    #text(weight: "bold")[Theorem#if title != none [ (#title)]:] #body
  ]
}

#let homework(deadline, body) = {
  v(1em)
  block(
    fill: rgb("eef5ff"),
    stroke: (left: 4pt + rgb("4488ff")),
    inset: (left: 10pt, top: 8pt, bottom: 8pt, right: 8pt),
    width: 100%
  )[
    #text(weight: "bold", fill: rgb("2255aa"))[Homework Assignment] \
    #text(size: 9pt, style: "italic", fill: rgb("4488ff"))[Due: #deadline]
    #v(0.5em)
    #body
  ]
}
