import manipulaBD

conexao = manipulaBD.criaConexaoBD('localhost','kaueVB','kaueVB','sys')
cursor = conexao.cursor()

def insereCliente(nome, cpf, email, telefone): # INSERE UMA ENTRADA NA TABELA CLIENTE
    
    comando = f'INSERT INTO cliente (nome_cliente, cpf_cliente, email_cliente, telefone_cliente) VALUES ("{nome}", "{cpf}", "{email}", "{telefone}")'
    cursor.execute(comando)
    conexao.commit()



def insereEndereco(rua, numero, complemento, cep): # INSERE UMA ENTRADA NA TABELA ENDEREÇO

    comando = f'INSERT INTO endereço (rua, numero, complemento, cep) VALUES ("{rua}", {numero}, "{complemento}", "{cep}")'
    cursor.execute(comando)
    conexao.commit()


def insereJob(cliente, titulo, descricao): # INSERE UMA ENTRADA NA TABELA JOB

    comando = f'INSERT INTO job (id_cliente, titulo_job, descricao_job) VALUES ("{cliente}", "{titulo}", "{descricao}")'
    cursor.execute(comando)
    conexao.commit()



def insereProfissional(cpf, nome, email, telefone, endereco): # INSERE UMA ENTRADA NA TABELA PROFISSIONAL
    
    comando = f'INSERT INTO profissional (cpf_profissional, nome_profissional, email_profissional, telefone_prof) VALUES ("{cpf}", "{nome}", "{email}", "{telefone}", "{endereco}")'
    cursor.execute(comando)
    conexao.commit()




def insereProposta(idProfissional,idJob): # INSERE UMA ENTRADA NA TABELA PROPOSTA
    comando = f'INSERT INTO proposta (id_profissional, id_job) VALUES ({idProfissional}, {idJob})'
    cursor.execute(comando)
    conexao.commit()




def insereServicoJob(idJob, idTagServico): # INSERE UMA ENTRADA NA TABELA SERVICO_JOB
    comando = f'INSERT INTO servico_job (id_job, id_tag_servico) VALUES ({idJob}, {idTagServico})'
    cursor.execute(comando)
    conexao.commit()



def insereServicoProfissional(idProfissional, idTagServico): #INSERE UMA ENTRADA NA TABELA SERVICO_PROFISSIONAL

    comando = f'INSERT INTO servico_profissional (id_profissional, id_tag_servico) VALUES ({idProfissional}, {idTagServico})'
    cursor.execute(comando)
    conexao.commit()


def insereTagServico(titulo, descricao): #INSERE UMA ENTRADA NA TABELA TAG_SERVICO

    comando = f'INSERT INTO tag_de_servico (titulo_tag, desc_tag) VALUES ("{titulo}", "{descricao}")'
    cursor.execute(comando)
    conexao.commit()



def leTodosClientes(): #LE E RETORNA TODOS OS CLIENTES DO BANCO
    lista_bd = []
    consulta = """SELECT * FROM cliente;"""
    resultados = manipulaBD.leConsulta(conexao, consulta)

    for resultado in resultados:
        lista_bd.append(resultado)
    
    print(lista_bd)

def consultaClienteNome(nome): # CONSULTA E RETORNA UM CLIENTE PELO NOME

    consulta = f'SELECT * FROM cliente WHERE nome_cliente = "{nome}"'
    resultados = manipulaBD.leConsulta(conexao, consulta)
    return resultados

def consultaClienteId(id): #CONSULTA E RETORNA UM CLIENTE PELA ID

    consulta = f'SELECT * FROM cliente WHERE Id_cliente = {id}'
    resultados = manipulaBD.leConsulta(conexao, consulta)
    return resultados

def cadastrarUsuario():

    nome = input("Digite o nome do usuario:")
    cpf = input("Informe o cpf do cliente:")
    email = input("Informe o email do cliente:")
    telefone = input("Informe o telefone do cliente:")
    insereCliente(nome,cpf,email,telefone)
    print("Cliente cadastrado com sucesso!")





appInit = True # INICIO DA APLICAÇÃO
while(appInit):

    print("Selecione uma das opções: ")
    print("0 - Criar estrutura")
    print("1 - Cadastrar Cliente")
    print("2 - Pesquisar Cliente")
    print("3 - Sair")

    opcao = input("Digite o numero correspondente")

    if opcao == "0":
        manipulaBD.criarTabela(conexao)

    elif opcao == "1":
        cadastrarUsuario()

    elif opcao == "2":

        print("1 - Pesquisar por nome")
        print("2 - Pesquisar por código")

        escolhaBusca = input("Digite a opção desejada:")

        if escolhaBusca == "1":
            nomeBusca = input("Digite o nome do cliente que deseja buscar: ")
            print(consultaClienteNome(nomeBusca))
        elif escolhaBusca == "2":
            idBusca = input("Digite a id do cliente que deseja buscar: ")
            print(consultaClienteId(idBusca))
        else:
            print('Opção inválida')
        
    elif opcao == "3":
        appInit = False
        print("adiós")
    
    else:
        print("Opcao Inválida!")
