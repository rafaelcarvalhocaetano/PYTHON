sexo = input("Informe seu SEXO F ou M ")
altura = float(input("Informe sua ALTURA para Calcularmos seu PESO IDEAL "))

homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7


if sexo == "F" or sexo == "f":
    print("Seu PESO IDEAL é : {:.2f}".format(homem))
else:
    if sexo == "M" or sexo == "m":
        print("Seu peso IDEAL é : {:.2ff} ".format(mulher))
    else:
        if (sexo != "M" or sexo != "m" or sexo != "F" or sexo != "f"):
            print("Opção Invalida")
