import re

def RunFile(filename):
    f = open(filename, "r")
    file = f.read()
    file = file.split(" ")
    file = str(file)
    word = re.findall("[a-zA-Z]+", file)
    f.close()
    print(len(word))
    

RunFile("data.txt")




