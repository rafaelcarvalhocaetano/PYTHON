arquivo = float(input("Informe o tamanho do arquivo em MB para DOWNLOAD : "))
speed = float(input("Informe a em Mbps : "))

convVelocidade = arquivo * 1.000
vel = speed * 1.024
divVel = convVelocidade / vel

tempo = divVel / 60
print(tempo)



