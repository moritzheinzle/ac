#import "template.typ": conf, lesson, definition, theorem, homework

#show: doc => conf("Discrete Mathematics", doc)

#lesson("Propositional Logic", date: "2026-10-01")

We introduce the basic operators for boolean logic. Let $P$ and $Q$ be propositions. 

#definition("Conjunction")[
  The conjunction of $P$ and $Q$, denoted $P and Q$, is true if and only if both $P$ and $Q$ are true.
]

#theorem(title: "De Morgan's Laws")[
  For any two propositions $P$ and $Q$, the following equivalences hold:
  $ not (P and Q) &equiv not P or not Q \
    not (P or Q)  &equiv not P and not Q $
]

#homework("2026-10-08")[
  + Complete exercises 1.1 through 1.5.
  + Prove De Morgan's laws using complete truth tables.
]

#lesson("Set Theory")
Today we shift focus to collections of distinct objects...
 and i love you
