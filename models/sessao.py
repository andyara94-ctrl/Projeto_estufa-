class Sessao:

    def __init__(self):
        self.usuario_logado = None

    def iniciar_sessao(self, usuario):

        self.usuario_logado = usuario

    def usuario_autenticado(self):

        return self.usuario_logado is not None

    def obter_usuario(self):

        return self.usuario_logado

    def encerrar_sessao(self):

        self.usuario_logado = None