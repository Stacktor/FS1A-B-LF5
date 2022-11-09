import tkinter as tk
from tkinter import ttk
import os




menu = tk.Tk()
menu.title("Projekte")
menu.geometry("400x400")

# Create a Tkinter variable
tkvar = tk.StringVar(menu)








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


#Spritpreis
'''
Spritpreis = float(input("Bitte geben Sie den Spritpreis ein: "))
Spritmenge = float(input("Bitte geben Sie die Spritmenge ein: "))
Spritbetrag = round((Spritpreis * Spritmenge),2)
print("Spritbetrag: ",Spritbetrag)
'''