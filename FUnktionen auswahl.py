länge = int(input("länge des quadrates"))
höhe = int(input("höhe"))+1
def linie():
    print("linie:---------------------------------------------------------------------------------")
def quadrat():
    length = "o"
    for i in range(länge,0,-1):
        length = length+"o"
    for i in range (höhe,0,-1):
        print(length)
        print("\n")
def leiter():
    print("leiter:\n## ##\n#####\n## ##\n#####\n## ##")
linie()
quadrat()
leiter()
