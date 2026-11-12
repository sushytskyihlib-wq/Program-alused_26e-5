nimi=(input("Mis on sinu nimi?: "))
if nimi.upper()=="JUKU":
    print("Lähme Jukuga kinno!")
    if nimi.isupper():
        print("Ära karju juku!")
    elif nimi.islower():
        print("Ära sosista, Juku!")
    try:
        vanus=int(input("Kui vana sa oled"))
        if 0<=vanus<6:
            pilet="tasutapilet"
        elif 6<= vanus <=14:
            pilet="lapsepilet"
        elif 14<vanus<65:
            pilet="täispilet"
        elif 65>= vanus <=100:
            pilet="sooduspilet"
        else:
            print("Viga andmetes.")
        try:
            print(f"Juku vanus on {vanus} aastat  seega on vaja osta{pilet}.")
        except NameError:
            print("pilet ei saa märata")
    except ValueError:
        print("Palun sisenda oma vanus numbriga ")
else:
    print("täna kinnno ei minna")
