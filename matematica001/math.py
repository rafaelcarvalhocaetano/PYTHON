num1 = int(input("Informe o 1° número INTEIRO "))
num2 = int(input("Informe o 2° número INTEIRO "))
num3 = float(input("Informe o ÚNICO número REAL "))

dobroPrimeiro = num1 * num1
divSegundo = num2 / 2
calc1 = dobroPrimeiro + divSegundo
##---------------------------------------
somaTriploPrimeiro = (num1 * num1) * num1
calc2 = somaTriploPrimeiro + num3
##---------------------------------------
print("O produto do dobro do primeiro foi {} com metade do segundo foi {} deu {} ".format(dobroPrimeiro, divSegundo, calc1))
print("A soma do triplo do primeiro deu {} com o terceiro que foi {} deu : {} ".format(somaTriploPrimeiro, num3, calc2))

