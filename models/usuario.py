class Usuario:

    def __init__(
        self,
        nome,
        email,
        senha,
        idusuario=None
    ):

        self.idusuario = idusuario
        self.nome = nome
        self.email = email
        self.senha = senha