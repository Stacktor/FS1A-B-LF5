def ausgeben(gesamtNote,Datum,Jahr,xGh1,xGh2,xWiso):
    if(gesamtNote >= 50):
        print("Prüfung vom:\t\t\t\t\t",Datum,".",Jahr)
        print("Gesamtnote der schriftlichen Leistungen:\t",gesamtNote,"%")
        print("Einzelleistungen")
        print("\tGH1\t\t",xGh1,"%")
        print("\tGH2\t\t",xGh2,"%")
        print("\tWISO\t\t",xWiso,"%")
        print("Herzlichen Glückwunsch zum Bestehen des ersten Prüfungsteils!")
        print("Damit sind Sie zur mündlichen Prüfung zugelassen!")
    else:
        print("Prüfung vom:\t\t\t\t\t",Datum)
        print("Gesamtnote der schriftlichen Leistungen:\t",gesamtNote,"%")
        print("Einzelleistungen")
        print("\tGH1\t\t",xGh1,"%")
        print("\tGH2\t\t",xGh2,"%")
        print("\tWISO\t\t",xWiso,"%")
        print("Es tut mir leid, Ihnen mitteilen zu müssen, dass Sie mit einem Prüfungsergebnis unter")
        print("50% nicht zur mündlichen Prüfung zugelassen sind.")
def ermittleNote(xGh1,xGh2,xWiso):
    
    # Variabeln
    fNotenZusammen = 0
    # Gewichtungen 
    fGh1Wicht  = 40
    fGh2Wicht  = 40
    fWisoWicht = 20

    if xGh1 < 30 or xGh2 < 30 or xWiso < 30 :
        return 0
    else :
        fNotenZusammen = xGh1 * fGh1Wicht 
        fNotenZusammen = fNotenZusammen + xGh2 * fGh2Wicht
        fNotenZusammen = fNotenZusammen + xWiso * fWisoWicht

        fNotenZusammen = fNotenZusammen / 100

        return round(fNotenZusammen,0)
def pruefeJahr(jahr):
    if jahr not in range(2019,2022):
        return 0
    else:
        if jahr % 4 == 0 and jahr % 100 != 0:
            return 2
        elif jahr % 4 == 0 and jahr % 100 == 0 and jahr % 400 == 0 :
            return 2
        else:
            return 1






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
aus = ausgeben(eN, datum, jahr, gh1, gh2, wiso)





