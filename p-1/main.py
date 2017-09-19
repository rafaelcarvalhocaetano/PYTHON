from builtins import print

print("parametro")
a = 10
b = 20

if a > b:
    print("A > B")
else:
    print("B > A")

print(a + b)
print(" ",a," ",b)
print("O Valor de é : ",a + b)
print("O Valor de é : ", str(a + b))

num = 2.3
print("Concatenando decimal", num)
print(" concat %.2f" %num)
print(" Concat ",a," ", num)

nome = "Rafael "
print("Seu nome ", nome)
print(" nome %s "%nome)
print(" nome "+nome)

login = input("Login: ")
senha = input("Senha : ")

print("Usuário ", login, "Com senha ", senha)

