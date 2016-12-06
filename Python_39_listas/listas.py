"""
lista_num = [100,200,300,400]
lista_indice = [0,1,2,3]
for item in lista_indice:
    lista_num[item] += 1000
    print(lista_num)
"""
#------outra forma de interar a função range---
lista_num = [100, 200, 300, 400]
lista_indice = range(0, 4)
for item in lista_indice:
    lista_num[item] += 1000
    print(lista_num)
#------outra formula----------
print("----------função range---------------")
lista_num = [100, 200, 300, 400]
for item in range(0, 4):
    lista_num[item] += 1000
    print(lista_num)
#------outra formula----------
print("---------Função range----------------")
lista_num = [100, 200, 300, 400, 500]
for item in range(len(lista_num)):
    lista_num[item] += 1000
    print(lista_num)
#------outra formula----------
print("---------Função Enumerate----------------")
lista_num = [10, 20, 30, 40, 50, 60]
for index, item in enumerate(lista_num):
    lista_num[index][item] += 100
    print(lista_num)