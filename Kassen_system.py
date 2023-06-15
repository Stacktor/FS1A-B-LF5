x=1
ticker=1
Artikelanzahl = []
artikelpreis = []
while (x==1):
    Anzahl=float(input("Anzahl des artikels :"))
    Artikelanzahl.append(Anzahl)
    Preis=float(input("Kosten des artikels : "))
    artikelpreis.append(Preis)
    y = input("weitere käufe? (j/n)")
    if (y=="n"):
        x=0
    else:
        ticker = ticker+1
for i in range (0,ticker,1):
    print (Artikelanzahl[i],"x",artikelpreis[i],"Euro =",Artikelanzahl[i]*artikelpreis[i],"Euro" )

print(Artikelanzahl(sum),"x", artikelpreis(sum),"Euro =",Artikelanzahl(sum)*artikelpreis(sum), "Euro")