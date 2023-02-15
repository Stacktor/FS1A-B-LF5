from random import*
Gewinnzahl=randint(1 ,20)
wiederhol=True
anykey=True
while(wiederhol==True):
    Spiel = False
    while(Spiel==False):
        Auswahlzahl=int(input("Raten Sie eine Zahl [1-20]: "))
        if (Auswahlzahl==Gewinnzahl):
            Spiel=True
            print ("Sie haben die Zahl erraten!")
        else:
            print ("Leider falsch!")
    if (input("press Enter to continue")):
        wiederhol=True

