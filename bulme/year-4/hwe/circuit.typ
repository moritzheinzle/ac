// Bauteil- & Schaltungstechnik Callouts für HWE (Hardwareentwicklung)

#let component(name, package: "", body) = {
  let header = if package != "" [#name (#package)] else [#name]
  block(
    fill: rgb("#f8fafc"),
    stroke: (left: 3.5pt + rgb("#0284c7")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#0284c7"))[Bauteil: #header] \
    #v(2pt)
    #body
  ]
}

#let spec(title: "Spezifikation", body) = {
  block(
    fill: rgb("#fefce8"),
    stroke: (left: 3.5pt + rgb("#ca8a04")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#ca8a04"))[#title] \
    #v(2pt)
    #body
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
