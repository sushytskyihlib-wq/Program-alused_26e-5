from random import * #random
from math import * #pi
# print("tere,maailm")
# nimi=input("Siseda oma nimi: ")
# print("Tere,",nimi)
# try:
#     vanus=int(input("Kui vana sa oled: "))
#     print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} .aastat vana.")
# except ValueError:
#     print("Palun kontrollige siseta")
# vanus=18 #int-täisarv
# eesnimi="jaak" #str-sõne
# pikkus=16.5 #float-kümnendmurd
# kas_käib_koolis=True #bool-tõeväärtus
# print(f"Vanus:{vanus}, tüüp:{type(vanus)}")
# print(f"Eesnimi:{eesnimi}, tüüp:{type(eesnimi)}")
# print(f"Pikkus:{pikkus}, tüüp:{type(pikkus)}")
# print(f"Käib koolis:{kas_käib_koolis}, tüüp:{type(kas_käib_koolis)}")
# kommide_arv=randint(1, 100)
# print(f"Laud on {kommide_arv} kommi. ")
# try:
#     kommid=int(input("mitu kommi soovid ära võtta? "))
#     kommide_arv -= kommid
#     print(f"Laud on nüüd {kommide_arv} kommi.")
# except ValueError:
#     print("Palun kontrollige numblid. ")

# try:
#     ümbermõõdu=float(input("Kui palju puu ümbermõõdu: "))
#     läbimõõdu=round(ümbermõõdu/pi,1)
#     print(f"Puu läbimõõt on {läbimõõdu}.")
#     N=float(input("Sisenda ristküliku esmete arv (N): "))
#     M=float(input("Sisenda teine arv (M): "))
#     diagonaal=round(sqrt(N**2 + M**2), 1) #sqrt() math moodulist
#     print(f"Ristküliku diadonaal on {diagonaal}.")
# except ValueError:
#     print("palun kontrollige nubrei.")

# try:
#     aeg = float(input("Mitu tundi kulus sõiduks? "))
#     teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#     kiirus = aeg / teepikkus

#     print("Sinu kiirus oli " + str(kiirus) + " km/h")
# except ValueError:
#     print("Palun kontrollige ared.")

arv1=randint(1, 100)
arv2=randint(1, 100)
arv3=randint(1, 100)
arv4=randint(1, 100)
arv5=randint(1, 100)
summa=arv1+arv2+arv3+arv4+arv5
keskmine=summa/5
print(f"Summa: {summa}, Keskmine: {keskmine}")
try:
    jagaja=int(input("Sisenda arv, millega on jagada: "))
    tulemus=summa/jagaja
    print("tulemus:", tulemus)
    print("Täisarvuline osa: ", int(tulemus))

    print("Jääk:", summa % jagaja)
except ValueError:
    print("kontrollige sisendused")