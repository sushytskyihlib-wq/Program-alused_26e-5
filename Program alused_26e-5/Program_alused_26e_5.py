print("Hello, \nWorld!")
print("tere Tulemast\t!")
print("Õpin",1,".kursusel") #sep=" " valikimisi on tühik
print("Õpin",1,".kursusel",sep="!")
#Parametrid sep ja end
print()#see on tühi rida
print("2026", "10", "01", sep="-")
print("Sama ", end="")#end="" Tähendab et reavahetust ei ole end="\n"
print("rida")
#Muutujad
nimi="Pyton"#str ehk sõne
kursus=1
print("Tere,",nimi)
print("Õpin",kursus,".kursusel",sep="!")
#input() funktsioon 
nimi=input("Siseta oma nimi: ")#Program küsib ja ootab kasutaja vastus
kursus=int(input("Sisesta kursuse number: "))#teisendab sõne arvuks
print("Tere,",nimi)
print("Õpin",kursus,".kursusel",sep="!")
print("jargmisel aastal õpin ",kursus+1,".kursusel")#kusus+1 tähendab et kurs+1
print("Liitmine")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"+",b,"=",a+b)

print("Liitmine")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"**",b,"=",a**b)

print("Liitmine")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"*",b,"=",a*b)

print("jagamine")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"/",b,"=",round(a/b,2))

print("Liitmine")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"//",b,"=",a//b)

print("jagamisjääk")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"%",b,"=",a%b)

nimi = "Mari"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")

a=float(input("arv 1: "))
tehe=input("Tehe: ")
b=float(input("arv 2: "))
print(f"{a} {tehe} {b} = {eval(f'{a} {tehe} {b}')}")
