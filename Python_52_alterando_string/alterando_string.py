#EXEMPLO 1
s = 'Alterando String'
for item in s:
    print(item)

#EXEMPLO 2
print()
sa = 'alterando string'
indice = 0
while (indice < len(sa)):
    print(indice," - ", s[indice])
    indice += 1

#EXEMPLO 3
sas = 'alterando a string'
for k,v in enumerate("alterando a string"):
    print(k,v)