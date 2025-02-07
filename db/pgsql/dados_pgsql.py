from conexao_pg import conn

cursor_obj = conn.cursor()

games = [
    # ('Star Wars Survicor', 2023, 9.0),
    # ('Luigi Mansion 3', 2019, 9.0),
    ('The Last of us II', 2020, 9.5),
    ('Spider Man 2', 2023, 10.0),
]

for game in games:
    cursor_obj.execute(
        """
            INSERT INTO games(nome, ano, pontos)
            VALUES (%s, %s, %s)
        """, game
    )

conn.commit()
print("Dados inseridos com sucesso")
conn.close()


