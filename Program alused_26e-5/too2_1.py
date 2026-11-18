from random import*
from math import*
from datetime import*
# nimi=(input("Mis on sinu nimi?: "))
# if nimi.upper()=="JUKU":
#     print("Lähme Jukuga kinno!")
#     if nimi.isupper():
#         print("Ära karju juku!")
#     elif nimi.islower():
#         print("Ära sosista, Juku!")
#     try:
#         vanus=int(input("Kui vana sa oled"))
#         if 0<=vanus<6:
#             pilet="tasutapilet"
#         elif 6<= vanus <=14:
#             pilet="lapsepilet"
#         elif 14<vanus<65:
#             pilet="täispilet"
#         elif 65>= vanus <=100:
#             pilet="sooduspilet"
#         else:
#             print("Viga andmetes.")
#         try:
#             print(f"Juku vanus on {vanus} aastat  seega on vaja osta{pilet}.")
#         except NameError:
#             print("pilet ei saa märata")
#     except ValueError:
#         print("Palun sisenda oma vanus numbriga ")
# else:
#     print("täna kinnno ei minna")

#2 ülesanne 
# pinginaabrid=["Anna","Juku","Vika","Dima"]
# nimi1=input("Sisesta esimene nimi: ")
# nimi2=input("Sisesta teine nimi: ")
# if nimi1.isalpha() and nimi2.isalpha(): 
#     if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
#         print(f"{nimi1} ja {nimi2} on täna pinginaabrid.")
#     else:
#         print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid")
# else:
#     print("viga: nimed paevad koosnema ainult tähtedest.")

# valik=input("Kas soovid otsida nimed algustähte järgi? (jah/ei):  ").lower()
# otsing=False
# if valik=="jah":
#     algustäht=input("Sisesta algustäht: ").capitalize()
#     for nimi in pinginaabrid:
#         if nimi.startswith(algustäht):
#             print(f"{nimi} algab tähtega {algustäht}.")
#             otsing=True
#     if not otsing:
#         print(f"Ühtegi nime, mis algab tähtega {algustäht}, ei leidnud.")
# else:
#     print("otsingut ei tehta.")
#ülesanne3
# try:
#     pikuss=float(input("Sisenda pikkus: "))
#     laius=float(input("Sisenda laius: "))
#     pindala=pikuss*laius
#     if pikuss.isdigit() and laius.isdigit() : 
#         print(f"Pindal on {pindala} ruut meetrid.")
#         valik=input(" Kas te tahate remonti teha? (jah/ei): ").lower()
#         if valik=="Jah":
#             try:
#                 rm_hind=float(input("Sisenda ruutmeetri hind: "))
#                 hind=round(pindala*rm_hind,2)
#                 print(f"Põrand maksab {hind} eurot.")
#                 valik=input("Kas te tahate remonti teha ise? (jah/ei)").lower()
#                 if valik=="jah":
#                     print(f"Põrand maksab {hind} eurot.")
#                 elif valik=="ei":
#                     try:
#                         töö_hind=float(input("Sisesta töö hind:"))
#                         hind=round(hind+pindala*töö_hind,2)
#                         print(f"Remoonti teeb profesionaal ja see maksab {hind} eurot.")
#                     except ValueError:
#                         print("kontrolige valik")
#             except ValueError:
#                 print("Kontrolige arv ")
#         else:
#             print("Remonti ei teha")
#     else:
#         print("Kirjutage ainult numbreit")
# except ValueError:
#     print("kontrollige arv ")
#Ülesanne4
# try:
#     hind=float(input("Sisenda on hind: "))
#     if hind > 700:
#         print("Allahindlus 30%")
#         odavhind=round(hind*0,3 ,2)
#         summa=hind-odavhind
#     else:
#         print("Allahindlust pole")
# except ValueError:
#     print("kontrolige arv ")
#ülesanne5
# try:
#     temperatuur=float(input("Kirjutage temperatur: "))
#     if temperatuur >=18:
#         print("See on hea temperatuur talvel.")
#     else:
#         print("see ei ole hea temperatuur talvel.")
# except ValueError:
#     print("Kirjutage nubriga valemeit. ")
#ülesanne6
# try:
#     kõrgus=float(input("Kui palju santimetri lõrgus te olete?: "))
#     if 120<=kõrgus<=160:
#         print("te olete lühike.")
#     elif 160<kõrgus<=180:
#         print("te olete keskmine kõrguses.")
#     elif 180<kõrgus<=200:
#         print("te olete kõrge.")
#     else:
#         print("ära valeta.")
# except ValueError:
#     print("Viga, kontrolige arv.")
#ülesnne7

