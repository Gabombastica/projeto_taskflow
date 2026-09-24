# Importar bibliotecas
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey, func
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, scoped_session

# Base de dados - endereço
engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/taskflow')

# Configurar sessão
db_session = scoped_session (sessionmaker(bind=engine))

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True) # Poderia ser id_pessoa
    nome_pessoa = Column(String(50), nullable=False)
    email_pessoa = Column(String(50), nullable=False, unique=True)
    senha_pessoa = Column(String(20), nullable=False)
    papel = Column(String(100), default='usuario', nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Pessoa {self.nome_pessoa}, {self.email_pessoa}, {self.senha_pessoa}, {self.papel}, {self.criado_em}'


class Tarefa(Base):
    __tablename__ = 'tarefas'
    id = Column(Integer, primary_key=True)
    nome_tarefa = Column(String(50), nullable=False)
    descricao_tarefa = Column(String(100), nullable=False)
    data_tarefa = Column(DateTime, nullable=False)
    prioridade_tarefa = Column(String(20), nullable=False)
    tipo_tarefa = Column(String(20), nullable=False)
    recurso_tarefa = Column(Integer, nullable=False)
    responsavel_tarefa = Column(String(50), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Tarefa {self.nome_tarefa}, {self.descricao_tarefa}, {self.data_tarefa}, {self.prioridade_tarefa}, {self.tipo_tarefa}, {self.recurso_tarefa}, {self.responsavel_tarefa}, {self.criado_em}'

class Tipo(Base):
    __tablename__ = 'tipos'
    id = Column(Integer, primary_key=True)
    nome_tipo = Column(String(50), nullable=False)
    descricao_atividade_tipo = Column(String(100), nullable=False)
    responsavel_tipo = Column(String(50), nullable=False)
    nome_atividade_tipo = Column(String(50), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Tipo {self.nome_tipo}, {self.descricao_atividade_tipo}, {self.responsavel_tipo}, {self.nome_atividade_tipo}, {self.criado_em}'

class Recurso(Base):
    __tablename__ = 'recursos'
    id = Column(Integer, primary_key=True)
    nome_recurso = Column(String(150), nullable=False)
    descricao_recurso = Column(String(100), nullable=False)
    responsavel_recurso = Column(String(50), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Recurso {self.nome_recurso}, {self.descricao_recurso}, {self.responsavel_recurso}, {self.criado_em}'



