import mysql.connector

class ConectorSQL():

    host = 'localhost'
    nomeUsuario = 'root'
    senhaUsuario = 'root'
    banco = 'bd'

    def criaConexaoBD(): #ABRE CONEXÃO COM O BANCO
        connection = None
        try:
            connection = mysql.connector.connect(
                host=ConectorSQL.host,
                user=ConectorSQL.nomeUsuario,
                passwd=ConectorSQL.senhaUsuario,
                database=ConectorSQL.banco
            )
            print("MySQL Database connection successful")
        except mysql.connector.Error as err:
            print(f"Error: '{err}'")

        return connection

    def executaConsulta(connection, query): # EXECUTA UMA CONSULTA. UTILIZADO APENAS PARA ALTERAÇÕES DIRETAS COM O BANCO
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query successful")
        except mysql.connector.Error as err:
            print(f"Error: '{err}'")

    def leConsulta(connection, query): # FAZ UMA CONSULTA E RETORNA O RESULTADO DA MESMA
        cursor = connection.cursor()
        resultado = None
        try:
            cursor.execute(query)
            resultado = cursor.fetchall()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error: '{err}'")

    def criarTabela(connection): #CRIA UMA NOVA TABELA
        cursor = connection.cursor()
        
        arquivoComandos = open('cria-tabelas.sql','r')
        comandos = arquivoComandos.read()
        arquivoComandos.close()

        query = comandos.split(';')

        for comando in query:
            try:
                cursor.execute(comando)
                connection.commit()
            except mysql.connector.OperationalError as err:
                print("Um erro ocorreu: ",err)
        """
        cursor.execute(query, params=None, multi=True)
        connection.commit()
        print('Sucesso!')
        """
        cursor.close()
        cursor = connection.cursor()

    def mudaDadosConexao(novoHost,novoUser,novaSenha,novoBD):
        ConectorSQL.host = novoHost
        ConectorSQL.nomeUsuario = novoUser
        ConectorSQL.senhaUsuario = novaSenha
        ConectorSQL.banco = novoBD
