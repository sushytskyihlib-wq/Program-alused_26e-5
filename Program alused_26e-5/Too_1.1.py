print("tere,maailm")
nimi=input("Siseda oma nimi: ")
vanus=int(input("Kui vana sa oled: "))
print("Tere,",nimi)
print("Sa oled",vanus,".aastat vana",sep=" ")
try:
    print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} .aastat vana.")
except ValueError:
    print("Palun kontrollige siseta")