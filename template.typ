#let project(
  title: "Vorlesungsmitschrift",
  course: "",
  author: "Moritz",
  date: none,
  lang: "de",
  table_of_contents: true,
  body,
) = {
  let doc-date = if date != none { date } else { datetime.today().display("[day].[month].[year]") }

  set document(title: title, author: author)
  set page(
    paper: "a4",
    margin: (x: 2.2cm, top: 2.5cm, bottom: 2.5cm),
    header: context {
      if counter(page).get().first() > 1 {
        text(9pt, fill: luma(100))[
          #if course != "" [#course] else [#title]
          #h(1fr)
          #title
        ]
        v(-0.3em)
        line(length: 100%, stroke: 0.4pt + luma(200))
      }
    },
    footer: context [
      #align(center, text(9pt, fill: luma(120))[
        #counter(page).display()
      ])
    ],
  )

  set text(
    font: ("Libertinus Serif", "New Computer Modern"),
    size: 11pt,
    lang: lang,
  )

  set par(justify: true, leading: 0.65em)
  set heading(numbering: "1.1")

  v(0.6cm)
  align(center)[
    #text(22pt, weight: "bold")[#title] \
    #if course != "" [
      #v(0.4em)
      #text(13pt, fill: luma(90))[#course] \
    ]
    #v(0.3em)
    #text(10pt, fill: luma(120))[#author #if author != "" [---] #doc-date]
    #v(1.2cm)
  ]

  if table_of_contents {
    outline(indent: 1.5em)
    pagebreak()
  }

  body
}

#let lecture-notes(
  title: "Vorlesungsnotizen",
  course: "Vorlesung",
  author: "Moritz",
  date: none,
  body,
) = project(title: title, course: course, author: author, date: date, body)

#let conf(
  title: "Vorlesung",
  subject: "",
  author: "Moritz",
  pagebreak_each_lesson: true,
  table_of_contents: true,
  doc,
  ..rest
) = project(
  title: title,
  course: subject,
  author: author,
  table_of_contents: table_of_contents,
  doc,
)

#let lesson(title, date: none) = {
  let d = if date != none { date } else { datetime.today().display("[day].[month].[year]") }
  heading(level: 1)[#title]
  text(9pt, fill: luma(120))[#d]
  v(0.6em)
}

#let note(title: "Notiz", body) = {
  block(
    fill: rgb("#f5f7fa"),
    stroke: (left: 3.5pt + rgb("#2b6cb0")),
    inset: (x: 10pt, y: 8pt),
    radius: (right: 3pt),
    width: 100%,
  )[
    #text(weight: "bold", fill: rgb("#2b6cb0"))[#title] \
    #v(2pt)
    #body
  ]
}

#let incfig(name, caption: none, width: 80%) = {
  let file = if name.ends-with(".svg") or name.ends-with(".png") or name.ends-with(".pdf") {
    name
  } else {
    name + ".svg"
  }
  let img = image("figures/" + file, width: width)
  if caption != none {
    figure(img, caption: caption)
  } else {
    align(center, img)
  }
}
