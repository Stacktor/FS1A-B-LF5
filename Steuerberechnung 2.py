



eingabe = float(input("Jahresgehalt eingeben: "))
familienstand: str = input("Familienstand eingeben: ")

if eingabe > 75000 and familienstand == "ledig":
    print("sie zahlen 30% Steuer")
    Steuer1 = round((eingabe * 0.30), 2)
    print("Steuer")
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))

if eingabe > 75000 and familienstand == "Verheiratet":
    print("sie zahlen 26% Steuer")
    Steuer1 = round((eingabe * 0.26), 2)
    print("Steuer")
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))

elif 48000 < eingabe < 75000 and familienstand == "ledig":
    print("Sie zahlen 20% Steuer")
    Steuer1 = round((eingabe * 0.20), 2)
    print("Steuer: ", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))

elif 48000 < eingabe < 75000 and familienstand == "verheiratet":
    print("Sie zahlen 16% Steuer")
    Steuer1 = round((eingabe * 0.20), 2)
    print("Steuer: ", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))

elif 48000 > eingabe and familienstand == "ledig":
    print("Sie Zahlen 10% Steuern")
    Steuer1 = round((eingabe * 0.10), 2)
    print("Steuer; ", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))

elif 48000 > eingabe and familienstand == "verheiratet":
    print("Sie Zahlen 6% Steuern")
    Steuer1 = round((eingabe * 0.06), 2)
    print("Steuer; ", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))

else:




















elif 48000 > eingabe:
    print("Sie Zahlen 10% Steuern")
    Steuer1 = round((eingabe * 0.10), 2)
    print("Steuer; ", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))



