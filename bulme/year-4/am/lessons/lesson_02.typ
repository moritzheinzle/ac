#import "../template.typ": *
#import "../math.typ"
#lesson("1. HÜ", date: "06.10.2026")



5.29 )
$ p(h) = p_0 dot e^(-h/H) $

Wobei: $quad$ $p_0 = 1013 #text("hPa") quad H = 7991 #text("m")$ \
a) Linearisier die Funktion um $h = 0$ m 

Dafür nehmen wir das Taylor-Polynom 1.Grades: 
$ s(h) = p(h_0) + (p'(h_0))/(1!) dot x $

Die Ableitung läßt sich mithilfe der Kettenregeln berechnen:
$  (dif p)/(dif h) &= p_0 dot e^(-h/H) dot (-1/H) $

Für $h = 0$ fällt der $e$ Term auf 1 also weg: 
$ (dif p)/(dif h) (0) = - p_0/H $


Linearisierung:
$ s(h) &= p_0 + (-p_0/H)/(1!)h \
  s(h) &= 1013 + (-1013/7991)/(1)h
$

b) Bestimme die Höhe bei der die Differenz der Annährung un der originalen Funktion 5% überschreiten

$ d(h) &= (s(h) - p(h))/p(h) \
   &= (p_0 -p_0/H h - p_0 dot e^(-h/H))/(p_0 dot e^(-h/H)) \ 
   &= (p_0  dot (1 - h/H - e^(-h/H)))/(p_0 dot e^(-h/H)) \ 
   &= (1 - h/H - e^(-h/H))/(e^(-h/H)) \
   &= (1 - h/H) dot 1/(e^(-h/H)) - (e^(-h/H))/(e^(-h/H)) \
   &= (1- h/H) dot e^(h/H) - 1
  $

Die 0.05 % einsetzen:
$ |d(h)| &= 0.05  \ 
  -[(1- h/H) dot e^(h/H) - 1] &= 0.05
$

TR: solve

$h = 2293.8$ m

5.31)

