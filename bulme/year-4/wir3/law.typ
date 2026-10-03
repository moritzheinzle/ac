// Recht & Gesetz Callouts für WIR3 (Wirtschaft und Recht)

#let law(num, statute: "", title: "", body) = {
  let header = if title != "" {
    [#title (§ #num #statute)]
  } else if statute != "" {
    [§ #num #statute]
  } else {
    [§ #num]
  }
  block(
    fill: rgb("#fef2f2"),
    stroke: (left: 3.5pt + rgb("#dc2626")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#dc2626"))[#header] \
    #v(2pt)
    #body
  ]
}

#let legal_principle(title: "Rechtsgrundsatz", body) = {
  block(
    fill: rgb("#f8fafc"),
    stroke: (left: 3.5pt + rgb("#0284c7")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#0284c7"))[#title] \
    #v(2pt)
    #body
  ]
}

#let case(title: "Fall / Beispiel", body) = {
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

  let header = if title != none and title != "" [Definition: #title] else [Definition]
  block(
    fill: rgb("#fefce8"),
    stroke: (left: 3.5pt + rgb("#ca8a04")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#ca8a04"))[#header] \
    #v(2pt)
    #body
  ]
}

#let important(body) = {
  block(
    fill: rgb("#fff1f2"),
    stroke: (left: 3.5pt + rgb("#e11d48")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#e11d48"))[Wichtig!] \
    #v(2pt)
    #body
  ]
}
