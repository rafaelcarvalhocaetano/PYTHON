def fuc():
    return 1, 2

# a,b = fuc()
# t = (10, 20)
# a,b = t
a, b = fuc()

print(a)
print(b)

def potencia(x):
    quadrado = x **2
    cubo = x **3

    return quadrado, cubo

q,c=potencia(10)
print(q)
print(c)