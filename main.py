from database.conexao import conectar
 
conexao = conectar()
 
cursor = conexao.cursor()
 
cursor.execute("SHOW TABLES")
 
for tabela in cursor.fetchall():
    print(tabela)
 
cursor.close()
conexao.close()