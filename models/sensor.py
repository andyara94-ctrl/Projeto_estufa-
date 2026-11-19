class Sensor:

    def __init__(
        self,
        tipo,
        descricao,
        unidade_medida,
        idsensor=None,
        status=True,
        id_usuario_cadastro=None
    ):

        self.idsensor = idsensor
        self.tipo = tipo
        self.descricao = descricao
        self.unidade_medida = unidade_medida
        self.status = status
        self.id_usuario_cadastro = id_usuario_cadastro
