import time
import os

print("Hallo, ich bin der Lebenslauf von Python")

name = (input("Wie ist dein Name? "))
strasse = (input("Wie ist deine Strasse? "))
plz = (input("Wie ist deine Postleitzahl? "))
ort = (input("Wie ist dein Wohnort? "))
geboren = (input("Wann bist du geboren? "))
hobbies = (input("Was sind deine Hobbies? "))

print ("""L E B E N S L A U F
--------------------
name: %s 
strasse: %s
plz: %s
ort: %s
geboren: %s
hobbies: %s""" % (name, strasse, plz, ort, geboren, hobbies))

time.sleep(5)

save = (input("Möchtest du den Lebenslauf speichern? (j/n) "))
if save == "j":
    file = open("Lebenslauf.txt", "w")
    file.write("""L E B E N S L A U F
--------------------
name: %s 
strasse: %s
plz: %s
ort: %s
geboren: %s
hobbies: %s""" % (name, strasse, plz, ort, geboren, hobbies))
    file.close()
    print("Lebenslauf wurde gespeichert")
    time.sleep(5)
    os.system("Lebenslauf.txt")
else:
    print("Lebenslauf wurde nicht gespeichert")
    time.sleep(5)

wait = input("Press enter to continue")
