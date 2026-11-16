from math import*
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
try:
    pikuss=float(input("Sisenda pikkus: "))
    laius=float(input("Sisenda laius: "))
    pindala=pikuss*laius
    if pikuss.isdigit() and laius.isdigit() : 
        print(f"Pindal on {pindala} ruut meetrid.")
        valik=input(" Kas te tahate remonti teha? (jah/ei): ").lower()
        if valik=="Jah":
            try:
                rm_hind=float(input("Sisenda ruutmeetri hind: "))
                hind=round(pindala*rm_hind,2)
                print(f"Põrand maksab {hind} eurot.")
                valik=input("Kas te tahate remonti teha ise? (jah/ei)").lower()
                if valik=="jah":
                    print(f"Põrand maksab {hind} eurot.")
                elif valik=="ei":
                    try:
                        töö_hind=float(input("Sisesta töö hind:"))
                        hind=round(hind+pindala*töö_hind,2)
                        print(f"Remoonti teeb profesionaal ja see maksab {hind} eurot.")
                    except ValueError:
                        print("kontrolige valik")
            except ValueError:
                print("Kontrolige arv ")
        else:
            print("Remonti ei teha")
    else:
        print("Kirjutage ainult numbreit")
except ValueError:
    print("kontrollige arv ")
