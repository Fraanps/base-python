# Utilizando o Input
# o retorno do input será sempre uma String

nome_filme = input("Digite o nome do filme: \n")
ano_lancamento = int(input("Digite o ano de lançamento do filme: \n")) # fazendo um casting
nota_filme = float(input("Digite a nota do filme: \n")) # fazendo um casting

# concatenando valores
print("Dados do Filme")
print("===============================")
# Opção 1
print("Nome do filme: ", nome_filme)
print("Ano de lançamento: ", ano_lancamento)
print("Nota do filme: ", nota_filme)

# Opção 2
print("NOME DO FILME: ", nome_filme, 
      "\nANO DE LANÇAMENTO: ", ano_lancamento, 
      "\nNOTA DO FILME: ", nota_filme)

# Opção 3
print(f"Nome do filme: {nome_filme} \n"
      f"Ano de lançamento: {ano_lancamento} \n"
      f"Nota do filme: {nota_filme}")



"""
    print(type(nome_filme))
    print(type(ano_lancamento))
    print(type(nota_filme))
"""
