from math import *


while True:
     print("Vali ülesanne 1,2,3,4,5,6,7,8,9,10,11")
     valik=input("Sisenda arv(1-11): ")
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
     elif valik=='6':
        i=float(input("Sisenda kui plju aega: "))
        arv=float(input("Sisenda kui palju euro te panite: "))
        if i>0 and arv>0:
            print(f"{arv*(1.03)**i}, summa on aastat") # 6 on tehtud iseseisevalt
     elif valik=='7':
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
     elif valik=='8':
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
     elif valik=='9':
            vastus=""
            for i in range(10):
                try:
                    arv=int(input(f"{i + 1}. arv: "))
                    if arv<0:
                        arv=arv*-1
                    vastus+=f"{arv}, "
                except ValueError:
                    print("palun sisesta arv")
                print("arvud olid", vastus) #ülesanne 9 iseseisev töö moodles number 21
     elif valik=='10':
         arv=["0","1","2","3","4","5","6","7","8","9","10"]
         for i in range(10):
            print(f"{i+1}")
            print(arv)# ülesanne 10 moodles on ülesannne 15 on kirjutatud iseseisvalt
     elif valik=='11':
         try:
             arv=float(input("Sisenda kui palju düüimin on olemas: "))
             arv>0
             tabel=arv*2.5
             print(f"{arv} düimid on {tabel} santimetrid")
         except ValueError:
             print("Ei saa veiksem kui null")# ülesanne 11 moodles on ülesanne 8 on kirjutatud iseseisvalt
     else:
        print("Viga: kirjuta numbrid 1-10")

