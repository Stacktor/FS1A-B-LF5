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
        # Prüfen, ob die neue Position innerhalb der Grenzen liegt
        if x + 1 <= 20:
            x += 1 # Nach Osten gehen bedeutet x um 1 erhöhen
        else:
            print("Sie können nicht weiter nach Osten gehen.")
    elif eingabe == "n":
        # Prüfen, ob die neue Position innerhalb der Grenzen liegt
        if y + 1 <= 20:
            y += 1 # Nach Norden gehen bedeutet y um 1 erhöhen
        else:
            print("Sie können nicht weiter nach Norden gehen.")
    elif eingabe == "w":
        # Prüfen, ob die neue Position innerhalb der Grenzen liegt
        if x - 1 >= 0:
            x -= 1 # Nach Westen gehen bedeutet x um 1 verringern
        else:
            print("Sie können nicht weiter nach Westen gehen.")
    elif eingabe == "s":
        # Prüfen, ob die neue Position innerhalb der Grenzen liegt
        if y - 1 >= 0:
            y -= 1 # Nach Süden gehen bedeutet y um 1 verringern
        else:
            print("Sie können nicht weiter nach Süden gehen.")
    elif eingabe == "b":
        break # Das Programm beenden
    else:
        print("Ungültige Eingabe. Bitte geben Sie o, n, w, s oder b ein.")