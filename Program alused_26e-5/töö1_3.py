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



# Loo uus projekt.
# Kopeeri antud kood failisse.
# Otsi ja paranda programmis vead.
# Lisa kommentaar, kus kirjelda, mis parandatud oli.

# Kood:

# print('Arvu kontroll")
# arv=input("Sisesta täisarv => ")
# if arv>0
#     print("Arv on positiivne")
# else if arv=0:
#     print("Arv on null")
# else:
# print("Arv on negatiivne")
# if arv%2==0:
#     print("Arv on paarisarv")
# else:
#     print("Arv on paaritu")
# print()
# print("Kehamassiindeks")
# mass=float(input("Sisesta kaal (kg) => "))
# pikkus=float(input("Sisesta pikkus (m) => ")
# kmi=mass/pikkus*2
# print("KMI:", round(kmi,1))
# if kmi<18.5:
#     print("Alakaal")
# elif kmi>=18.5:
#     print("Normaalkaal")
# elif kmi>=25:
#     print("Ülekaal")
# elif kmi>=30
#     print("Rasvumine")
# print()
# print("Ostu allahindlus")
# summa=float(input("Sisesta ostusumma => "))
# if summa=<0:
#     print("Vigane summa")
# elif summa>100 or summa<=500:
#     print("Allahindlus 5%, maksta:", round(summa*0.95,2))
# elif summa>500:
#     print("Allahindlus 10%, maksta:", round(summa*0.9,2))
# else
#     print("Allahindlust pole, maksta:", summa
# Programmi tulemus:

 
# Arvu kontroll
# Sisesta täisarv => 9
# Arv on positiivne
# Arv on paaritu

# Kehamassiindeks
# Sisesta kaal (kg) => 85
# Sisesta pikkus (m) => 1.75
# KMI: 27.8
# Ülekaal

# Ostu allahindlus
# Sisesta ostusumma => 650
# Allahindlus 10%, maksta: 585.0
# Lisaülesanne:

# Muuda programmi nii, et alguses kuvatakse menüü ja kasutaja valib, millist osa käivitada:
 
# Vali programm:
# 1 - Arvu kontroll
# 2 - Kehamassiindeks
# 3 - Ostu allahindlus
# Sisesta valik (1-3) =>
# Käivitub ainult valitud osa. Kui kasutaja sisestab midagi muud kui 1, 2 või 3, kuvatakse teade Vigane valik.

# Lisa arvu kontrolli osasse kontroll, kas arv jagub 3-ga.
# Kehamassiindeksi osa ei tohi lubada sisestada nulli või negatiivset kaalu või pikkust.
# Lisaülesande tulemus (näide):

 
# Vali programm:
# 1 - Arvu kontroll
# 2 - Kehamassiindeks
# 3 - Ostu allahindlus
# Sisesta valik (1-3) => 1
# Arvu kontroll
# Sisesta täisarv => 9
# Arv on positiivne
# Arv on paaritu
# Arv jagub 3-ga
# Töö esitamine

# Salvesta projekt GitHubi. Visual Studios vali Git → Create Git Repository, logi sisse oma GitHubi kontoga ja vajuta Create and Push.
# ⚠️ Eemalda linnuke kastist Private repository, sest muidu õpetaja sinu tööd ei näe.
# Kontrolli, et kood on GitHubis. Ava brauseris oma repositoorium ja veendu, et seal on sinu .py fail, mitte ainult .gitignore ja .gitattributes.
# Kopeeri link aadressiribalt. Kui repositoorium on brauseris avatud, kopeeri aadress brauseri ülevalt aadressiribalt. Näiteks:
# https://github.com/kasutajanimi/Hindeline-too
# Lisa link Moodle’isse. Vajuta selles ülesandes Lisa esitus, kleebi link tekstikasti ja vajuta Salvesta muudatused.
# Hindamine:

# Kriteerium	Punktid
# Aastaaeg	15
# Kiiruse kontroll	15
# Taksosõit	15
# Kommentaarid	10
# try/except	15
# Lisa 1: menüü	10
# Lisa 2: allahindlus	10
# Lisa 3: negatiivne kiirus	10
# Kokku	100
