# Startpunkt ist x=10, y=10
x = 10
y = 10

# Eine Schleife, die die Benutzereingaben liest und verarbeitet
while True:
    # Die aktuelle Position ausgeben
    print(f"Sie sind bei {x} | {y}.")

    # Die Benutzereingabe lesen
    eingabe = input("Wohin wollen Sie gehen? (o/n/w/s/b): ")

    # Die Eingabe überprüfen und die Position entsprechend ändern
    if eingabe == "o":
        x += 1 # Nach Osten gehen bedeutet x um 1 erhöhen
    elif eingabe == "n":
        y += 1 # Nach Norden gehen bedeutet y um 1 erhöhen
    elif eingabe == "w":
        x -= 1 # Nach Westen gehen bedeutet x um 1 verringern
    elif eingabe == "s":
        y -= 1 # Nach Süden gehen bedeutet y um 1 verringern
    elif eingabe == "b":
        break # Das Programm beenden
    else:
        print("Ungültige Eingabe. Bitte geben Sie o, n, w, s oder b ein.")