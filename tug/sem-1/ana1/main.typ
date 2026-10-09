#import "template.typ": *

#show: project.with(
  title: "Analysis 1",
  course: "ANA1",
  author: "Heinzle Moritz",
)


= Subjunktion vs Bijunktion

$A arrow B$ kann man als $not A or B$ umschreiben

$(A arrow B) arrow.l.r (not A) or B$

Behauptung: Die Aussage (Bijunktion) "$A arrow B arrow.l.r (not A or B)$" hat immer den Wahrheitswert WAHR 


Satz: Sei $n in NN$ Dann ist n gerade genau dann wenn $n²$ gerade ist.


Sei $n in NN$ dann gilt:    $n text("gerade") arrow.l.r n² text("gerade")$


Sei $n in NN$ dann hat die Aussage "n $text("gerade") arrow.l.r n² text("gerade")$" hat immer den Wahrheitswert WAHR.

Behauptung: $A arrow.l.r.double B$


Fall 2: A ist W, B ist F: \
Das heist, n kann in der Form $n = 2 dot k$ fpr ein $k in NN$ geschrieben werden. Dann ist $n² = 4k² = 2 dot 2(k²)$. Das heißt, $n²$ ist gerade. Aber B ist F laut Annahme, d.h. $n²$ ist nicht gerade.

Fazit: Alle Fälle die auftreten können sind wahr.

Disjunktive Normalform


Existenzcantor $exists$: es gibt min. 1\
Allcantor $forall$: für alle

$forall$ mögen Schokolade negiert ist gleich wie $exists$ mögen Schokolade nicht.

$forall text("negiert") exists ... not...$


Scriptum Def 2.6.2
Folge ist konvergent mit Grenzwert a wenn:\
$(forall epsilon > 0) (exists N in NN)(forall n >= N): |a_n - a| < epsilon$

Folge $(a_n)_(n in NN)_(n in NN)$ ist nicht konvergent mit Grenzwer a:

$ not ((forall epsilon > 0) (exists N in NN)(forall n >= N): |a_n - a| < epsilon)$

$(exists e > 0) not ((exists N in NN) (forall n >= N) : |a_n - a | < epsilon)$

$(exists epsilon > 0) (forall N in NN)( exists n >= N): not (|a_n -a |) < epsilon)$

$(exists epsilon > 0)(forall N in NN) (exists n >= N) : |a_n -a| >= epsilon$

Alle Kinder mögen alle Süßigkeiten.
Alle Süßigkeiten werden von allen Kinder gemocht.

Gleiche Cantoren darf man vertauschen.

Für alle Kinder gibt es eine Süßigkeit die das Kind mag.$(forall... exists...)$ Es gibt eine Süßigkeit die alle Kinder mögen. $(exists... forall ...)$ 

Unterschiedliche Cantoren dar man nicht vertauschen.
#include "lessons/lesson_01.typ"
