#Array
x=1
Artikelanzahl = []
Artikelpreis = []

#Eingabe

while (x==1):
    print("Bitte geben Sie den Preis des Artikel ein:")
    Artikelpreis.append(float(input()))
    print("Bitte geben Sie die Anzahl des Artikel ein:")
    Artikelanzahl.append(float(input()))
    abfrage = input("Wollen Sie noch einen Artikel eingeben? (1 = Ja, 0 = Nein)")
    if (abfrage == "0"):
        x=0
    

    

print (Artikelanzahl, Artikelpreis)