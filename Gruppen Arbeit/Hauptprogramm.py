def ausgeben(gesamtNote,Datum,Jahr,xGh1,xGh2,xWiso):
    if(gesamtNote >= 50):
        print("Prüfung vom:\t\t\t\t\t",DT,DM,".",Jahr)
        print("Gesamtnote der schriftlichen Leistungen:\t",gesamtNote,"%")
        print("Einzelleistungen")
        print("\tGH1\t\t",xGh1,"%")
        print("\tGH2\t\t",xGh2,"%")
        print("\tWISO\t\t",xWiso,"%")
        print("Herzlichen Glückwunsch zum Bestehen des ersten Prüfungsteils!")
        print("Damit sind Sie zur mündlichen Prüfung zugelassen!")
    else:
        print("Prüfung vom:\t\t\t\t\t",DT, DM)
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
def pruefeDatum(DT,DM,pj):
    if (DM<=12 and DM>0 ):
        if(DM == 1 or DM ==3 or DM ==5 or DM ==7 or DM ==8 or DM ==10 or DM ==12):
            if (DT<=31 and DT>0):
                Datum=0
            else :
                Datum=1
        if(DM == 4 or DM ==6 or DM ==9 or DM ==11):
            if (DT<=30 and DT>0):
                Datum=0
            else :
                Datum=1
        elif(DM == 2 and pj == 1):    
            if(DT<29 and DT>0):
                Datum=0
            else :
                Datum=1
        elif(DM == 2 and pj == 2):    
            if(DT<=29 and DT>0):
                Datum=0
            else :
                Datum=1
    else :
        Datum=1
    return Datum
def kalkulatorNote(ermittleNote):
    vNote = int(ermittleNote)
    
    def PraedikatMdl(vProzentMdl):
        
        if vProzentMdl >= 92:
            return "sehr gut"
        elif vProzentMdl >= 81:
            return "gut"
        elif vProzentMdl >= 67:
            return "befriedigend"
        elif vProzentMdl >= 50:
            return "ausreichend"
        elif vProzentMdl >= 30:
            return "mangelhaft"
        else:
            return "ungenügend"
        
        
    def PraedikatSch(vProzentSch):
        
        if vProzentSch >= 92:
            return "sehr gut"
        elif vProzentSch >= 81:
            return "gut"
        elif vProzentSch >= 67:
            return "befriedigend"
        elif vProzentSch >= 50:
            return "ausreichend"
        elif vProzentSch >= 30:
            return "mangelhaft"
        else:
            return "ungenügend"
        
        
    def PraedikatGes(vProzentGes):
        
        if vProzentGes >= 92:
            return "sehr gut"
        elif vProzentGes >= 81:
            return "gut"
        elif vProzentGes >= 67:
            return "befriedigend"
        elif vProzentGes >= 50:
            return "ausreichend"
        elif vProzentGes >= 30:
            return "mangelhaft"
        else:
            return "ungenügend"
    
    def AusgabePosi(vMuendlich,vNote,vGesamtpruefnote):
        
        vProzentSch = vNote
        print("Gesamtnote der schriftlichen Leistungen:",vNote," % (",PraedikatSch(vProzentSch),")")
        vProzentMdl = vMuendlich
        print("Note der mündlichen Prüfung:",vMuendlich," % (",PraedikatMdl(vProzentMdl),")")
        vProzentGes = vGesamtpruefnote
        print("Gesamtprüfungsnote:",vGesamtpruefnote," % (",PraedikatGes(vProzentGes),")")
        print("Mit diesem Ergebnis hätten Sie die Prüfung mit ",PraedikatGes(vProzentGes)," bestanden!!!")
    
    def AusgabeNegi(vMuendlich,vNote,vGesamtpruefnote):
        
        vProzentSch = vNote
        print("Gesamtnote der schriftlichen Leistungen:",vNote," % (",PraedikatSch(vProzentSch),")")
        vProzentMdl = vMuendlich
        print("Note der mündlichen Prüfung:",vMuendlich," % (",PraedikatMdl(vProzentMdl),")")
        vProzentGes = vGesamtpruefnote
        print("Gesamtprüfungsnote:",vGesamtpruefnote," % (",PraedikatGes(vProzentGes),")")
        print("Mit diesem Ergebnis hätten Sie die Prüfung leider nicht bestanden!!!")
    
    vSicherheit = 1
    
    while vSicherheit == 1:
        vSicherheit = 0
            
        vNochmal = int(input("Möchten Sie Ihre Gesamtprüfnote berechnen? (Ja = 1; Nein = 2: ): "))
        
        while vNochmal == 1:
            vMuendlich = int(input("Bitte geben Sie Ihre Mündliche Note in % ein: "))
            vGesamtpruefnote = vMuendlich + vNote
            vGesamtpruefnote = vGesamtpruefnote / 2
            
            if vMuendlich < 30:
                AusgabeNegi(vMuendlich,vNote,vGesamtpruefnote)
                vNochmal = int(input("Möchten SieIhre Gesamtnote nochmal berechnen? (Ja = 1; Nein = 2: )"))
                
            elif vGesamtpruefnote < 50:
                AusgabeNegi(vMuendlich,vNote,vGesamtpruefnote)
                vNochmal = int(input("Möchten SieIhre Gesamtnote nochmal berechnen? (Ja = 1; Nein = 2: )"))
                
            else:
                AusgabePosi(vMuendlich,vNote,vGesamtpruefnote)
                vNochmal = int(input("Möchten SieIhre Gesamtnote nochmal berechnen? (Ja = 1; Nein = 2: )"))
            
            
        else:
            if vNochmal == 2:
                print("")
            
            else:
                print("Ungültige Eingabe!!!\n")
                vSicherheit = 1
            
    else:
        print("")






Datum=1
jahr = int(input("Prüfungsjahr angeben: "))
pj = pruefeJahr(jahr)
if pj == 0:
    exit(0)
else:
    DT = int(input("Genauen Tag angeben: "))
    DM = int(input("Genauen Monat angeben"))
    pd = pruefeDatum(DT, DM, pj)
if pd == 1:
    print("Eingegebenes Datum ist ungültig")
    exit(0)
else:
    gh1 =  int(input("gh1 angeben"))
    gh2 =  int(input("gh2 angeben"))
    wiso = int(input("wiso angeben"))
    eN = ermittleNote(gh1,gh2,wiso)


kN = kalkulatorNote(eN)
aus = ausgeben(eN, Datum, jahr, gh1, gh2, wiso)