import re


file_open = open("domains.xml", "r")
file = file_open.read()
file= file.split("\n")
file = str(file)
name_domaine = re.findall("\.[a-z]+", file)
print(len(name_domaine))









