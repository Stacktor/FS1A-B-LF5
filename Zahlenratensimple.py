from random import*
wiederhol=True
anykey=True
while(wiederhol==True):
    Spiel = False
    Gewinnzahl=randint(1 ,20)
    while(Spiel==False):
        Auswahlzahl=int(input("Raten Sie eine Zahl [1-20]: "))
        if (Auswahlzahl==Gewinnzahl):
            Spiel=True
            print ("Sie haben die Zahl erraten!")
        else:
            print ("Leider falsch!")
            if(Gewinnzahl>Auswahlzahl):
                print("ihre zahl ist zu klein")
            else:
                print("ihre zahl ist zu gross")
    if (input("press Enter to continue")):
        wiederhol=True        
