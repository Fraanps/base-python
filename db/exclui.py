import sqlite3

conn = sqlite3.connect('titulo.db')
cursor = conn.cursor()

# exclusão de dados
id = (2, 3)
cursor.execute(
    """
        DELETE FROM filmes WHERE ID in (?,?)
    """,
    (id)
)

conn.commit()
# conn.close

print("Dados excluídos com sucesso!")