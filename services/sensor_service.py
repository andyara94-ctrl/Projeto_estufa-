from repositories.sensor_repository import SensorRepository
from models.sensor import Sensor


class SensorService:

    @staticmethod
    def cadastrar(
        sessao,
        tipo,
        descricao,
        unidade_medida
    ):

        if not sessao.usuario_autenticado():

            print("Faça login primeiro.")
            return

        usuario = sessao.obter_usuario()

        sensor = Sensor(
            tipo=tipo,
            descricao=descricao,
            unidade_medida=unidade_medida,
            id_usuario_cadastro=usuario.idusuario
        )

        return SensorRepository.cadastrar(sensor)

    @staticmethod
    def listar_por_usuario(id_usuario):

        return SensorRepository.listar_por_usuario(
            id_usuario
        )