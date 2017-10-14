area = float(input("Informe o tamanho em metros quadrados a serem pintados : "))
qtdTintaL = 18
valorLata18L = 80.00

qtdTintas = area / 3

print("----------------QUANTIDADE DE TINTAS---------------------")
if (qtdTintas <= qtdTintaL):
    qtdTintaL
    valorLata18L
    print("Quantidade de Tintas \t\t\t{}L".format(qtdTintaL))
    print("Valor a ser pago     \t\t\t{}L".format(valorLata18L))
else:
    if (qtdTintas > qtdTintaL and qtdTintas <= (qtdTintaL * 2) ):
        litros = qtdTintaL * 2
        valor = valorLata18L * litros
        print("Quantidade de Tintas \t\t\t{}L".format(qtdTintaL))
        print("Valor a ser pago     \t\t\t{}L".format(valorLata18L))

