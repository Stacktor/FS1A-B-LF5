Tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

print ("A")
print  (Tage[0])

print ("B")
print (Tage[6])

print("C")
for i in range (0,7,1):
    print (Tage[i])

print("D)")
for i in range (7,0,-1):
    print (Tage[i-1])


x = len (Tage)
print(x)

Tage.pop (1)
Tage.pop (5)
print (Tage)




