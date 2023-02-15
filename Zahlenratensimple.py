from random import*
Gewinnzahl=randint(1 ,20)
Spiel = False
while(Spiel==False):
    Auswahlzahl=int(input("Raten Sie eine Zahl [1-20]: "))
    if (Auswahlzahl==Gewinnzahl):
        Spiel=True
    else:
        print ("Leider falsch!")
print ("Sie haben die Zahl erraten!")

