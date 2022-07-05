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

def criarTabela(connection): #CRIA UMA NOVA TABELA
    cursor = connection.cursor()
    query = f'CREATE TABLE cliente (Id_cliente int NOT NULL AUTO_INCREMENT,nome_cliente char(50) NOT NULL,cpf_cliente char(14) NOT NULL,email_cliente char(50) NOT NULL, telefone_cliente char(11) NOT NULL, id_endereço int DEFAULT "1", PRIMARY KEY (Id_cliente), KEY Cliente_Endereço__fk (id_endereço)) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3 ; CREATE TABLE endereço (id_endereco int NOT NULL AUTO_INCREMENT, rua char(50) NOT NULL, numero int DEFAULT NULL, complemento char(50) DEFAULT NULL, cep char(8) NOT NULL, PRIMARY KEY (id_endereco)) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3; CREATE TABLE job (id_job int NOT NULL AUTO_INCREMENT, id_cliente int NOT NULL, titulo_job char(50) NOT NULL, descricao_job char(200) DEFAULT NULL, PRIMARY KEY (id_job), KEY id_cliente_job (id_cliente), CONSTRAINT id_cliente_job FOREIGN KEY (id_cliente) REFERENCES cliente (Id_cliente)) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3; CREATE TABLE profissional (id_profissional int NOT NULL AUTO_INCREMENT,cpf_profissional char(14) NOT NULL, nome_profissional char(50) NOT NULL,email_profissional char(50) NOT NULL,telefone_prof char(11) NOT NULL,id_endereço int NOT NULL,PRIMARY KEY (id_profissional),KEY Profissional_Endereco (id_endereço),CONSTRAINT Profissional_Endereco FOREIGN KEY (id_endereço) REFERENCES profissional (id_profissional)) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3; CREATE TABLE proposta (id_profissional int NOT NULL,id_job int NOT NULL,valor float NOT NULL,KEY id_job (id_job),KEY id_profissional (id_profissional),CONSTRAINT id_job FOREIGN KEY (id_job) REFERENCES job (id_job),CONSTRAINT id_profissional FOREIGN KEY (id_profissional) REFERENCES profissional (id_profissional)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3; CREATE TABLE servico_job (id_job int NOT NULL,id_tag_servico int NOT NULL,KEY id_tag_de_serviço2 (id_job),KEY id_tag_de_servico2 (id_tag_servico),CONSTRAINT id_job1 FOREIGN KEY (id_job) REFERENCES job (id_job),CONSTRAINT id_tag_de_servico2 FOREIGN KEY (id_tag_servico) REFERENCES tag_de_servico (id_tag_de_servico)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3; CREATE TABLE serviço_profissional (id_profissional int NOT NULL,id_tag_de_servico int NOT NULL,KEY id_profissional1 (id_profissional),KEY id_tag_de_servico1 (id_tag_de_servico),CONSTRAINT id_profissional1 FOREIGN KEY (id_profissional) REFERENCES profissional (id_profissional),CONSTRAINT id_tag_de_servico1 FOREIGN KEY (id_tag_de_servico) REFERENCES tag_de_servico (id_tag_de_servico)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3; CREATE TABLE tag_de_servico (id_tag_de_servico int NOT NULL AUTO_INCREMENT,titulo_tag char(50) NOT NULL,desc_tag varchar(100) NOT NULL,PRIMARY KEY (id_tag_de_servico)) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3' 

    cursor.execute(query)
    connection.commit()
    print("Tabela criada")


