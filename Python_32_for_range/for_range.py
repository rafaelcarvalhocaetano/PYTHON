print(list(range(10)))
print(list(range(1, 15)))
print(list(range(0, 100, 10)))
print(list(range(0, 100, 3)))
print(list(range(100, 0, -3)))
print(list(range(-100, 0, 3)))

"""  range( 100, 0, 1)
    100 == início
    0 == termino
    1 == intervalo da lista

"""

for i in range(10):
    print(i)

for i in range(-10, 0 , 1):
    print(i)

for i in list(range(0, 10, 1)):
    print(i)