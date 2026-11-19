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

    @staticmethod
    def listar_por_usuario(id_usuario):

        conexao = Conexao.conectar()

        cursor = conexao.cursor(
            dictionary=True
        )

        sql = """
            SELECT
                idsensor,
                id_usuario_cadastro,
                tipo,
                descricao,
                unidade_medida
            FROM sensor
            WHERE id_usuario_cadastro = %s
        """

        cursor.execute(
            sql,
            (id_usuario,)
        )

        return cursor.fetchall()