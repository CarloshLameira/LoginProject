from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model import User

def DefineSession():
        '''FUNCAO QUE CRIA UMA SECAO E RETORNA LEA MESMO

        Return:
        h -- List of objects     
        '''
        USUARIO = 'root'
        SENHA = '123321'
        HOST = 'localhost'
        BANCO = 'projetocadastro'
        PORT = '3306'

        CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

        engine = create_engine(CONN, echo=False)
        Session = sessionmaker(bind=engine) 
        return  Session()
       
class DalUser():
        @classmethod
        def cadastrar(cls, user:User):
                '''DEFINE UM METODO QUE IRA CADASTRAR OS USUARIOS

                Keywords arguments:
                user -- Object

                Return: None
                '''
                session=DefineSession()
                session.add(user)
                session.commit()
                
        @classmethod
        def find(cls,mail):
                '''METODO QUE IRA ENCONTRAR O CADASTRO DESEJADO

                Keywords arguments:
                mail -- String (default None)
                
                Return: List
                '''
                session=DefineSession()
                x = session.query(User).all()
                x = session.query(User).filter(User.user_email == mail)                     
                return x

#x = User(user_name='zezin', user_email='ze@gmail.com', user_pass='123321')


#DalUser.find('ze@gmail.com')

