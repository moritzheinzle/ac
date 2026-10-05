#import "../template.typ": *
#import "../math.typ": *

#lesson("", date: "05.10.2026")

Wir verwende Unendliche Reihen um bestimmte Funktionen (e, sinus) zu definieren  und in jeder gewünschten Genauigkeit bezeichnen zu können.

#formula(title: "Unendliche Folge")[
  $ chevron.l a_1, a_2, a_3, ... a_n chevron.r $
]

#definition(title:"konvergent vs divergent")[
  Eine unendliche Reihe ist konvergent, wenn die Folge der Teilsummen *konvergent* ist.
  $ s_n = sum_(n=1)^infinity c_n $

  Gibt es keinen Grenzwert ist die Folge *divergent*
]


#formula(title:"Potenzreihe")[
  $ sum_(n=0)^infinity a_n x^n = a_0 dot x⁰ + a_1 dot x¹  a_2 dot x² + ... + a_n dot x^n $ 
]

#definition(title: "Taylor Reihe")[
  Sei $I subset.eq$ ein offenes Intervall, $x_0 in I$ eine feste Entwicklungsstelle und $f: I -> RR$ eine Funktion, die an der Stelle $x_0 $ undendlich oft differenzierbar ist $f in C^infinity (I)$

  $ T_f (x;x_0) = sum_(n=0)^infinity (f^(n) (x_0))/(n!) (x-x_0)^n $

]
