#import "@local/notes-template:0.1.0": *
#import "law.typ": *

#show: doc => conf(
  title: "WIR3",
  subject: "BULME - Jahrgang 4",
  author: "Moritz",
  school: "BULME",
  class: "4AHET",
  school_year: "2026/27",
  lang: "de",
  pagebreak_each_lesson: true,
  table_of_contents: true,
  doc
)

// ==============================================================================
// LEKTIONEN
// ==============================================================================
#include "lessons/lesson_01.typ"
#include "lessons/lesson_02.typ"
