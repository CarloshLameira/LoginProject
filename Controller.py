from Model import User
import rsa
from Dal import DalUser
import re
from hashlib import sha256


def check(email):
        '''ESSA FUNCAO VERIFICA SE UMA STRING ESTA NO FORMATO DE UM EMAIL

        Keywords arguments:
                email -- String (default None)
        
        Return: Boolean
        '''
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{3,}\b'
        if(re.fullmatch(regex, email)):
                return True
 
        else:
                False
         

class UserController:
        
        @classmethod
        def cadastrar(cls,name, email, password):
                ''' ESSE METODO TESTA SE OS VALORES DE NOME/EMAIL/SENHA SAO VALIDOS

                Keywords arguments:
                name -- String (default None)
                email -- String (default None)
                password -- String (default None)
                
                Return:
                String
                '''       
                x = DalUser.find(email)
                for i in x:
                        if i.user_name:
                                return 'Email ja cadastrado'  

                if name!='':
                        if check(email):
                                       
                                        if len(password)>=8:
                                                if re.search("[A-Z]", password):
                                                        if re.search("[0-9]", password):
                                                                if re.search("[_@$!?/|\#%&]", password):
                                                                        hashpassword = sha256(password.encode()).hexdigest()
                                                                        user = User(user_name=name, user_email=email, user_pass=hashpassword)
                                                                        DalUser.cadastrar(user)
                                                                        return 'Usuario Cadastrado'
                                                                else:
                                                                        return 'Senha deve possuir pelo menos um caracter especial'
                                                        else:
                                                                return 'Senha deve possuir pelo menos 1 numero'
                                                else:
                                                        return 'Senha deve possuir pelo menos 1 letra maiuscula'
                                        else:
                                                return 'Senha deve possuir pelo menos 8 caracteres'
                        else:
                                 return 'Email invalido'
                        
       
        @classmethod
        def login(cls, email, password):
                '''ESSE METODO AUTENTICA O USUARIO
                Keywords arguments:
                email -- String (default None)
                password -- String (default None)
                
                Return: String
                '''
                x = DalUser.find(email)
                hashpass = sha256(password.encode()).hexdigest()
                for i in x:
                        if i.user_pass == hashpass:
                                return 'Logado com sucesso'
                        else:
                                return 'Senha invalida'

                

