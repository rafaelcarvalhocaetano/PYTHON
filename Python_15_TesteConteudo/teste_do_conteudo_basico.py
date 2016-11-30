login = input("informe o seu nome")
senha = input("Informe sua senha")
if(login == "rafael" and senha == str("123456")):

    a = float(input("Informe um Número: "))
    b = float (input("Informe o segundo Número: "))
    div = a / b
    mod = a % b

    print("A divisão de ", a, "por ", b, "é: ", div)
    print("O modulo da divisão de ", a , "por ", b , "é: ", mod)

else:
    print("Erro de Sintase")
