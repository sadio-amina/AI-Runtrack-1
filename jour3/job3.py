import re

n = int(input("Veuillez saisir un nombre entier : "))
f = open("data.txt", "r")
file = f.read()
f.close()
words = re.findall("[a-zA-Z]+", file)

w=[]
for word in words:
    if len(word) == n :
        w.append(word)
print(len(w))





