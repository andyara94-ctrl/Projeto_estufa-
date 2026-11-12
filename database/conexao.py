import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
 
# Carrega as variáveis do arquivo .env
load_dotenv()
 
class Conexao:
 
    @staticmethod
    def conectar():
        # Traz as configurações do banco que estão no .env
        host = os.getenv("DB_HOST", "127.0.0.1")
        porta = os.getenv("DB_PORT", "3306")
        usuario = os.getenv("DB_USER")
        senha = os.getenv("DB_PASSWORD", "")
        banco = os.getenv("DB_NAME")
 
        # Verifica se as configurações obrigatórias existem
        if not all([host, porta, usuario, banco]):
            raise ValueError("Verifique as configurações obrigatórias no arquivo .env")
 
        try:
            conexao = mysql.connector.connect(
                host=host,
                port=int(porta),
                user=usuario,
                password=senha,
                database=banco
            )
            return conexao
        except Error as erro:
            raise ConnectionError(f"Erro ao conectar com o MySQL: {erro}")
 
# Função auxiliar para permitir 'from database.conexao import conectar' no main.py
def conectar():
    return Conexao.conectar()
 
# Só executa o teste se você rodar o arquivo conexao.py diretamente
if __name__ == "__main__":
    conexao = None
    try:
        conexao = conectar()
        if conexao.is_connected():
            print("Conexão realizada com sucesso!")
    except Exception as erro:
        print(erro)
    finally:
        if conexao and conexao.is_connected():
            conexao.close()
            print("Conexão encerrada.")
 
