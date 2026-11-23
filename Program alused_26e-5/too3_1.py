while True:
     print("Vali ülesanne 1,2,3,4,5,6,7,8")
     valik=input("Sisenda arv(1-8): ")
     if valik=='1':
        i=0
        kogus=0
        while i<15:
            arv=float(input(f"{i+1}. arv: "))
            if arv.is_integer():
                kogus+=1
            i+=1
        print("Täisarve: ",kogus)
     elif valik=='2':
        try:
            A=int(input("Sisenda arv A: "))
            while A<0:
                A=int(input("Sisenda positiivsed täisarv: "))
            summa=0
            for i in range(1,A+1):
                 summa+=i
                 print("Summa: ",summa)
        except ValueError:
            print("Palun sisenda kehtiv täisarv.")
     elif valik=='3':
        i=0
        korutis=1
        while i<8:
            arv=int(input(f"{i+1}. arv: "))
            if arv>0:
                korutis*=arv
            i+=1
        print("korutevärtus: ",korutis)

     elif valik=='4':
        for i in range(10,21):
            print(f"{i}^2 on {i ** 2}")
     elif valik=='5':
        try:
            while True:
                i=0
            summa=1
            while i<8:
                arv=int(input(f"{i+1}. arv: "))
                if arv<0:
                    summa+=arv
                i+=1
            print("summa: ",summa)
        except ValueError:
            print("Palun sisenda kehtiv täisarv")

        i=float(input("Sisenda kui plju aega: "))
        arv=float(input("Sisenda kui palju euro te panite: "))
        if i>0 and arv>0:
            protsent=arv*0,03
     else :
        print("Viga: ")
