tel = {}
tel = {}
tel = {
    1111222222: "rafael",
    2222333333: "rose",
    3333444444: "vitor",
    4444555555: "Heitor"
}
print(tel)
print(len(tel))
print(tel.keys()) #retorna a lista com os elementos
print(tel.values()) #retorna a lista com os valores
print(tel[1111222222])
print(tel.get(1111222222))
print(tel.popitem())
print(tel.popitem())

tel = {
    1111222222: "rafael",
    2222333333: "rose",
    3333444444: "vitor",
    4444555555: "Heitor"
}
print(1111222222 in tel)
tel2 = {
    99999:"teste1",
    22222: "teste2"
}
print(tel.update(tel2))
t = (10,10,10)
tel[t] = "rafael"
print(tel)