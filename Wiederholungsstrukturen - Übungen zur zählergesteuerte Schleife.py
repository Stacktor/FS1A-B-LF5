# Erstellen Sie eine leere Liste für die Matrix
matrix = []

# Schleife von 1 bis 10 für jede Zeile
for i in range(1, 11):
    # Erstellen Sie eine leere Liste für die Zeile
    row = []
    # Schleife von 1 bis 10 für jede Spalte
    for j in range(1, 11):
        # Berechnen Sie das Produkt von i und j und fügen Sie es der Zeile hinzu
        row.append(i * j)
    # Fügen Sie die Zeile der Matrix hinzu
    matrix.append(row)

# Schleife über jede Zeile in der Matrix
for row in matrix:
    # Konvertieren Sie jedes Element in der Zeile in einen String und trennen Sie sie mit Leerzeichen
    line = " ".join(str(x) for x in row)
    # Geben Sie die Zeile auf dem Bildschirm aus
    print(line)