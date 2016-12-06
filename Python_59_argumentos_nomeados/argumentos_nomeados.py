def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
          .format(nome, sobrenome, idade, sexo))

dados_pessoais("rafael", "Carvalho", 30, True)
dados_pessoais(nome="Rafael", sobrenome="Carvalho", idade=30, sexo="Masculino")