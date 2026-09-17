# Importar bibliotecas
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Base de dados - endereço
engine = create_engine('mysql+pysql://root:senaisp@localhost:3306/taskflow')

# Config sessão
local_session = sessionmaker(bind=engine)

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
