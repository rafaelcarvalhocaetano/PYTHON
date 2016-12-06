lista = ['aaa', 'bbb', 'ccc', 'ddd', 'eee',]
print(lista[0])
lista.append('fff')
print(lista)

#inseri elementos na listas informando seu index
lista.insert(1, 'aa')
print(lista)

print(lista[2])

#exclui todos os elementos da lista
lista.clear()
print(lista)

lista = ['aaa', 'bbb', 'ccc', 'ddd', 'eee',]
print(lista)

#exclui os elementos selecionados da lista
lista.pop()
print(lista)
lista.pop()
print(lista)
lista.pop(0)
print(lista)

lista = ['aaa', 'bbb', 'ccc', 'ddd', 'eee',]
#deletando elementos da lista por index

del(lista[2:4])
print(lista)

lista = ['aaa', 'bbb', 'ccc', 'ddd', 'eee',]

#deletando elementos de dois em dois
del(lista[::2])
print(lista)
