#import "../template.typ": *
#import "../math.typ"
#pagebreak()
#lesson([HÜ $->$ 12.10.2026], date: "06.10.2026")



== 5.29 )
$ p(h) = p_0 dot e^(-h/H) $

Wobei: $quad$ $p_0 = 1013 #text("hPa") quad H = 7991 #text("m")$ \
=== a) // Linearisier die Funktion um $h = 0$ m 

Taylor-Polynom 1.Grades: 
$ s(h) = p(h_0) + (p'(h_0))/(1!) dot x $

Ableitung:
$  (dif p)/(dif h) &= p_0 dot e^(-h/H) dot (-1/H) $

Für $h = 0$ fällt der $e$ Term auf 1 also weg: 
$ (dif p)/(dif h) (0) = - p_0/H $


Linearisierung:
$ s(h) &= p_0 + (-p_0/H)/(1!)h \
  s(h) &= 1013 + (-1013/7991)/(1)h
$

=== b) // Bestimme die Höhe bei der die Differenz der Annährung un der originalen Funktion 5% überschreiten

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


$ h = 2293.8m $ 

== 5.31)
$ f(x) = 1 / sqrt(L dot (C + x)) = (L dot (C + x))^(-1/2) $

Wobei: $quad L = 0.2 #text("H") quad C = 50 #text("µF") = 50 dot 10^(-6) #text("F")$ \
=== a) // Linearisier die Funktion um $x = 0$

Taylor-Polynom 1.Grades:
$ s(x) = f(x_0) + (f'(x_0))/(1!) dot x $

Ableitung:
$ (dif f)/(dif x) &= -1/2 dot (L dot (C + x))^(-3/2) dot L \
  &= - L / (2 dot (L dot (C + x))^(3/2))
$

Für $x = 0$ einsetzen:
$ f(0) &= 1 / sqrt(0.2 dot 50 dot 10^(-6)) = 100 dot sqrt(10) approx 316.23 #text("s")^(-1) \
  f'(0) &= - 0.2 / (2 dot (0.2 dot 50 dot 10^(-6))^(3/2)) = - 10^6 dot sqrt(10) approx -3.1623 dot 10^6 #text("s")^(-1) #text("/F")
$

Linearisierung:
$ s(x) &= f(0) + f'(0) dot x \
  s(x) &= 316.23 - 3.1623 dot 10^6 dot x
$

=== b) // Bestimme die Werte für $x = 2 #text("µF") = 2 dot 10^(-6) #text("F")$

Genauer Wert:
$ f(2 dot 10^(-6)) = 1 / sqrt(0.2 dot (50 + 2) dot 10^(-6)) approx 310.09 #text("s")^(-1) $

Näherung:
$ s(2 dot 10^(-6)) = 316.23 - 3.1623 dot 10^6 dot 2 dot 10^(-6) approx 309.91 #text("s")^(-1) $

Güte der Näherung:
$ d &= |(s(x) - f(x))/f(x)| \
    &= |(309.91 - 310.09)/310.09| approx 0.058 %
$

Die Näherung weicht um weniger als 0.1% ab.


== 5.39)
$ i(t) = U_0 / R dot e^(-t/tau) $

Wobei: $quad U_0 = 100 #text("V") quad R = 2 #text("k")$#text("Ω") $ = 2000 #text("Ω") quad tau = 0.2 #text("s")$ \
$ I_0 = U_0 / R = 100 / 2000 = 0.05 #text("A") $

Ableitung:
$ (dif i)/(dif t) = - I_0/tau dot e^(-t/tau) $

=== a) // Linearisier die Stromstärke zum Zeitpunkt $t = 0$ s

Für $t = 0$ fällt der $e$ Term auf 1 weg:
$ i(0) = I_0 = 0.05 #text("A") quad (dif i)/(dif t) (0) = - I_0/tau = - 0.05/0.2 = -0.25 #text("A/s") $

Linearisierung:
$ s_a (t) &= i(0) + i'(0) dot t \
  s_a (t) &= 0.05 - 0.25 dot t = I_0 dot (1 - t/tau)
$

=== b) // Linearisier die Stromstärke zum Zeitpunkt $t = tau$

Für $t = tau$ einsetzen:
$ i(tau) = I_0 dot e^(-1) quad (dif i)/(dif t) (tau) = - I_0/tau dot e^(-1) $

Linearisierung:
$ s_b (t) &= i(tau) + i'(tau) dot (t - tau) \
  s_b (t) &= I_0 dot e^(-1) - I_0/tau dot e^(-1) dot (t - tau) \
  s_b (t) &= I_0 dot e^(-1) dot (2 - t/tau) \
  s_b (t) &= 0.01839 - 0.09197 dot (t - 0.2)
$

=== c) //Zeige die Nullstellen der linearisierten Funktionen

Fall a):
$ s_a (t) &= 0 \
  I_0 dot (1 - t/tau) &= 0 \
  1 - t/tau &= 0 arrow.r t = tau
$

Fall b):
$ s_b (t) &= 0 \
  I_0 dot e^(-1) dot (2 - t/tau) &= 0 \
  2 - t/tau &= 0 arrow.r t = 2 tau
$
