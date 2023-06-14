
Wochentage = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]
print(Wochentage) #a)

print(Wochentage[0]) #b)

print(Wochentage[6]) #c)

for i in range (0 ,7 ,1):
    print(Wochentage[i])    #d)

for i in range (7,0,-1):
    print(Wochentage[i-1])    #e)

Zahl = len(Wochentage)
print(Zahl)                  #f)

Wochentage.pop (1)
Wochentage.pop (-1)   
print(Wochentage)           #g)





