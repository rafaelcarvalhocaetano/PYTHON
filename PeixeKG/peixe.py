multa = 4.00
kgPermitido = 50.00
peso = float(input("Informe quantos kilos de peixe possui : "))
excesso = ""

if (peso > kgPermitido):
    valorMulta = peso - kgPermitido
    excesso = "Peso acima do permitido "
    print(excesso, "Quantidade de {}Kg a MAIS".format(valorMulta))
else:
    if (peso <= kgPermitido):
        excesso = "Liberado "
        qtd = peso - kgPermitido
        if(peso == kgPermitido):
            val = peso
            print("Peso = {}kg, {}".format(val, excesso))
        else:
            print("Peso = {}kg Permitido, {}".format(qtd, excesso))
