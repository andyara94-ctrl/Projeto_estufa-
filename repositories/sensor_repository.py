from database.conexao import Conexao

class SensorRepository:

    @staticmethod
    def cadastrar(sensor):

        conexao = Conexao.conectar()

        cursor = conexao.cursor()

        sql = """
            INSERT INTO sensor
            (
                tipo,
                descricao,
                unidade_medida,
                status,
                id_usuario_cadastro
            )
            VALUES
            (%s,%s,%s,%s,%s)
        """

        cursor.execute(
            sql,
            (
                sensor.tipo,
                sensor.descricao,
                sensor.unidade_medida,
                sensor.status,
                sensor.id_usuario_cadastro
            )
        )

        conexao.commit()

        sensor.idsensor = cursor.lastrowid

        return sensor