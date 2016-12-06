lista = ['rafael', 'rose', 'vitor', 'heitor']
print(lista)
len(lista)
print(len(lista))#verificando a quantidade dos elementos
lista.insert(5, 'pai') # inseri o elemento na posição solicitado dentro do elemento
print(lista)
print(len(lista)) #conta a qtd de elementos da lista
lista.append('mae') #o append inseri sempre no ultimo elemento da lista
print(lista)
lista.append('rafael')
lista.append('rafael')
print(lista)

print("===Função count====")
print(lista.count('rafael'))
print(lista.count('rose'))

print("====função index")
#verifica o index que encontra-se o elemento 'rose'
lista.index('rose')
print(lista.index('rose'))
print(lista.index('rafael'))