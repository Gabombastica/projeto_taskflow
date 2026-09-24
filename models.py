# Importar bibliotecas
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Base de dados - endereço
engine = create_engine('mysql+pysql://root:senaisp@localhost:3306/taskflow')

# Configurar sessão
db_session = sessionmaker(bind=engine)

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True) # Poderia ser id_pessoa
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    senha_hash = Column(String(20), nullable=False)
    papel = Column(String(100), default='usuario', nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Pessoa {self.nome}'

