#Steuer 3
JahresgehaltBrutto = float(input("Ihr Jahres gehalt -Brutto- : "))
Kinder = float(input("Die Anzahl ihrer Kinder : "))
Familienstand = input("Geben sie ihren Familienstand an (Ledig)(Verheiratet) : ")
Kinderkürzung = Kinder*5000
print("Kürzung ",Kinderkürzung)
eingabe = JahresgehaltBrutto - Kinderkürzung
if eingabe > 75000 and Familienstand=="Ledig" or "ledig":
    print("sie zahlen 30% Steuer")
    Steuer1 = round((eingabe * 0.30), 2)
    print("Steuer; -", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))
elif 48000 < eingabe < 75000 and Familienstand=="Ledig" or "ledig":
    print("Sie zahlen 20% Steuer")
    Steuer1 = round((eingabe * 0.20), 2)
    print("Steuer: -", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))
elif 48000 > eingabe and Familienstand=="Ledig" or "ledig":
    print("Sie Zahlen 10% Steuern")
    Steuer1 = round((eingabe * 0.10), 2)
    print("Steuer; -", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))
elif eingabe > 75000 and Familienstand == "Verheiratet" or "verheiratet" :
    print("sie zahlen 26% Steuer")
    Steuer1 = round((eingabe * 0.26), 2)
    print("Steuer: -", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))
elif 48000 < eingabe < 75000 and  Familienstand=="Verheiratet" or "verheiratet":
    print("Sie zahlen 16% Steuer")
    Steuer1 = round((eingabe * 0.16), 2)
    print("Steuer: -", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))
elif 48000 > eingabe and Familienstand=="Verheiratet" or "verheiratet":
    print("Sie Zahlen 6% Steuern")
    Steuer1 = round((eingabe * 0.06), 2)
    print("Steuer; -", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))