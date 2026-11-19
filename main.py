from database.conexao import conectar
 
conexao = conectar()
 
cursor = conexao.cursor()
 
cursor.execute("SHOW TABLES")
 
for tabela in cursor.fetchall():
    print(tabela)
 
cursor.close()
conexao.close()

import bcrypt
from database.conexao import Conexao
from mysql.connector import IntegrityError

# ==========================================
# CLASSE QUE REPRESENTA UM USUÁRIO
# ==========================================

class Usuario:

    def __init__(self, nome, email, senha, idusuario=None):
        self.idusuario = idusuario
        self.nome = nome
        self.email = email
        self.senha = senha

    # Cadastrar usuário no banco
    @staticmethod
    def cadastrar(nome, email, senha):

        conexao = None
        cursor = None

        try:
            conexao = Conexao.conectar()

            if conexao is None:
                return False

            cursor = conexao.cursor()

            # Criptografar senha
            senha_hash = bcrypt.hashpw(
                senha.encode("utf-8"),
                bcrypt.gensalt()
            )

            sql = """
                INSERT INTO usuario (nome, email, senha)
                VALUES (%s, %s, %s)
            """

            valores = (nome, email, senha_hash.decode("utf-8"))

            cursor.execute(sql, valores)
            conexao.commit()

            print("\nUsuário cadastrado com sucesso!")
            print(f"ID gerado pelo MySQL: {cursor.lastrowid}")

            return True

        except IntegrityError:
            print("\nEsse usuário ou e-mail já está cadastrado!")
            return False

        except Exception as erro:
            if conexao:
                conexao.rollback()

            print(f"\nErro ao cadastrar: {erro}")
            return False

        finally:
            if cursor:
                cursor.close()

            if conexao and conexao.is_connected():
                conexao.close()

    # Buscar usuário e validar senha
    @staticmethod
    def autenticar(nome, senha):

        conexao = None
        cursor = None

        try:
            conexao = Conexao.conectar()

            if conexao is None:
                return None

            cursor = conexao.cursor(dictionary=True)

            sql = """
                SELECT idusuario, nome, email, senha
                FROM usuario
                WHERE nome = %s
            """

            cursor.execute(sql, (nome,))
            resultado = cursor.fetchone()

            if resultado:

                senha_hash = resultado["senha"].encode("utf-8")

                if bcrypt.checkpw(
                    senha.encode("utf-8"),
                    senha_hash
                ):

                    return Usuario(
                        resultado["nome"],
                        resultado["email"],
                        senha,
                        resultado["idusuario"]
                    )

            return None

        except Exception as erro:
            print(f"\nErro no login: {erro}")
            return None

        finally:
            if cursor:
                cursor.close()

            if conexao and conexao.is_connected():
                conexao.close()


# ==========================================
# CLASSE RESPONSÁVEL PELA SESSÃO
# ==========================================

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

    # Verificar autenticação
    def usuario_autenticado(self):

        return self.usuario_logado is not None

    # Recuperar usuário conectado
    def obter_usuario(self):

        return self.usuario_logado

    # Encerrar sessão
    def encerrar_sessao(self):

        if self.usuario_logado is not None:

            print(f"\nAté logo, {self.usuario_logado.nome}!")

            self.usuario_logado = None

            print("Logout realizado com sucesso!")

        else:
            print("\nNenhum usuário está logado.")


# ==========================================
# CRIANDO A SESSÃO
# ==========================================
sessao = Sessao()

# ==========================================
# MENU PRINCIPAL
# ==========================================
while True:

    print("\n========== MENU ==========")
    print("1 - Cadastrar usuário")
    print("2 - Login")
    print("3 - Ver usuário logado")
    print("4 - Logout")
    print("5 - Sair")
    print("==========================")

    opcao = input("Escolha uma opção: ")

    # OPÇÃO 1 - CADASTRO
    if opcao == "1":

        nome = input("\nDigite o nome de usuário: ").strip()
        email = input("Digite o e-mail: ").strip()
        senha = input("Digite a senha: ")

        if not nome or not email or not senha:
            print("\nPreencha todos os campos!")

        else:
            Usuario.cadastrar(nome, email, senha)

    # OPÇÃO 2 - LOGIN
    elif opcao == "2":

        if sessao.usuario_autenticado():
            print("\nJá existe um usuário logado!")

        else:

            nome = input("\nUsuário: ").strip()
            senha = input("Senha: ")

            usuario = Usuario.autenticar(nome, senha)

            if usuario is not None:
                sessao.iniciar_sessao(usuario)

            else:
                print("\nUsuário ou senha incorretos!")

    # OPÇÃO 3 - VER USUÁRIO LOGADO
    elif opcao == "3":

        if sessao.usuario_autenticado():

            usuario = sessao.obter_usuario()

            print("\n====== USUÁRIO LOGADO ======")
            print(f"ID: {usuario.idusuario}")
            print(f"Nome: {usuario.nome}")
            print(f"E-mail: {usuario.email}")
            print("Status: Autenticado")
            print("============================")

        else:
            print("\nNenhum usuário está logado.")

    # OPÇÃO 4 - LOGOUT
    elif opcao == "4":

        sessao.encerrar_sessao()

    # OPÇÃO 5 - SAIR
    elif opcao == "5":

        print("\nPrograma encerrado!")
        break

    # OPÇÃO INVÁLIDA
    else:

        print("\nOpção inválida! Tente novamente.")
