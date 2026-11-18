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
        self.usuario_logado = usuario
        print(f"\nBem-vindo(a), {usuario.nome}!")

    # Verificar se existe usuário logado
    def usuario_autenticado(self):
        return self.usuario_logado is not None

    # Recuperar usuário conectado
    def obter_usuario(self):
        return self.usuario_logado

    # Encerrar sessão
    def encerrar_sessao(self):
        if self.usuario_logado:
            print(f"\nAté logo, {self.usuario_logado.nome}!")
            self.usuario_logado = None
        else:
            print("\nNenhum usuário está logado.")


# Lista para armazenar os usuários cadastrados
usuarios = []

# Criando a sessão
sessao = Sessao()

while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar usuário")
    print("2 - Login")
    print("3 - Ver usuário logado")
    print("4 - Logout")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # Cadastro
    if opcao == "1":
        nome = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        novo_usuario = Usuario(nome, senha)
        usuarios.append(novo_usuario)

        print("Usuário cadastrado com sucesso!")

    # Login
    elif opcao == "2":
        nome = input("Usuário: ")
        senha = input("Senha: ")

        encontrado = False

        for usuario in usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                sessao.iniciar_sessao(usuario)
                encontrado = True
                break

        if not encontrado:
            print("Usuário ou senha incorretos.")

    # Mostrar usuário logado
    elif opcao == "3":
        if sessao.usuario_autenticado():
            usuario = sessao.obter_usuario()
            print(f"Usuário logado: {usuario.nome}")
        else:
            print("Nenhum usuário está logado.")

    # Logout
    elif opcao == "4":
        sessao.encerrar_sessao()

    # Sair
    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")