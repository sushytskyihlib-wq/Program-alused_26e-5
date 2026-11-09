from datetime import *
from math import * # from math kasutame pi
täna=date.today()
print(f"Täna on {täna}")

print(3 + 8 / (4 - 2) * 4)# kui me kasutame () vastus  on 19.0
print(3 + 8 / 4 - 2 * 4)# kui me ei kasutame () vastus on -3.0
#a=2R
try:
    r = float(input("kirjutage arv: "))
    a = 2 * r
    S1 = a ** 2
    print(f"S ruut on {S1}")
    P1 = 4 * a
    print(f"P ruut on {P1}")
    S2 = pi * (r ** 2)
    print("S ring on",round(S2,2))
    P2 = 2 * pi * r
    print("P ring on: ",round (P2,2))
except ValueError:
    print("kontrolige arv: ")


6378;km=6378000000
R=6378000000#mm
c=2*pi*R
d=25.75
suurus = c / d
print("suurus on: ", suurus)


print("Kill-Koll Kill-Koll Killadi-Koll Kill-Koll Killadi-Koll Kill-Koll Kill-Koll Kill-Koll Kill-Koll")


text="Rong see sõitis tsuhh tsuhh tsuhh,piilupart oli rongijuht. Rattad tegid rat tat taa, rat tat taa ja tat tat taa. Aga seal rongi peal, kas sa tead, kes olid seal? Rong see sõitis tuut tuut tuut, piilupart oli rongijuht. Rattad tegid kill koll koll, kill koll koll ja kill koll kill."
Vastus=text.title() 
print (Vastus)
#ülesanne7
try:
    A = float(input("Esimene arv: "))
    B = float(input("Teine arv: "))
    P=2*(A+B)
    S=A*B
    print(f"Perimeter on:{P}")
    print(f"Pind on:{S}")
except ValueError:
    print("kontrilige arv: ")

    #ülesanne8
kütus=int(input("Kui palju kütus te tangitute: "))
kilometr=int(input("Kui palju kilometrid te sõidate: "))
kulu=(kütus/kilometr)*100
print(f"Keskmine kulu 100 kilometrit on: {kulu} ")
#Ülesanne9
s=29.9/60
vastus=s*1000
print(vastus)
#ülesanne10
kõik_minuted=int(input("kui palju minuted on: "))
tund=kõik_minuted//60
minuted=kõik_minuted%60
print(f"see on {tund} tund ja {minuted} min ")

