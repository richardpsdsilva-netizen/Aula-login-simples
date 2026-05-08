# Importamos as ferramentas do SQLAlchemy para definir colunas e tipos de dados
from sqlalchemy import Column, Integer, String, create_engine

# sessionmaker cria uma "fábrica" de sessões; declarative_base é a classe pai para nossos modelos
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente definidas no arquivo .env (como a URL do banco)
load_dotenv()

# Criamos a classe Base. Todos os nossos modelos (tabelas) vão herdar dela para serem reconhecidos pelo SQLAlchemy
Base = declarative_base()

# Definimos a classe que representa a tabela "usuarios" no banco de dados
class Usuario(Base):
    __tablename__ = "usuarios"  # Nome exato da tabela que será criada no banco

    # Define a coluna ID como chave primária e auto-incremento (1, 2, 3...)
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Define a coluna email: máximo 150 caracteres, única no banco e obrigatória (não nula)
    email = Column(String(150), unique=True, nullable=False)
    
    # Define a coluna senha: texto de até 100 caracteres, também obrigatória
    senha = Column(String(100), nullable=False)

    nome = Column(String(100))

# Puxa a string de conexão (ex: postgresql://user:password@localhost/dbname) das variáveis de ambiente
DATABASE_URL = os.getenv("DATABASE_URL")

# O Engine é o "motor" que gerencia a comunicação real com o driver do banco de dados
engine = create_engine(DATABASE_URL)

# Configuramos o Session para que, quando chamado, ele utilize o nosso 'engine' configurado acima
Session = sessionmaker(bind=engine)

# Função de Dependência para o FastAPI
def get_db():
    """
    Cria uma nova sessão de banco de dados para cada requisição e garante 
    que ela seja fechada após o uso.
    """
    db = Session() # Abre a conexão/sessão
    try:
        yield db   # Entrega a sessão para a rota do FastAPI que a solicitou
    finally:
        db.close() # Fecha a conexão após a resposta ser enviada ao usuário (limpeza)