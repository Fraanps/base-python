import sqlite3

conn = sqlite3.connect('titulo.db')
cursor = conn.cursor()

# Inserindo dados
dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall())