from Model import User
import rsa
from Dal import DalUser
from rsa.key import PrivateKey, PublicKey
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
        #Keypublic = PublicKey(8959256223667307440646239669639551691754589213337493349186493242210461639848394061610513627742212005523399981863814891297358119440031491390825189564189331, 65537)    
        #KeyPrivate = PrivateKey(8959256223667307440646239669639551691754589213337493349186493242210461639848394061610513627742212005523399981863814891297358119440031491390825189564189331, 65537, 6081472639364997464097969359958269322053109781414036790391844887208364682617742026209852044088196436089392145563399114872145083288864215743920253430390769, 6869053162681910458482422563820092584873136287379889387845611634777872352647051437, 1304292747702262807886140354689988773602858015335320497101886396934502463)
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
                                                                        encpassword = sha256(password.encode())
                                                                        user = User(user_name=name, user_email=email, user_pass=encpassword)
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
                for i in x:
                        decMessage = rsa.decrypt(i.user_pass, cls.KeyPrivate).decode()
                        if decMessage == password:
                                return 'Logado com sucesso'
                        else:
                                return 'Senha invalida'

                

#print(UserController.login('ze@gmail.com', 'Ventilador10!'))
#print(UserController.cadastrar('ze', 'zezinnn@gmail.com', 'Ventilador10!'))