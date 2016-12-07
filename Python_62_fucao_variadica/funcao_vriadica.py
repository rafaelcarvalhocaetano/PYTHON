def lista_de_argumentos(*lista):
    print(lista)

lista_de_argumentos(1,2,3,4,5,6,7)

lista_de_argumentos("um", "dois", "tres", "quatro")


def lista_args_assoc(**dicionario):
    print(dicionario)


lista_args_assoc(a=1, b=2, c=3)

def args(*argss, **user):
    print(argss)
    print(user)

args(1,2,3,4,5,um=1,dois=2)