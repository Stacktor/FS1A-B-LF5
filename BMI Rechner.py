h=float(input("gebe höhe in cm an: "))
w=float(input("gebe gewicht in Kg an: "))
geschlecht=(input("geben sie ihr geschlecht an (weiblich/mänlich)")) 
BMI=w/(h*h)
print("Der berechnete BMI liegt bei:  ",BMI)
print("ihr normalgewicht liegt bei:  ",h-100)
print("dein idealgewicht wäre bei:  ",(h-100)*(-0.1)+(h-100)) 
if(BMI>0):
    if(geschlecht == "weiblich" or "Weiblich"):
        if(BMI<19):
            print("du bist untergewichtig")
        elif(BMI>=19):
            print("du bist normalgewichtig")
        elif(BMI>=25):
            print("du bist übergewichtig")
        elif(BMI>=40):
            print("du bist adipös")
        else: 
            print("du bist stark adipös")
    else:
        if(BMI<=16):
            print("du bist sehr untergewichtig")
        elif(BMI<=18.5):
            print("du bist leicht untergewichtig")
        elif(BMI<=25):
            print("kratuliere du hast ein gesundes gewicht")
        elif(BMI<=30):
            print("du bist leicht übergewichtig")
        else: 
            print("du bist sehr übergewichtig")
else:
    print("gebe richtige werte an")
