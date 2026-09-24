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
        return f'Pessoa {self.nome}, {self.email}, {self.senha_hash}, {self.papel}, {self.criado_em}'


class Tarefa(Base):
    __tablename__ = 'tarefas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(100), nullable=False)
    data = Column(DateTime, nullable=False)
    prioridade = Column(String(20), nullable=False)
    tipo = Column(String(20), nullable=False)
    recurso = Column(Integer, nullable=False)
    responsavel = Column(String(50), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Tarefa {self.nome}, {self.descricao}, {self.data}, {self.prioridade}, {self.tipo}, {self.recurso}, {self.responsavel}, {self.criado_em}'

class Tipo(Base):
    __tablename__ = 'tipos'
    id = Column(Integer, primary_key=True)
    tipo = Column(String(50), nullable=False)
    descricao = Column(String(100), nullable=False)
    responsavel = Column(String(50), nullable=False)
    atividade = Column(String(50), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Tipo {self.tipo}, {self.descricao}, {self.responsavel}, {self.atividade}, {self.criado_em}'

class Recurso(Base):
    __tablename__ = 'recursos'
    id = Column(Integer, primary_key=True)
    recurso = Column(String(150), nullable=False)
    descricao = Column(String(100), nullable=False)
    responsavel = Column(String(50), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Recurso {self.recurso}, {self.descricao}, {self.responsavel}, {self.criado_em}'



