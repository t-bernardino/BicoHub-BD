import manipulaBD

conexao = manipulaBD.criaConexaoBD('localhost','root','root','bd')
cursor = conexao.cursor()

def insereCliente(nome, cpf, email, telefone, endereco):
    
    comando = f'INSERT INTO cliente (nome_cliente, cpf_cliente, email_cliente, telefone_cliente) VALUES ("{nome}", "{cpf}", "{email}", "{telefone}")'
    cursor.execute(comando)
    conexao.commit()



def insereEndereco(rua, numero, complemento, cep):

    comando = f'INSERT INTO endereço (rua, numero, complemento, cep) VALUES ("{rua}", {numero}, "{complemento}", "{cep}")'
    cursor.execute(comando)
    conexao.commit()


def insereJob(cliente, titulo, descricao):

    comando = f'INSERT INTO job (id_cliente, titulo_job, descricao_job) VALUES ("{cliente}", "{titulo}", "{descricao}")'
    cursor.execute(comando)
    conexao.commit()



def insereProfissional(cpf, nome, email, telefone, endereco):
    comando = f'INSERT INTO profissional (cpf_profissional, nome_profissional, email_profissional, telefone_prof) VALUES ("{cpf}", "{nome}", "{email}", "{telefone}", "{endereco}")'
    cursor.execute(comando)
    conexao.commit()




def insereProposta(idProfissional,idJob):
    comando = f'INSERT INTO proposta (id_profissional, id_job) VALUES ({idProfissional}, {idJob})'
    cursor.execute(comando)
    conexao.commit()




def insereServicoJob(idJob, idTagServico):
    comando = f'INSERT INTO servico_job (id_job, id_tag_servico) VALUES ({idJob}, {idTagServico})'
    cursor.execute(comando)
    conexao.commit()



def insereServicoProfissional(idProfissional, idTagServico):
    comando = f'INSERT INTO servico_profissional (id_profissional, id_tag_servico) VALUES ({idProfissional}, {idTagServico})'
    cursor.execute(comando)
    conexao.commit()




def insereTagServico(titulo, descricao):
    comando = f'INSERT INTO tag_de_servico (titulo_tag, desc_tag) VALUES ("{titulo}", "{descicao}")'
    cursor.execute(comando)
    conexao.commit()



def leTodosClientes():
    lista_bd = []
    consulta = """SELECT * FROM cliente;"""
    resultado = manipulaBD.executaConsulta(conexao, consulta)