Aushilfskräfte= int(input("anzahl der aushilfskräfte"))
Wochenlohn = 25 
Wochenendlohn = 30 
Aushilfskraft_counter = 1 
Lohnkosten = 0 
for i in 0,Aushilfskräfte,1:
    Arbeitsstunden = int(input("Stunden"))
    wochenend = int(input("Wochenend Stunden?"))
    Arbeitsstunden = Arbeitsstunden - wochenend
    Arbeiterlohn = Arbeitsstunden*Wochenlohn+wochenend*Wochenendlohn
    Lohnkosten = Lohnkosten+Arbeiterlohn
    print(print("lohn des Mitarbeiters ",Aushilfskraft_counter," : ", Arbeiterlohn ))
    Aushilfskraft_counter = Aushilfskraft_counter +1
print(print("Lohnkosten", Lohnkosten))
