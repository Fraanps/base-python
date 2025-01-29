import sqlite3

# conectando no banco de dados
conn = sqlite3.connect('titulo.db')
cursor = conn.cursor()

# Inserindo dados
cursor.execute(
    """
        INSERT INTO filmes (nome, ano, nota)
        VALUES('Top Gun Maverick', 2022, 9.0)
    """   
)

conn.commit()
conn.close()

print("Dados inseridos")
