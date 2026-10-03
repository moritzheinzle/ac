#let definition(..args) = {
  let pos = args.pos()
  let named = args.named()
  let body = none
  let title = named.at("title", default: none)

  if pos.len() == 1 {
    body = pos.at(0)
  } else if pos.len() >= 2 {
    title = pos.at(0)
    body = pos.at(1)
  }

  let header = if title != none and title != "" [Definition (#title)] else [Definition]
  block(
    fill: rgb("#fef9e7"),
    stroke: (left: 3.5pt + rgb("#d97706")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#d97706"))[#header] \
    #v(2pt)
    #body
  ]
}

#let theorem(..args) = {
  let pos = args.pos()
  let named = args.named()
  let body = none
  let title = named.at("title", default: none)

  if pos.len() == 1 {
    body = pos.at(0)
  } else if pos.len() >= 2 {
    title = pos.at(0)
    body = pos.at(1)
  }

  let header = if title != none and title != "" [Satz (#title)] else [Satz]
  block(
    fill: rgb("#f0f4f8"),
    stroke: (left: 3.5pt + rgb("#2563eb")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#2563eb"))[#header] \
    #v(2pt)
    #body
  ]
}

#let lemma(..args) = {
  let pos = args.pos()
  let named = args.named()
  let body = none
  let title = named.at("title", default: none)

  if pos.len() == 1 {
    body = pos.at(0)
  } else if pos.len() >= 2 {
    title = pos.at(0)
    body = pos.at(1)
  }

  let header = if title != none and title != "" [Lemma (#title)] else [Lemma]
  block(
    fill: rgb("#f3f0ff"),
    stroke: (left: 3.5pt + rgb("#7c3aed")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#7c3aed"))[#header] \
    #v(2pt)
    #body
  ]
}

#let corollary(..args) = {
  let pos = args.pos()
  let named = args.named()
  let body = none
  let title = named.at("title", default: none)

  if pos.len() == 1 {
    body = pos.at(0)
  } else if pos.len() >= 2 {
    title = pos.at(0)
    body = pos.at(1)
  }

  let header = if title != none and title != "" [Korollar (#title)] else [Korollar]
  block(
    fill: rgb("#f5f3ff"),
    stroke: (left: 3.5pt + rgb("#6d28d9")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#6d28d9"))[#header] \
    #v(2pt)
    #body
  ]
}

#let proposition(..args) = {
  let pos = args.pos()
  let named = args.named()
  let body = none
  let title = named.at("title", default: none)

  if pos.len() == 1 {
    body = pos.at(0)
  } else if pos.len() >= 2 {
    title = pos.at(0)
    body = pos.at(1)
  }

  let header = if title != none and title != "" [Proposition (#title)] else [Proposition]
  block(
    fill: rgb("#f0fdf4"),
    stroke: (left: 3.5pt + rgb("#059669")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#059669"))[#header] \
    #v(2pt)
    #body
  ]
}

#let proof(title: "Proof", body) = {
  block(
    width: 100%,
    stroke: (left: 2.5pt + rgb("#94a3b8")),
    inset: (left: 10pt, y: 6pt),
  )[
    #text(weight: "bold", style: "italic", fill: rgb("#475569"))[#title.] \
    #v(2pt)
    #body
    #align(right)[#text(fill: rgb("#64748b"))[$square$]]
  ]
}

#let formula(title: "Formel", body) = {
  block(
    fill: rgb("#f0fdf4"),
    stroke: (left: 3.5pt + rgb("#16a34a")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#16a34a"))[#title] \
    #v(2pt)
    #body
  ]
}

#let example(title: "Beispiel", body) = {
  block(
    fill: rgb("#f8fafc"),
    stroke: (left: 3.5pt + rgb("#64748b")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#475569"))[#title] \
    #v(2pt)
    #body
  ]
}

#let homework(deadline: none, body) = {
  block(
    fill: rgb("#eef5ff"),
    stroke: (left: 3.5pt + rgb("#2563eb")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#1d4ed8"))[Hausübung]
    #if deadline != none [ #h(1fr) #text(size: 9pt, style: "italic", fill: rgb("#3b82f6"))[Fällig: #deadline] ] \
    #v(2pt)
    #body
  ]
}
