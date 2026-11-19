import bcrypt

from database.conexao import Conexao
from models.usuario import Usuario


class UsuarioRepository:

    @staticmethod
    def cadastrar(nome, email, senha):

        conexao = Conexao.conectar()

        cursor = conexao.cursor()

        senha_hash = bcrypt.hashpw(
            senha.encode("utf-8"),
            bcrypt.gensalt()
        )

        sql = """
            INSERT INTO usuario
            (nome,email,senha)
            VALUES (%s,%s,%s)
        """

        cursor.execute(
            sql,
            (
                nome,
                email,
                senha_hash.decode()
            )
        )

        conexao.commit()

    @staticmethod
    def autenticar(email, senha):

        conexao = Conexao.conectar()

        cursor = conexao.cursor(
            dictionary=True,
            buffered=True
        )

        sql = """
            SELECT *
            FROM usuario
            WHERE email=%s
            LIMIT 1
        """

        cursor.execute(sql, (email,))

        resultado = cursor.fetchone()

        if resultado:

            senha_hash = resultado["senha"].encode()

            if bcrypt.checkpw(
                senha.encode(),
                senha_hash
            ):

                return Usuario(
                    idusuario=resultado["idusuario"],
                    nome=resultado["nome"],
                    email=resultado["email"],
                    senha=None
                )

        return None
