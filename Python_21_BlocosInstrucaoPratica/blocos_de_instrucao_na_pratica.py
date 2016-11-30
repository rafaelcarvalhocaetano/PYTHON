num = input("Digite um número")
num = int(num)

if(num > 10):
    print("O valor é maior que 10")
    if(num <= 15):
        print("O número é maior que 10 e menor que 15")
    else:
        if(num <= 50):
            print("O número é maior que 10 e menor que 50")
        else:
            print("O número é maior que 50")
else:
    if(num > 5):
        print("O número é menor que 10 e maior que 5")
        if(num == 7):
            print("O número é igual a 7")
    else:
        print("O valor é menor que 5")
