nota1 = float(input("Informe a 1° nota : "))
nota2 = float(input("Informe a 2° nota : "))
nota3 = float(input("Informe a 3° nota : "))
nota4 = float(input("Informe a 4° nota : "))

media = (nota1+nota2+nota3+nota4) / 4

print("A média do Bimestre foi : {:.1f} ".format(media))

if media >= 10.0:
    print("Parabéns sua média foi {:.1f}, você passou !!! ".format(media))
if (media >= 6.0 and media <= 9.0):
    print("Parabéns sua média foi {:.1f}, passou raspando !!! ".format(media))
if media <= 5.0:
    print("Reprovado sua média foi {:.1f} ".format(media))


