#erstell Zahlenraten

import random
import time

print("Zahlenraten")
print("Ich denke mir eine Zahl zwischen 1 und 100 aus.")
print("Du musst sie erraten.")
print("Ich sage dir, ob die Zahl zu hoch oder zu niedrig ist.")
print("Wenn du die Zahl erraten hast, ist das Spiel vorbei.")
print("")
print("Drücke die Eingabetaste, um zu beginnen.")
input()

# Zufallszahl zwischen 1 und 100 erzeugen
Zahl = random.randint(1, 100)
versuche = 0

# Schleife, die solange läuft, bis die Zahl erraten wurde
while True:
    # Versuchszahl abfragen
    print("Welche Zahl denkst du?")
    versuch = input()
    versuch = int(versuch)

    # Versuchszahl mit der Zufallszahl vergleichen
    versuche = versuche + 1
    if versuch < Zahl:
        # Zahl ist zu niedrig
        print("Deine Zahl ist zu niedrig.")
    elif versuch > Zahl:
        # Zahl ist zu hoch
        print("Deine Zahl ist zu hoch.")
    else:
        # Zahl wurde erraten
        break

# Ausgabe, wie viele Versuche gebraucht wurden
print("Du hast die Zahl in " + str(versuche) + " Versuchen erraten.")
time.sleep(5)