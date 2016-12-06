print("====in - not in=====")
#verificando condições
print(2 in (1,2,3,4,5))
print()
print(6 not in (1,2,3,4,5))
print()
print(6 in (1,2,3,4,5))
print()
print(1 in range(1,6)) #verificando com range
print()
print(1 in range(2,6))
print()
print(list(range(1,9)))
print()
x = range(1,6)
if 3 in x:
    print("Contido")
else:
    print("Não contido")