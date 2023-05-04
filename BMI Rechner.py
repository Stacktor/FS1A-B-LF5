hcm=float(input("gebe höhe in cm an: "))
hm = hcm*0.01
w=float(input("gebe gewicht in Kg an: "))
geschlecht=(input("geben sie ihr geschlecht an (weiblich/mänlich)")) 
BMI=w/(hm*hm)
print("Der berechnete BMI liegt bei:  ",BMI)
print("ihr normalgewicht liegt bei:  ",hcm-100)
print("dein idealgewicht wäre bei:  ",(hcm-100)*(-0.1)+(hcm-100)) 
if(BMI>0):
    if(geschlecht == "weiblich" or "Weiblich"):
        if(BMI<19):
            print("du bist untergewichtig")
        elif(BMI<=19):
            print("du bist normalgewichtig")
        elif(BMI<=25):
            print("du bist übergewichtig")
        elif(BMI<=40):
            print("du bist adipös")
        else: 
            print("du bist stark adipös")
    else:
        if(BMI<=20):
            print("du bist sehr untergewichtig")
        elif(BMI<=25):
            print("du bist normalgewichtig")
        elif(BMI<=30):
            print("du bist übergewichtig")
        elif(BMI<=40):
            print("du bist adipös")
        else: 
            print("du bist stark adipös")
else:
    print("gebe richtige werte an")
