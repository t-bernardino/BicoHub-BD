import mysql.connector

def criaConexaoBD(host_name, user_name, user_password, db_name): #ABRE CONEXÃO COM O BANCO
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def executaConsulta(connection, query): # EXECUTA UMA CONSULTA. UTILIZADO APENAS PARA ALTERAÇÕES DIRETAS COM O BANCO
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def leConsulta(connection, query): # FAZ UMA CONSULTA E RETORNA O RESULTADO DA MESMA
    cursor = connection.cursor()
    resultado = None
    try:
        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado
    except Error as err:
        print(f"Error: '{err}'")

def criarTabela(connection, query): #CRIA UMA NOVA TABELA
    try:
        cursor.execute("CREATE TABLE cliente (\n  Id_cliente int NOT NULL AUTO_INCREMENT,\n  nome_cliente char(50) NOT NULL,\n  cpf_cliente char(14) NOT NULL,\n  email_cliente char(50) NOT NULL,\n  telefone_cliente char(11) NOT NULL,\n  id_endereço int DEFAULT '1',\n  PRIMARY KEY (Id_cliente),\n  KEY Cliente_Endereço__fk (id_endereço)\n) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3)")
        print("Tabela criada")
    except Error as err:
        print("Erro na criação")
                   

