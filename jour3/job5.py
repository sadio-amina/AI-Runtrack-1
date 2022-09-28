import re
import matplotlib.pyplot as plt

from collections import Counter

f = open ("data.txt", "r")
file = f.read()
f.close()
pattern = re.findall("[a-zA-Z]", file)

occurence = Counter(pattern)
occurence= dict(occurence)
print(occurence)

values= []
#Récupérer les valeurs des clés

for value in occurence.values():
    values.append(value)
#print(values)
for key, value in occurence.items():
    occurence_pourc = (occurence[key] / sum(values) ) * 100
    #print(occurence_pourc)





   

    


    

    

        
    


