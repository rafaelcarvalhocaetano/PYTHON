#numero = int (input("DIgite um número: "))
numero = input("Digite um número: ")
numero = int(numero)

numero2 = input("Digite outro número: ")
numero2 = int(numero2)

if(numero == numero2):
    print("O número %d é igual a %d. " %(numero, numero2))
if(numero != numero2):
    print("O número %d é diferente de %d. " %(numero, numero2))
if(numero < numero2):
    print("O número %d é menor que %d" %(numero, numero2))
if(numero > numero2):
    print("O número %d é menor que %d "%(numero, numero2))
if(numero >= numero2):
    print("O número %d é menor ou igual a %d " %(numero, numero2))
if(numero <= numero2):
    print("O número %d é menor ou igual a %d" %(numero, numero2))