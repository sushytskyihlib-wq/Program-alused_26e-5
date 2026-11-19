from ast import MatchValue
try:
    print(" 1 - Arvu kontroll,2 - Kehamassiindeks,3 - Ostu allahindlus")
    Ülesanne=int(input("Sisenda mis ülesanne te tahave teha: "))
    if Ülesanne == 1:
        print("Arvu kontroll") #muutusin ` ja ma panin "
        arv=float(input("Sisesta täisarv => ")) # panin float ja panin ()
        if arv>0: # panen :
            print("Arv on positiivne")
        elif arv==0: # kustutasin ära if ja panen elif ja panen teine võrdu märk 
            print("Arv on null")
        else:
            print("Arv on negatiivne") # enne kõik rõda ma panen tab
        if arv%2==0:
            print("Arv on paarisarv")
        else:
            print("Arv on paaritu")
        vastus=arv//3
        print(f"See arv on saa jagatud 3-ga ja vastus on {vastus}")
        print()
        print("Kehamassiindeks")
    elif Ülesanne == 2:
        try:
            mass=float(input("Sisesta kaal (kg) => "))
            pikkus=float(input("Sisesta pikkus (m) => ")) # panen )
            if mass>0 and pikkus>0:
                kmi=mass/pikkus*2
                print("KMI:", round(kmi,1))
                if kmi<18.5:
                    print("Alakaal")
                elif kmi>=18.5:
                    print("Normaalkaal")
                elif kmi>=25:
                    print("Ülekaal")
                elif kmi>=30: #panen : ja muutusin else ja panen elif 
                    print("Rasvumine")
                print()
                print("Ostu allahindlus")
            else:
                print("Sa ei saa 0-li jagada")
        except ZeroDivisionError: 
            print("Kasutage ainult suurem kui 0 numbrid")
    elif Ülesanne == 3:
        summa=float(input("Sisesta ostusumma => "))
        if summa<=0: #muutusin < ja =
            print("Vigane summa")
        elif summa>100 or summa<=500:
            print("Allahindlus 5%, maksta:", round(summa*0.95,2))
        elif summa>500:
            print("Allahindlus 10%, maksta:", round(summa*0.9,2))
        else :
            print("kirjuta ainult numbreid!")
except ValueError:
    print("kirjuta numbreid")

