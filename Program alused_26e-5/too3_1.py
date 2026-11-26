from math import e


while True:
     print("Vali ülesanne 1,2,3,4,5,6,7")
     valik=input("Sisenda arv(1-7): ")
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
     elif valik=='6':
         pos_kogus=0
         neg_kogus=0
         null_kogus=0
         while True:
             try:
                 N=int(input("Sisenda N>0 arv: "))
                 if N>0: break
             except ValueError:
                 print ("palun sisenda positivne täisarv")
                 continue
         for i in range(N):
             while True:
                 try:
                     arv=float(input(f"{i+1}, arv: "))
                     break
                 except ValueError:
                      print("Sisenda kehtiv arv: ")
             if arv<0:
                 print("Negativne arv")
                 neg_kogus+=1
             elif arv>0:
                 print("Positiivne arv")
                 pos_kogus+=1
             else:
                 print("Null")
                 null_kogus+=1
         print(f"Negatiivne arvude kogus: {neg_kogus}")
         print(f"Positiivne arvude kogus: {pos_kogus}")
         print(f"Null {null_kogus} korda")
     elif valik=='7':
         while True:
             try:
                 A=int(input("Sisenda A arv: "))
                 B=int(input("Sisenda B arv: "))
                 K=int(input("Sisenda K arv: "))
                 break
             except ValueError:
                 print("palun sisenda positiivne täisarv")
             if A>B:
                 print(" A peab olema võrand või väiksem kui B")
                 A,B=B,A
         print(f"Arvud vahemikus [{A} ,{B}], mis on {K}-ga jaguvad: ")
         for i in range(A,B+1):
             if i % K == 0:
                 print(i)
     else :
        print("Viga: ")
