###Job19
W = int (input("entrez widht :"))
H = int( input ("Entrez height :"))

def Draw_rectangle():
    filled = "|"+"-"*W+"|"
    empty = "|"+" "*W+"|"
    print(filled)
    for i in range(H):
        print(empty)
    print(filled)

Draw_rectangle()