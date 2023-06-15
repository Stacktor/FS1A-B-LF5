# Abfrage des Nutzers Höchsttemperatur

mo = float(input("Temperatur vom Montag?"))
di = float(input("Temperatur vom Dienstag?"))
mi = float(input("Temperatur vom Mittwoch?"))
do = float(input("Temperatur vom Donnerstag?"))
fr = float(input("Temperatur vom Freitag?"))
sa = float(input("Temperatur vom Samstag?"))
so = float(input("Temperatur vom Sonntag?"))


# Liste mit den Wochentagen

Wochentage = ["montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag"]

# Berechnen Mittlere Temperatur

mittel = ((mo+di+mi+do+fr+sa+so)/7)
print(mittel)

