import psycopg2

# conectando no banco de dados
conn = psycopg2.connect(
    database='db_games',
    user='postgres',
    password='postgres123',
    host='localhost',
    port='5432'
)
