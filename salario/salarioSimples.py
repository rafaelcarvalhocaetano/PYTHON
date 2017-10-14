sal = float(input("Informe o VALOR da HORA trabalhada : "))
diasTrabalhados = float(input("Informe a quantidade de DIAS trabalhado no MÊS : "))

horaTrabalhada = diasTrabalhados * 8
soma = horaTrabalhada * sal

print("Seu SALÁRIO neste MÊS foi R$ {:.2f} ".format(soma))

