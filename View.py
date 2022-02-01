from Controller import UserController
while True:
        menu=input('Entre com 1 para cadastrar e 2 para logar\n')
        if menu == '1':
                name = input('Entre com o seu nome: ')
                mail = input('Entre com o seu email: ')
                password = input('Entre com a sua senha: ')
                print('\n')
                out = UserController.cadastrar(name, mail, password)
                print(out)
                print('\n')

                while out != 'Usuario Cadastrado':
                        if UserController.cadastrar(name, mail, password) == 'Email invalido' or UserController.cadastrar(name, mail, password) == 'Email ja cadastrado' :
                                mail = input('Entre com o seu email: ')
                                password = input('Entre com a sua senha: ')
                                print('\n')
                                out = UserController.cadastrar(name, mail, password)
                                print(out)
                                print('\n')
                        else:
                                password = input('Entre com a sua senha: ')
                                print('\n')
                                out = UserController.cadastrar(name, mail, password)
                                print(out) 
                                print('\n')

        if menu == '2':
                mail = input('Entre com o seu email: ')
                password = input('Entre com a sua senha: ') 
                print('\n')
                aux = UserController.login(mail, password)
                if aux != None:
                        if aux == 'Logado com sucesso : )':
                                print(aux)
                                print('\n')
                        else:
                                print(aux)
                                print('\n')
                else:
                        print('Email nao cadastrado')
                print('\n')                            

