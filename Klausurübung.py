# Input
monatsgehalt = float(input("Geben Sie Ihr Monatsgehalt ein: "))
kinder = float(input("Geben Sie die Anzahl ihrer Kinder ein: "))
dauerbetrieb = float(input("Arbeitsangehörigkeit im Betrieb (in Jahren): "))

# Berechnung
if dauerbetrieb < 10:
    fehltage = float(input("Geben Sie die Anzahl der fehlenden Tage ein: "))

if dauerbetrieb > 3:
    if dauerbetrieb < 10:
        if fehltage > 20:
            bonus = monatsgehalt * 0.1
        else:
            bonus = monatsgehalt * 0.15
    else:
        bonus = monatsgehalt
else:
    if fehltage <= 2:
        bonus = monatsgehalt * 0.01
    else:
        bonus = 0

bonus = bonus + kinder * 50
print("Der Bonus beträgt: ", bonus)

