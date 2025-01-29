import sqlite3

conn = sqlite3.connect('titulo.db')
cursor = conn.cursor()

# Atualizando dados
id = 2
cursor.execute(
    """
        UPDATE filmes SET nota = ?
        WHERE id = ?
    """,
    (8.5, id)
)

conn.commit()
conn.close()

print("Dados atualizados")