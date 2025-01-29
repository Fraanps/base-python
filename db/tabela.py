import sqlite3

# conectando no banco de dados
conn = sqlite3.connect('titulo.db')

# criando o cursor (permite que realize operações dentro do banco de dados)
cursor = conn.cursor()

# criando a tabela
cursor.execute(
    """
       CREATE TABLE filmes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
       );    
    """
)

# fechando conexão
conn.close()
print("Tabela foi criada")
