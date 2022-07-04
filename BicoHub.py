import manipulaBD

conexao = manipulaBD.criaConexaoBD('localhost','root','root','bd')
cursor = conexao.cursor()

def insereCliente(nome, cpf, email, telefone, endereco):
    comando = f'INSERT INTO cliente (nome_cliente, cpf_cliente, email_cliente, telefone_cliente) VALUES ("{nome}", "{cpf}", "{email}", "{telefone}")'
    cursor.execute(comando)
    conexao.commit()


"""
def insereEndereco(rua, numero, complemento, cep):





def insereJob(cliente, titulo, descricao):





def insereProfissional(cpf, nome, email, telefone, endereco):





def insereProposta(idProfissional,idJob):





def insereServicoJob(idJob, idTagServico):




def insereServicoProfissional(idProfissional, idTagServico):





def insereTagServico(titulo, descricao):



"""

insereCliente("Jose da silva", "12345678912","joao@gmail.com","12345678",5)