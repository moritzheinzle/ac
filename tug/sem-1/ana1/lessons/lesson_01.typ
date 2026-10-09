#import "../template.typ": *

#lesson("Mengen", date: "06.10.2026")

== Axiom
Sind Grundlagen nach denen man Mathematik betreibt. Ganze Mathematik kommt aus den 10 Axiomen

ZFC ist die gängige Axiomatik. $->$ wurde in der Sprache der Mengen formuliert.

Alles was es gibt sind Mengen

Definition (Mengen) G.Cantor Eine Menge ist eine Zusammenfassung von wohlunterscheidbaren Objekten unseres Denkens oder unserer Anschauung zu einem Ganzen.

Eine Menge schreiben wir:
$ {a_1, a_2,a_3,...,a_n} $

Die leere Menge "$emptyset$" hat keine Elemente.

a ist Element von A: $a in A$

Seien A und B Mengen, dann schreiben wir:

Extensionalitätsprinzip: Mengen sind dadurch charakterisiert welche Elemente sie enthalten.

Eine Menge M ist Ding für das "$x in M$" eine Aussageform ist.

Eine Menge M ist ein Ding für das die Aussage  "$x in M$" für jedes x entweder Wahr oder Falsch ist.

$x in M$, statt $not (x in M)$ schreiben wir $x in.not M$

== Operationen

Vereinigung: Seien A und B mengen dann ist $A union B$ auch eine Menge.

$a in (A union B) <==> a in A or a in B$

Durchschnitt: Seien A und B Mengen, dann ist $A inter B$ auch eine Menge.

$a in (A inter B) <==> a in A and a in B$


Wenn A... Menge dann ist $A^c$ die Kompliment Menge. $x in A^c <==> x in.not A$


Behauptung: A,B,C...Mengen
$ A union (B inter C) = (A union B) inter (A union C) $


Wahrheitstabelle mit Aussagen machen wie $x in A$, $x in B$ das gleiche wie Logisches Distributivgesetz.

kartesisches Produkt: Seien A und B Mengen, dann ist:
$ A times B = {(a,b) | a in A, b in B} $
auch eine Menge (die Menge der geordneten Paare (a,b) mit a aus A und b aus B)

$ A = {1,2,3,4} quad B = {a,b} \
A times B = {(1,a),(2,a)...} $

$ A = {text("Anna"), text("Barbara"), text("Claudia")} quad quad B = { text("Apfel"), text("Birne"), text("Kiwi")} \
A times B = {(text("Anna, Apfel")),...}
$

 
Definition: Eine *Relation* ist eine Teilmenge eines kartesischen Produktes

z.b $R= {(text("Anna, Apfel"), (text("Anna, Birne")), (text("Claudia, Birne")),(text("Claudia, Kiwi"))} $


$ NN times NN$

$(m,n) in R$ wenn n ohne Rest durch m teilbar ist. $ (2,12) in R \
(7,13) in.not R $
