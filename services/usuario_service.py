from repositories.usuario_repository import UsuarioRepository


class UsuarioService:

    @staticmethod
    def cadastrar(nome, email, senha):

        return UsuarioRepository.cadastrar(
            nome,
            email,
            senha
        )

    @staticmethod
    def autenticar(email, senha):

        return UsuarioRepository.autenticar(
            email,
            senha
        )