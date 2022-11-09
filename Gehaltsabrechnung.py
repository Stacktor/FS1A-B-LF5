import time
import os

Bruttogehalt = float(input("Bitte geben Sie das Bruttogehalt ein: "))
# Bruttogehalt
lohnsteuer = float(input("Bitte geben Sie die Lohnsteuer ein: "))
# Lohnsteuer



Kirchensteuer = round((lohnsteuer * 9/100 ),2)
solidaritätszuschlag = round((lohnsteuer * 5.5/100 ),2)
zeugs = round((Kirchensteuer + solidaritätszuschlag),2)
# Kirchensteuer und Solidaritätszuschlag


Rentenversicherung = round((Bruttogehalt * 18.6/100 )* 0.5 ,2)
krankenversicherung = round((Bruttogehalt * 14/100 )* 0.5 ,2)
arbeitslosenversicherung = round((Bruttogehalt * 2.4/100 )* 0.5 ,2)
pflegeversicherung = round((Bruttogehalt * 3.3/100 )* 0.5 ,2)
Sozialversicherung = round((Rentenversicherung + krankenversicherung + arbeitslosenversicherung + pflegeversicherung),2)
# Sozialversicherung

personalaufwand = round((Bruttogehalt + Sozialversicherung),2)

nettogehalt = round((Bruttogehalt - lohnsteuer - zeugs - Sozialversicherung),2)


print("Lohnsteuer:                              ",lohnsteuer)
print("kirchenssteuer:                          ",Kirchensteuer)
print("solidaritätszuschlag:                    ",solidaritätszuschlag)
print("AN-Anteil zur Sozialversicherung:        ",zeugs)
print("Rentenversicherung:                      ",Rentenversicherung)
print("Krankenversicherung:                     ",krankenversicherung)
print("Arbeitslosenversicherung:                ",arbeitslosenversicherung)
print("Pflegeversicherung:                      ",pflegeversicherung)
print("Sozialversicherung:                      ",Sozialversicherung)
print("netto:                                   ",nettogehalt)
print("Personalaufwand:                         ",personalaufwand)

# Berechnung

