from conexao_pg import conn

cursor_obj = conn.cursor()

sql = """
    UPDATE games
    SET nome = %s 
    WHERE ID = %s
"""

cursor_obj.execute(sql, ("Fifa 23", 3))

conn.commit()
print("Dados atualizados com sucesso!")
conn.close()

