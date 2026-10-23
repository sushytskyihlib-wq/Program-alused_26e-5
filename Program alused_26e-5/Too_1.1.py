print("tere,maailm")
nimi=input("Siseda oma nimi: ")
print("Tere,",nimi)
try:
    vanus=int(input("Kui vana sa oled: "))
    print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} .aastat vana.")
except ValueError:
    print("Palun kontrollige siseta")