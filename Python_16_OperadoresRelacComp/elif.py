idade = int(input("Informe sua idade: "))
if(idade <= 0):
    print("Sua idade não pode ser 0 ou igual 0 ")
    print("Sua idade é: ", idade)
elif(idade > 150):
    print("Sua idade não pode ser maior que ", idade)
    print("Sua idade é: ", idade)
elif(idade < 18):
    print("Você é menor de idade, pois tem ", idade)
    print(idade)
