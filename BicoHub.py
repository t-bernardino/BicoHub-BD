from manipulaBD import ConectorSQL

conexao = ConectorSQL.criaConexaoBD()
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



def insereProfissional(cpf, nome, email, telefone): # INSERE UMA ENTRADA NA TABELA PROFISSIONAL
    
    comando = f'INSERT INTO profissional (cpf_profissional, nome_profissional, email_profissional, telefone_prof) VALUES ("{cpf}", "{nome}", "{email}", "{telefone}")'
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
    resultados = ConectorSQL.leConsulta(conexao, consulta)

    for resultado in resultados:
        lista_bd.append(resultado)
    
    print(lista_bd)

def consulta(query): # CONSULTA E RETORNA UM CLIENTE PELO NOME

    #consulta = f'{query}'
    resultados = ConectorSQL.leConsulta(conexao, query)
    return resultados

    """
    widths = []
    columns = []
    tavnit = '|'
    separator = '+' 
    for cd in cursor.description:
        widths.append(max(columnnm(cd[0]), len(cd[0])))
        columns.append(cd[0])

    for w in widths:
        tavnit += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in resultados:
        print(tavnit % row)
    print(separator)
    """

def consultaClienteNome(nome): # CONSULTA E RETORNA UM CLIENTE PELO NOME

    query = "SELECT * FROM cliente WHERE nome_cliente LIKE '%"+nome+"%'"
    print(consulta(query))

def consultaClienteCPF(cpf): # CONSULTA E RETORNA UM CLIENTE PELO CPF

    query = "SELECT * FROM cliente WHERE cpf_cliente LIKE '%"+cpf+"%'"
    return consulta(query)

def consultaClienteCodigo(codigo): # CONSULTA E RETORNA UM CLIENTE PELO CÓDIGO

    query = f'SELECT * FROM cliente WHERE Id_cliente = {codigo}'
    return consulta(query)

def consultaProfissionalNome(nome): # CONSULTA E RETORNA UM PROFISSIONAL PELO NOME

    query = "SELECT * FROM profissional WHERE nome_profissional LIKE '%"+nome+"%'"
    return consulta(query)

def consultaProfissionaCPF(cpf): # CONSULTA E RETORNA UM PROFISSIONAL PELO CPF

    query = "SELECT * FROM profissional WHERE cpf_profissional LIKE '%"+cpf+"%'"
    return consulta(query)

def consultaProfissionaCodigo(codigo): # CONSULTA E RETORNA UM PROFISSIONAL PELO CÓDIGO

    query = f'SELECT * FROM profissional WHERE id_profissional = {codigo}'
    return consulta(query)

def retornaIdCliente(nome):

    query = "SELECT Id_cliente FROM cliente WHERE nome_cliente  LIKE '%"+nome+"%'"
    return consulta(query)

def mostraJobsClientes(nome):

    query = "SELECT cliente.Id_cliente, cliente.nome_cliente, job.titulo_job FROM (job INNER JOIN cliente ON job.id_cliente = cliente.Id_cliente) WHERE cliente.nome_cliente LIKE '%"+nome+"%'"
    print(consulta(query))

def pesquisaProfissionalTag(servico):

    query = "SELECT profissional.nome_profissional, tag_de_servico.titulo_tag FROM ((profissional INNER JOIN serviço_profissional ON profissional.id_profissional = serviço_profissional.id_profissional) INNER JOIN tag_de_servico ON serviço_profissional.id_tag_de_servico = tag_de_servico.id_tag_de_servico) WHERE tag_de_servico.titulo_tag LIKE '%"+servico+"%'"
    print(consulta(query))




def selecionaEndereco(rua,numero,complemento,cep):

    query = "SELECT id_endereco FROM endereco WHERE rua='"+{rua}+"' and numero="+{numero}+" and complemento="+{complemento}+" and cep="+{cep}
    return consulta(query)

"""
def consultaClienteId(id): #CONSULTA E RETORNA UM CLIENTE PELA ID

    consulta = f'SELECT * FROM cliente WHERE Id_cliente = {id}'
    resultados = manipulaBD.leConsulta(conexao, consulta)
    return resultados
"""

def cadastrarUsuario():

    nome = input("Digite o nome do usuario:")
    cpf = input("Informe o cpf do cliente:")
    email = input("Informe o email do cliente:")
    telefone = input("Informe o telefone do cliente:")
    insereCliente(nome,cpf,email,telefone)
    rua = input("Digite o numero da rua: \n")
    numero = input("Insira o numero: \n")
    complemento = input("Insira o complemento: \n")
    cep = input("Insira o cep: \n")
    insereEndereco(rua, numero, complemento, cep)
    print("Cliente cadastrado com sucesso!")
    
    
def cadastrarPrestador():
    
    cpf = input("Digite o CPF do profissional: \n")
    nome = input("Digite o nome do profissional: \n ")
    email = input("Digite o email do profissional: \n")
    telefone = input("Digite o telefone do profissional: \n")
    insereProfissional(cpf, nome, email, telefone)
    rua = input("Digite o numero da rua: \n")
    numero = input("Insira o numero: \n")
    complemento = input("Insira o complemento: \n")
    cep = input("Insira o cep: \n")
    insereEndereco(rua, numero, complemento, cep)
    print("Profissional cadastrado com sucesso!")





appInit = True # INICIO DA APLICAÇÃO
while(appInit):

    print("Selecione uma das opções: ")
    print("0 - Criar estrutura")
    print("1 - Cadastrar")
    print("2 - Pesquisar")
    print("3 - Configurações")
    print("4 - Sair")

    opcao = input("Digite o numero correspondente \n")

    if opcao == "0":
        ConectorSQL.criarTabela(conexao)

    elif opcao == "1":
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar prestador")

        escolhaCadastro = input("Digite a opção desejada \n")

        if escolhaCadastro == "1":
            cadastrarUsuario()
        elif escolhaCadastro == "2":
            cadastrarPrestador()

    elif opcao == "2":

        print("1 - Pesquisar por nome do cliente")
        print("2 - Pesquisar por ID do cliente")
        print("3 - Pesquisar 

        escolhaBusca = input("Digite a opção desejada: \n")

        if escolhaBusca == "1":
            nomeBusca = input("Digite o nome do cliente que deseja buscar: \n")
            print(consultaClienteNome(nomeBusca))
        elif escolhaBusca == "2":
            idBusca = input("Digite a id do cliente que deseja buscar: \n")
            print(consultaClienteCodigo(idBusca))
        else:
            print('Opção inválida')
        
    elif opcao == "4":
        appInit = False
        print("Obrigado por usar a aplicação!")
    
    else:
        print("Opcao Inválida!")
