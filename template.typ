#let info = yaml("info.yml")

#let project(
  title: auto,
  course: auto,
  author: "Heinzle Moritz",
  date: none,
  lang: "en",
  table_of_contents: true,
  body,
) = {
  let doc-title = if title != auto and title != none { title } else { info.at("title", default: "Lecture Notes") }
  let doc-course = if course != auto and course != none { course } else { info.at("course", default: info.at("short", default: "")) }
  let doc-author = if author != auto and author != none { author } else { info.at("author", default: "Heinzle Moritz") }
  let doc-date = if date != none { date } else { datetime.today().display("[day] [month repr:long] [year]") }

  set document(title: doc-title, author: doc-author)
  set page(
    paper: "a4",
    margin: (x: 2.2cm, top: 2.5cm, bottom: 2.5cm),
    header: context {
      if counter(page).get().first() > 1 {
        text(9pt, fill: luma(100))[
          #if doc-course != "" [#doc-course] else [#doc-title]
          #h(1fr)
          #doc-title
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
    #text(22pt, weight: "bold")[#doc-title] \
    #if doc-course != "" [
      #v(0.4em)
      #text(13pt, fill: luma(90))[#doc-course] \
    ]
    #v(0.3em)
    #text(10pt, fill: luma(120))[#doc-author #if doc-author != "" [---] #doc-date]
    #v(1.2cm)
  ]

  if table_of_contents {
    outline(indent: 1.5em)
    pagebreak()
  }

  body
}

#let lecture-notes(
  title: auto,
  course: auto,
  author: "Heinzle Moritz",
  date: none,
  lang: "en",
  table_of_contents: true,
  body,
) = project(
  title: title,
  course: course,
  author: author,
  date: date,
  lang: lang,
  table_of_contents: table_of_contents,
  body,
)

#let conf(
  title: auto,
  subject: auto,
  course: auto,
  author: "Heinzle Moritz",
  pagebreak_each_lesson: true,
  table_of_contents: true,
  lang: "en",
  doc,
  ..rest
) = project(
  title: title,
  course: if course != auto { course } else { subject },
  author: author,
  lang: lang,
  table_of_contents: table_of_contents,
  doc,
)

#let lesson(title, date: none) = {
  let d = if date != none { date } else { datetime.today().display("[day] [month repr:long] [year]") }
  heading(level: 1)[#title]
  text(9pt, fill: luma(120))[#d]
  v(0.6em)
}

#let note(title: "Note", body) = {
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