#ulesanne8
# summa=0
# arve="Toode   Kogus   Hind    Kokku\n"
# valik=input("Kas soovid osta piima? (jah/ei): ")
# if valik.lower()=="jah":
#     kogus=input("Kui palju piima soovid osta (täisarv): ")
#     if kogus.isdigit():
#         kogus=int(kogus)
#         piim_hind=round(uniform(0.5, 3), 2)
#         print(f"Piima hind on {piim_hind} eurot.")
#         summa+=kogus*piim_hind
#         print(f"Piima kogusumma on {kogus*piim_hind} eurot.")
#         arve+=f"piim   {kogus}   {piim_hind}€    {kogus*piim_hind}€\n"
# else:
#     print("Selge: Piima ei taha")
# print(f"Kogusumma on:{round(summa,2)} eurot.")


# valik=input("Kas soovid osta sai? (jah/ei): ")
# if valik.lower()=="jah":
#     kogus=input("Kui palju sai soovid osta (täisarv): ")
#     if kogus.isdigit():
#         kogus=int(kogus)
#         sai_hind=round(uniform(0.5, 3), 2)
#         print(f"Sai hind on {sai_hind} eurot.")
#         summa+=kogus*sai_hind
#         print(f"Sai kogusumma on {round(kogus*sai_hind,2)} eurot.")
#         arve+=f"sai   {kogus}   {round(sai_hind,2)}€    {round(kogus*sai_hind,2)}€\n"
# print(f"Kogusumma on:{round(summa,2)} eurot.")
# valik=input("Kas soovid osta leiba? (jah/ei): ")
# if valik.lower()=="jah":
#     kogus=input("Kui palju leiba soovid osta (täisarv): ")
#     if kogus.isdigit():
#         kogus=int(kogus)
#         leib_hind=round(uniform(0.5, 3), 2)
#         print(f"Leiva hind on {round(leib_hind,2)} eurot.")
#         summa+=kogus*leib_hind
#         print(f"Leiva kogusumma on {round(kogus*leib_hind,2)} eurot.")
#         arve+=f"leib   {kogus}   {round(leib_hind,2)}€    {round(kogus*leib_hind,2)}€\n"
# print(f"Kogusumma on:{round(summa,2)} eurot.")
# # Lõpus kuva tšekk: iga ostetud toote nimi, kogus, hind ja summa ning kõige all kogusumma.
# print("Arve NR: 0000")
# print("--------------")
# print(arve)
#ülesanne9
# try:
#     arv_1=float(input("Kirjutage eesimene arv: "))
#     arv_2=float(input("Kirjutage teine arv: "))
#     arv_3=float(input("Kirjutage kolmas arv: "))
#     arv_4=float(input("Kirjutage neljas arv: "))
#     if 0<arv_1 and 0<arv_2 and 0<arv_3 and 0<arv_4: 
#         if arv_1==arv_2==arv_3==arv_4:
#             ruut=arv_1*arv_2*arv_3*arv_4
#         print(f"see on ruutu {ruut} diagonaal")
#     else:
#         print("see on ristkülik ")
# except ValueError:
#     print("kontrollige arv")

# try:
#     tegimine=["+","-","*","/"]
#     arv_1=float(input("Sisenda oma esimene arv: "))
#     arv_2=float(input("Sisenda oma teine arv: "))
#     print("Mis tegevus tetahate tegema?")
#     tegevus=(input("Sisenda tegevus: "))
#     if tegevus in tegimine :
#         print(f"{arv_1} {tegevus} {arv_2}={eval(f'{arv_1} {tegevus} {arv_2}')}")
# except ValueError:
#     print("Muutuge arv!")
# except ZeroDivisionError:
#     print("sa ei saa nulli jagada")

# date.today().year
# aastat=int(input("mis aasta sa oled sundinud?: "))


# try:
#     hind=float(input("Sisenda on hind: "))
#     if 0> hind <= 10:
#         print("Allahindlus 10%")
#         odavhind=round(hind*0,1 ,2)
#         summa=hind-odavhind
#     else:
#         print("Allahindlust pole")
#     if hind > 10:
#         print("Allahindlus 20%")
#         odavhind=round(hind*0,2 ,2)
#         summa=hind-odavhind
#     else:
#         print("Allahindlust pole")
# except ValueError:
#     print("kontrolige arv ")

#ülesanne14
try:
    inimesed=int(input("Sisenda kui palju inimesi on olemas: "))
    isted=int(input("Sisenda kui palju isted on olemas: "))
    if inimesed > 0 and isted > 0:
        buss=inimesed//isted
        print(f"meil on {buss} bussi")
        vimane_buss=inimesed % isted
        print(f"meil on {vimane_buss} inimesi vimasel bussil")
    else:
        print("kirjuta positiivne arv: ")
except ValueError:
    print("kirjuta ainult numbrit")