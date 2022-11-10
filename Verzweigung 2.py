# code 1


eingabe = float(input("zahl zwischen 10 und 18: "))

if 10 < eingabe < 18:
    print("richtig die zahl ist zwischen 10 und 18")
else:
    print("falsch")

# code 2

eingabe = float(input("zahl zwischen 2 und 10 oder 20 und 28: "))
if 2 < eingabe < 10 or 20 < eingabe < 28:
    print("richtig die zahl ist zwischen 2 und 10 oder 20 und 28")
else:
    print("falsch")

# Bonus

eingabe = float(input("Umsatz angeben"))
if 25000 < eingabe < 50000:
    print("Sie erhalten 2% Bonus")
    Bonus1 = round((eingabe * 2 / 100), 2)
    print("Bonus: ", Bonus1)
    print("Neuer Umsatz: ", round((eingabe + Bonus1), 2))
elif 50000 < eingabe < 750000:
    print("Sie erhalten 3% Bonus")
    Bonus1 = round((eingabe * 3 / 100), 2)
    print("Bonus: ", Bonus1)
    print("Neuer Umsatz: ", round((eingabe + Bonus1), 2))
elif 75000 < eingabe < 100000:
    print("Sie erhalten 4% Bonus")
    Bonus1 = round((eingabe * 4 / 100), 2)
    print("Bonus: ", Bonus1)
    print("Neuer Umsatz: ", round((eingabe + Bonus1), 2))
elif eingabe > 100000:
    print("Sie erhalten 5% Bonus")
    Bonus1 = round((eingabe * 5 / 100), 2)
    print("Bonus: ", Bonus1)
    print("Neuer Umsatz: ", round((eingabe + Bonus1), 2))
else:
    print("Sie erhalten Keinen Bonus")
    print("")
