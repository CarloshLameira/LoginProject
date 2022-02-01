from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()#importa codigos de banco de dados que o sqlalchemy usa

class User(Base):
        '''DEFINE A CLASSE/TABELA USER
        '''
        __tablename__ = 'User'
        user_id = Column(Integer, primary_key=True)
        user_name = Column(String(60))
        user_email = Column(String(35))
        user_pass = Column(String(64))

