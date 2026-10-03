#import "@local/notes-template:0.1.0": *
#import "../circuit.typ": *

#lesson("Operationsverstärker: Differentiator und Integrator", date: "02.10.2026")

== 1. Bauteilübersicht

#component("LM741 / TL081", package: "DIP-8 / SOIC-8")[
  Standard-Operationsverstärker für analoge Signalverarbeitung.
  - Versorgungsspannung: $plus.minus 15"V"$
  - Eingangswiderstand: $r_e approx 2"M"Omega$ (Bipolar) bzw. $10^12 Omega$ (JFET TL081)
  - Leerlaufverstärkung: $A_0 > 10^5$
]

#spec(title: "Idealer Operationsverstärker")[
  - Eingangswiderstand: $R_"in" -> infinity$ (kein Eingangsstrom: $I_+ = I_- = 0$)
  - Ausgangswiderstand: $R_"out" -> 0$
  - Differenzverstärkung: $A_D -> infinity$
  - Virtuelle Masse am invertierenden Eingang bei gegengekoppeltem Betrieb: $U_- = U_+ = 0"V"$
]

== 2. Der Differenzierer (Differentiator)

Beim Differenzierer liegt am invertierenden Eingang eine Kapazität $C$ in Serie zum Eingangssignal, und im Rückkopplungszweig ein Widerstand $R$.

#formula(title: "Ausgangsspannung des Differenzierers")[
  $ u_a (t) = - R C dot (dif u_e (t))/(dif t) $
]

=== Herleitung nach Kirchhoff:
Da kein Strom in den OPV fließt ($I_- = 0$), gilt am Summierknoten:
$ I_C = - I_R $

Mit den Bauteilgleichungen:
$
  I_R &= (u_a(t))/R \
  I_C &= C dot (dif u_e (t))/(dif t)
$

Gleichsetzen liefert unmittelbar die Ausgangsspannung:
$ (u_a(t))/R = - C dot (dif u_e(t))/(dif t) quad <==> quad u_a(t) = - R C dot (dif u_e(t))/(dif t) $

== 3. Der Integrator

Beim Integrator sind Widerstand und Kondensator vertauscht: der Widerstand $R$ liegt am Eingang und der Kondensator $C$ in der Gegenkopplung.

#formula(title: "Ausgangsspannung des Integrators")[
  $ u_a(t) = - 1 / (R C) integral_(0)^(t) u_e(tau) dif tau + u_a(0) $
]

=== Herleitung:
Knotengleichung am invertierenden Eingang:
$ I_R = - I_C $

Einsetzen der Ströme:
$ (u_e(t))/R = - C dot (dif u_a(t))/(dif t) $

Integration beider Seiten von $0$ bis $t$:
$ integral_(0)^(t) (dif u_a(tau))/(dif tau) dif tau = - 1/(R C) integral_(0)^(t) u_e(tau) dif tau $

#note[
  In der Praxis benötigt der Integrator einen Parallelwiderstand $R_p$ zum Kondensator $C$, um die DC-Drift durch Eingangs-Offsetströme zu begrenzen.
]
