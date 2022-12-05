# Input
monatsgehalt = float(input("Geben Sie Ihr Monatsgehalt in Euro ein: "))
kinder = float(input("Geben Sie die Anzahl ihrer Kinder ein: "))
dauerbetrieb = float(input("Arbeitsangehörigkeit im Betrieb in Jahren: "))

if dauerbetrieb < 10:
    fehltage = float(input("Geben sie fehltage an"))
# Berechnung
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
        bonus = monatsgehalt * 0.1
    else:
        bonus = 0

bonus = bonus + kinder * 50
print("Der Bonus beträgt: ", bonus)

