# Classe que representa um usuário
class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha


# Classe responsável pela sessão
class Sessao:
    def __init__(self):
        self.usuario_logado = None

    # Iniciar sessão
    def iniciar_sessao(self, usuario):
        if self.usuario_logado is not None:
            print("\nJá existe um usuário logado!")
            return

        self.usuario_logado = usuario
        print(f"\nBem-vindo(a), {usuario.nome}!")

    # Verificar se existe usuário logado
    def usuario_autenticado(self):
        return self.usuario_logado is not None

    # Recuperar usuário conectado
    def obter_usuario(self):
        return self.usuario_logado

    # Encerrar sessão (Logout)
    def encerrar_sessao(self):
        if self.usuario_logado is not None:
            print(f"\nUsuário {self.usuario_logado.nome} desconectado com sucesso!")
            self.usuario_logado = None
            print("Logout realizado!")
        else:
            print("\nNenhum usuário está logado!")


# Lista de usuários cadastrados
usuarios = []

# Criando a sessão
sessao = Sessao()


# Menu principal
while True:
    print("\n========== MENU ==========")
    print("1 - Cadastrar usuário")
    print("2 - Login")
    print("3 - Ver usuário logado")
    print("4 - Logout")
    print("5 - Sair")
    print("==========================")

    print("\n")
    opcao = input("Escolha uma opção: ") 
    # OPÇÃO 1 - Cadastro
    if opcao == "1":
        nome = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        # Verifica se o usuário já existe
        if any(u.nome == nome for u in usuarios):
            print("\nEsse usuário já está cadastrado!")
        else:
            novo_usuario = Usuario(nome, senha)
            usuarios.append(novo_usuario)
            print("\nUsuário cadastrado com sucesso!")

    # OPÇÃO 2 - Login
    elif opcao == "2":

        if sessao.usuario_autenticado():
            print("\nJá existe um usuário logado!")
        else:
            nome = input("Usuário: ")
            senha = input("Senha: ")

            encontrado = False

            for usuario in usuarios:
                if usuario.nome == nome and usuario.senha == senha:
                    sessao.iniciar_sessao(usuario)
                    encontrado = True
                    break

            if not encontrado:
                print("\nUsuário ou senha incorretos!")

    # OPÇÃO 3 - Ver usuário logado
    elif opcao == "3":

        if sessao.usuario_autenticado():
            usuario = sessao.obter_usuario()
            print("\n========== USUÁRIO LOGADO ==========")
            print(f"Nome: {usuario.nome}")
            print("Status: Autenticado")
            print("====================================")
        else:
            print("\nNenhum usuário está logado!")

    # OPÇÃO 4 - Logout
    elif opcao == "4":
        sessao.encerrar_sessao()

    # OPÇÃO 5 - Sair
    elif opcao == "5":
        print("\nPrograma encerrado!")
        break

    # Opção inválida
    else:
        print("\nOpção inválida! Tente novamente.")
