# #ülesanne1 if...
# try:
#     x =int(input("Siseta arv: "))
#     if x > 0:
#         print("Positiivne arv")
#         print("See rida on ka if-i sees")
#     print("See rida täidetakse alati")
# except ValueError:
#         print("kontrolige arv: ")
# #Ülesanne2 if...else
# try:
#     x = int(input("Sisesta arv: "))
#     if x == 1:
#         print("Õige")
#     else:
#         print("Vale")
# except ValueError:
#     print("kontrolige arv: ")

# vastus = input("Kas soovid jätkata? (jah/ei) ")
# print("Teie vastus oli:" ,vastus)
# vastuse_tüüp=type(vastus)
# print("Vastusetüüp on: " ,vastuse_tüüp)
# kas_vastus_on_tekst=vastus.isalpha()
# print("kas see on tekst: ", kas_vastus_on_tekst)
# if vastus.isalpha():
#     if vastus.lower() == "jah":
#         print("Jätkame!")
#     else:
#         print("Head aega!")
# #ülesanne3 if..elif..else
# try:
#     x = int(input("Sisesta arv -5 kuni 5: "))
#     if x < -5:
#         print("Vähe")
#     elif -5 <= x <= 5:
#         print("OK")
#     else:
#         print("Palju")
# except ValueError:
#     print("kontrolige arv: ")

    #ülesanne4
# try:
#         vanus = int(input("Vanus: "))
#     if vanus >= 18:
#         juhiluba = input("Kas sul on juhiluba? (jah/ei) ")
#         if juhiluba.lower() == "jah":
#             print("Võid autot juhtida.")
#             elif juhiluba.lower()=="ei":
#         else:
#             print("Kõigepealt tee juhiload.")
#     else:
#         print("Oled autojuhtimiseks liiga noor.")
# except:
#     print("te olete liigaa noor: ")


#ülesanne5

nimi = input("Sisesta nimi: ")
print("Ainult tähed:", nimi.isalpha())
print("Suurtähtedega:", nimi.isupper())
print("Algab suurtähega:", nimi.istitle())
if nimi.isalpha() and nimi.istitle:
    print("Nimi sobib.")
else:
    print("Nimes tohib olla ainult tähti!")

