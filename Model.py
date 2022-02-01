from sqlalchemy import Column, Integer, String,BLOB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
        '''DEFINE A CLASSE/TABELA USER
        '''
        __tablename__ = 'User'
        user_id = Column(Integer, primary_key=True)
        user_name = Column(String(500))
        user_email = Column(String(35))
        user_pass = Column(BLOB())

