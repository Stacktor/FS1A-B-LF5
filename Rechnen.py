import os
import time
# zahlen eingabe
zahl1= input( " Erste Zahl " )
zahl2 = input( " Zweite Zahl " )
# rechnen
select = input( " Wie Möchtest du Rechnen (+) (-) (*) (/) (//) (%) (-) " )
# ausgabe
if select == "+":
    print( " Ergebnis " , int( zahl1 ) + int( zahl2 ) )
elif select == "-":
    print( " Ergebnis " , int( zahl1 ) - int( zahl2 ) )
elif select == "*":
    print( " Ergebnis " , int( zahl1 ) * int( zahl2 ) )
elif select == "/":
    print( " Ergebnis " , int( zahl1 ) / int( zahl2 ) )
elif select == "//":
    print( " Ergebnis " , int( zahl1 ) // int( zahl2 ) )
    print( " Rest " , int( zahl1 ) % int( zahl2 ) )
elif select == "%":
    print( " Rest " , int( zahl1 ) % int( zahl2 ) )
#elif select == "P":
    #print( " Ergebnis"  ,zahl1 * zahl2  / (zahl1 + zahl2) )
#Nicht Funktionierend

else:
    print( " Fehler " )
    back = input( " Drücke Enter um zurück zu kommen " )
    os.system( " Rechnen.py " )


time.sleep( 2 )
# speichern
save = (input("Möchtest du die Rechnung speichern? (j/n) "))
if save == "j":
    file = open("Rechnung.txt", "w")
    file.write("""Ergebnis: %s""" % (int(zahl1) + int(zahl2)))
    file.close()
    print("Rechnung wurde gespeichert")
    time.sleep(3)
    os.system("Rechnung.txt")
else:
    print("Rechnung wurde nicht gespeichert")
    time.sleep(3)

loop = input("Möchtest du noch eine Rechnung machen? (j/n) ")
if loop == "j":
    open("Rechnen.py")
else:
    print("Programm wird beendet")
    time.sleep(5)
    exit(25)
