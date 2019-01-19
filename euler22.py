file = open("p022_names.txt", "r")
cont = file.read()
names = cont.split(",")
noms = [i.strip('"') for i in names]
noms.sort()
Answer = 0
indx = 1
for each in noms:
    total = 0
    btotal = 0
    name = list(each)
    for letters in name:
        total += (ord(letters)-64)
    btotal += total*indx
    Answer += btotal
    indx += 1
print(Answer)
file.close()