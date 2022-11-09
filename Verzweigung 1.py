import tkinter as tk
from tkinter import ttk
import os



"""
menu = tk.Tk()
menu.title("Projekte")
menu.geometry("400x400")






# Bestellbetrag

Bestellbetrag = float(input("Bitte geben Sie den Bestellbetrag ein: "))

if Bestellbetrag > 500.00:
    print("Sie erhalten 5% Rabatt")
    Rabatt1 = round((Bestellbetrag * 5/100 ),2)
    print("Rabatt: ",Rabatt1)
    print("Neuer Bestellbetrag: ",round((Bestellbetrag - Rabatt1),2))
else:
    print("Sie erhalten 3% Rabatt")
    Rabatt1 = round((Bestellbetrag * 3/100 ),2)
    print("Rabatt: ",Rabatt1)
    print("Neuer Bestellbetrag: ",round((Bestellbetrag - Rabatt1),2))

#Temparatur

Temp1 = float(input("Enter the first number: "))

if Temp1 > 30:
    print("Heute ist ein Schöner Tag")

"""
#Spritpreis

Spritgetankt = float(input("Wie viel Liter Sprit haben Sie getankt? "))
Spritart = input("Bitte geben Sie die Spritart ein: ")

Diesel = 1.28
Super = 1.36

#Rechnung Diesel

Netto = round((Diesel * Spritgetankt),2)
mws = round((Diesel * Spritgetankt) * 0.19 ,2)
Brutto = (round((Diesel * Spritgetankt) + mws,2))

#Rechnung Super

Netto1 = round((Super * Spritgetankt),2)
mws1 = round((Super * Spritgetankt) * 0.19 ,2)
Brutto1 = (round((Super * Spritgetankt) + mws1,2))

if Spritart == "Diesel":
  print(Brutto,"€")
  print(Netto,"€")
  print(mws,"€")

elif Spritart == "Super":
    print(Brutto1,"€")
    print(Netto1,"€")
    print(mws1,"€")


else:
    print("Falsche Eingabe")
