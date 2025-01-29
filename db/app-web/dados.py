import sqlite3
import pandas as pd

# conectando no banco de dados
def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# insere dados
def insere_dados(nome, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    
    cursor.execute(
    """
        INSERT INTO filmes (nome, ano, nota)
        VALUES(?, ?, ?)
    """, (nome, ano, nota)   
    )
    conexao.commit()
    conexao.close()
    
    
# listagem de dados
def obter_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall() # retorna uma lista de tuplas
    
    #colunas = [desc[0] for desc in cursor.description] # obtem o nome das colunas
    cursor.close()
    
    # converte os dados pra um DataFrame do pandas
    #df = pd.DataFrame(dados, columns=colunas)

    return dados

    
