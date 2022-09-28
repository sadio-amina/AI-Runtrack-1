import re
f = open ("data.txt", "r")
file = f.read()
f.close()
pattern = re.findall("[a-zA-Z]+", file)



    
    
