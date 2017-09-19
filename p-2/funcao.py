a = 1
b = 3

def soma(v1, v2):
    s = v1 + v2
    return s

def imprime(x):
    for i in range(x):
        print(i)

print("A soma de ",a,"+",b," é: ",soma(a, b))
imprime(5)

##tem que colocar o int para converter
v = int(input("n: "))
if(v % 2 == 0):
    print("par")
else:
    print("impar")

x = 0
while(x <= 10):
    print(x)
    x = x+1
else:
    print("erro")

for c in "rafael":
    print(c)

print(list(range(0,10, 1)))
print(list(range(10)))
print(list(range(0, 100, 10)))