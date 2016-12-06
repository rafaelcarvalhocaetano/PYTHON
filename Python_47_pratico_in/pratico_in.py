"""""
a = 10
b = 25
c = 66

x = int(input("Digite um número: "))

if(x == a) or (x == b) or (x == c):
    print("Está contido")
else:
    print("Não está contido")

print("===utilizando Operadores IN")

r = 10
y = 25
t = 66

l = int(input("Digite um número: "))

if(l in [r,y,t]):
    print("ESTÁ contido")
else:
    print("NÃO está contido")
"""
cores = ['azul', 'amarelo', 'red', 'green', 'black', 'branco']
while True:
    valor = input("Digite o nome de uma cor ou 0 para sair: ")

    if(valor == '0'):
        break
    if valor in cores:
        print("A cor ", valor, "Esta cor está contida")
        print()
    else:
        print("Não está contida")