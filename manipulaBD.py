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


