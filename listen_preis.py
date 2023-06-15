temperatures = []  # Leeres Array zur Speicherung der Temperaturen

# Temperaturen der letzten 7 Tage abfragen
for i in range(7):
    temperature = float(input(f"Geben Sie die maximale Temperatur am Tag {i+1} ein: "))
    temperatures.append(temperature)

# Durchschnittliche Höchsttemperatur berechnen
average_temperature = sum(temperatures) / len(temperatures)

print("Die durchschnittliche Höchsttemperatur der letzten Woche beträgt:", average_temperature)