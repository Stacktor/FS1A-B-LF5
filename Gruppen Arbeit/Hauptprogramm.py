jahr = int(input("Prüfungsjahr angeben: "))
pj = pruefeJahr(jahr)
if pj == 0:
    exit(0)
else:
    datum = int(input("Genaues Datum angeben: "))
    pd = pruefeDatum(datum)
if pd == 0:
    print("Eingegebenes Datum ist ungültig")
    exit(0)
else:
    gh1 =  int(input("gh1 angeben"))
    gh2 =  int(input("gh2 angeben"))
    wiso = int(input("wiso angeben"))
    eN = ermittleNote(gh1,gh2,wiso)


kN = kalkulatorNote(eN)
aus = ausgabe(eN, datum, jahr, gh1, gh2, wiso)
