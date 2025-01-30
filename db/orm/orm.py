from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo=True)
Base = declarative_base()


class Filme(Base):
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)


Base.metadata.create_all(engine)

# inserindo dados
def adiciona_filme(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = Filme(nome = nome, ano = ano, nota = nota)
    session.add(filme)
    session.commit()
    session.close()
    
# adiciona_filme("Ferrari", 2023, 8.0)
# adiciona_filme("O processo Goldman", 2023, 9.0)

# Atualizar dados 
def atualiza_filme(id, nome = None, ano = None, nota = None ):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    filme = session.query(Filme).filter_by(id = id).first()
    if filme: 
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        session.commit()
    session.close()
    
# atualiza_filme(1, None, None, 9.0 )
# atualiza_filme(2, "Anselm - O som do Tempo", 2022, 7.0 )

# Exclui dados
def exclui_filme(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id = id).first()
    if filme:
        session.delete(filme)
    session.commit()
    session.close()
    
exclui_filme(4)