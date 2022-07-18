import tkinter as tk
from tkinter import Toplevel, ttk

class InterfaceGrafica():

    opcaoPesquisa = 0
          
    def criaJanelaEstrutura(janela):
        janelaEstrutura = tk.Toplevel(janela)
        frameJanelaEstrutura = tk.Frame(master=janelaEstrutura, width=900, height=200, bg="yellow")
        
        #FUNÇÃO DEVE CRIAR BASE E RETORNAR MENSAGEM DE SUCESSO OU ERRO

        mensagemCriado = tk.Label(master=frameJanelaEstrutura,text="ESTRUTURA CRIADA COM SUCESSO")
        mensagemCriado.place(x=200,y=100)
        
        
        botaoSair = tk.Button(master=frameJanelaEstrutura,text="VOLTAR",command=janelaEstrutura.destroy)
        botaoSair.place(x=200,y=150)
        frameJanelaEstrutura.pack()


    """
    def criaLayoutPesquisa(janela,opcao):

        match opcao:

            case 0:

                mensagemInvalida = tk.Label(janela,text="OPCÃO INVÁLIDA")
                mensagemInvalida.pack()

            case 1:

                rotuloCPF = tk.Label(janela,text="CPF")
                rotuloCPF.place(x=20,y=25)
                campoCPF = tk.Text(master=janela, height=1,width=60)
                campoCPF.place(x=100,y=25)
                
                rotuloNome = tk.Label(janela,text="Nome:")
                rotuloNome.place(x=20,y=55)
                campoNome = tk.Text(master=janela,height=1,width=60)
                campoNome.place(x=100,y=55)

                rotuloEmail = tk.Label(janela,text="E-mail:")
                rotuloEmail.place(x=20,y=85)
                campoEmail = tk.Text(master=janela,height=1,width=60)
                campoEmail.place(x=100,y=85)

                rotuloTelefone = tk.Label(janela,text="Telefone:")
                rotuloTelefone.place(x=20,y=115)
                campoTelefone = tk.Text(master=janela,height=1,width=60)
                campoTelefone.place(x=100,y=115)

                rotuloRua = tk.Label(janela,text="Rua")
                rotuloRua.place(x=20,y=145)
                campoRua = tk.Text(master=janela, height=1,width=60)
                campoRua.place(x=100,y=145)
                
                rotuloNumero = tk.Label(janela,text="Numero:")
                rotuloNumero.place(x=20,y=175)
                campoNumero = tk.Text(master=janela,height=1,width=60)
                campoNumero.place(x=100,y=175)

                rotuloCEP = tk.Label(janela,text="CEP:")
                rotuloCEP.place(x=20,y=205)
                campoCEP = tk.Text(master=janela,height=1,width=60)
                campoCEP.place(x=100,y=205)

                botaoPesquisar = tk.Button(master=janela,text="PESQUISAR")
                botaoPesquisar.place(x=200,y=235)
            
            case 2:

                rotuloCPF = tk.Label(janela,text="CPF")
                rotuloCPF.place(x=20,y=25)
                campoCPF = tk.Text(master=janela, height=1,width=60)
                campoCPF.place(x=100,y=25)
                
                rotuloNome = tk.Label(janela,text="Nome:")
                rotuloNome.place(x=20,y=55)
                campoNome = tk.Text(master=janela,height=1,width=60)
                campoNome.place(x=100,y=55)

                rotuloEmail = tk.Label(janela,text="E-mail:")
                rotuloEmail.place(x=20,y=85)
                campoEmail = tk.Text(master=janela,height=1,width=60)
                campoEmail.place(x=100,y=85)

                rotuloTelefone = tk.Label(janela,text="Telefone:")
                rotuloTelefone.place(x=20,y=115)
                campoTelefone = tk.Text(master=janela,height=1,width=60)
                campoTelefone.place(x=100,y=115)

            case 3:

                mensagemInvalida = tk.Label(janela,text="OPCÃO INVÁLIDA")
                mensagemInvalida.pack()
            """
    
    def criaJanelaResultado(janela):

        janelaResultado = Toplevel(janela)
        frameJanelaResultado = tk.Frame(master=janelaResultado, width=600, height=600, background="white")

        
    
    def criaJanelaPesquisa(janela):
        
        janelaPesquisa = tk.Toplevel(janela)
        frameJanelaPesquisa = tk.Frame(master=janelaPesquisa,width=900,height=800,bg="yellow")

        """
        frameBotoesSeletores = tk.Frame(master=frameJanelaPesquisa,width=840,height=200,bg="gray")
        frameBotoesSeletores.place(x=20,y=0)

        frameMostraConsulta = tk.Frame(master=frameJanelaPesquisa,width=840,height=600,bg="white")
        frameMostraConsulta.place(x=20,y=200)
        
        opcaoBotao = 0
        
        botaoPesquisaCliente = tk.Radiobutton(master=frameBotoesSeletores,text="Cliente", variable = opcaoBotao, value=1, command= lambda: InterfaceGrafica.criaLayoutPesquisa(frameMostraConsulta, 1))
        botaoPesquisaCliente.place(x=60,y=100)

        botaoPesquisaProfissional = tk.Radiobutton(master=frameBotoesSeletores,text="Profissional", variable = opcaoBotao, value=2, command= lambda: InterfaceGrafica.criaLayoutPesquisa(frameMostraConsulta, 2))
        botaoPesquisaProfissional.place(x=200,y=100)

        botaoPesquisaJob = tk.Radiobutton(master=frameBotoesSeletores,text="Job", variable = opcaoBotao, value=3, command= lambda: InterfaceGrafica.criaLayoutPesquisa(frameMostraConsulta, 3))
        botaoPesquisaJob.place(x=400,y=100)"""

        abas = ttk.Notebook(frameJanelaPesquisa)
        abaCliente = tk.Frame(abas,width=900,height=800)
        abaProfissional = tk.Frame(abas,width=900,height=800)
        abaJob = tk.Frame(abas,width=900,height=800)

        abas.add(abaCliente,text="Cliente")
        abas.add(abaProfissional,text="Profissional")
        abas.add(abaJob,text="Job")

        #ELEMENTOS DA ABA CLIENTE

        rotuloCPF = tk.Label(abaCliente,text="CPF")
        rotuloCPF.place(x=20,y=25)
        campoCPF = tk.Text(master=abaCliente, height=1,width=60)
        campoCPF.place(x=100,y=25)
                
        rotuloNome = tk.Label(abaCliente,text="Nome:")
        rotuloNome.place(x=20,y=55)
        campoNome = tk.Text(master=abaCliente,height=1,width=60)
        campoNome.place(x=100,y=55)

        rotuloEmail = tk.Label(abaCliente,text="E-mail:")
        rotuloEmail.place(x=20,y=85)
        campoEmail = tk.Text(master=abaCliente,height=1,width=60)
        campoEmail.place(x=100,y=85)

        rotuloTelefone = tk.Label(abaCliente,text="Telefone:")
        rotuloTelefone.place(x=20,y=115)
        campoTelefone = tk.Text(master=abaCliente,height=1,width=60)
        campoTelefone.place(x=100,y=115)

        rotuloRua = tk.Label(abaCliente,text="Rua")
        rotuloRua.place(x=20,y=145)
        campoRua = tk.Text(master=abaCliente, height=1,width=60)
        campoRua.place(x=100,y=145)
                
        rotuloNumero = tk.Label(abaCliente,text="Numero:")
        rotuloNumero.place(x=20,y=175)
        campoNumero = tk.Text(master=abaCliente,height=1,width=60)
        campoNumero.place(x=100,y=175)

        rotuloCEP = tk.Label(abaCliente,text="CEP:")
        rotuloCEP.place(x=20,y=205)
        campoCEP = tk.Text(master=abaCliente,height=1,width=60)
        campoCEP.place(x=100,y=205)

        botaoPesquisar = tk.Button(master=abaCliente,text="PESQUISAR")
        botaoPesquisar.place(x=200,y=235)

        botaoVoltar = tk.Button(master=abaCliente,text="VOLTAR",command=janelaPesquisa.destroy)
        botaoVoltar.place(x=350,y=235)

        #ELEMENTOS DA ABA PROFISSIONAL

        rotuloCPF = tk.Label(abaProfissional,text="CPF")
        rotuloCPF.place(x=20,y=25)
        campoCPF = tk.Text(master=abaProfissional, height=1,width=60)
        campoCPF.place(x=100,y=25)
                
        rotuloNome = tk.Label(abaProfissional,text="Nome:")
        rotuloNome.place(x=20,y=55)
        campoNome = tk.Text(master=abaProfissional,height=1,width=60)
        campoNome.place(x=100,y=55)

        rotuloEmail = tk.Label(abaProfissional,text="E-mail:")
        rotuloEmail.place(x=20,y=85)
        campoEmail = tk.Text(master=abaProfissional,height=1,width=60)
        campoEmail.place(x=100,y=85)

        rotuloTelefone = tk.Label(abaProfissional,text="Telefone:")
        rotuloTelefone.place(x=20,y=115)
        campoTelefone = tk.Text(master=abaProfissional,height=1,width=60)
        campoTelefone.place(x=100,y=115)

        rotuloRua = tk.Label(abaProfissional,text="Rua")
        rotuloRua.place(x=20,y=145)
        campoRua = tk.Text(master=abaProfissional, height=1,width=60)
        campoRua.place(x=100,y=145)
                
        rotuloNumero = tk.Label(abaProfissional,text="Numero:")
        rotuloNumero.place(x=20,y=175)
        campoNumero = tk.Text(master=abaProfissional,height=1,width=60)
        campoNumero.place(x=100,y=175)

        rotuloCEP = tk.Label(abaProfissional,text="CEP:")
        rotuloCEP.place(x=20,y=205)
        campoCEP = tk.Text(master=abaProfissional,height=1,width=60)
        campoCEP.place(x=100,y=205)

        botaoPesquisar = tk.Button(master=abaProfissional,text="PESQUISAR")
        botaoPesquisar.place(x=200,y=235)

        botaoVoltar = tk.Button(master=abaProfissional,text="VOLTAR",command=janelaPesquisa.destroy)
        botaoVoltar.place(x=350,y=235)

        #ELEMENTOS DA ABA JOB

        rotuloClienteJob = tk.Label(abaJob,text="Cliente")
        rotuloClienteJob.place(x=20,y=25)
        campoClienteJob = tk.Text(master=abaJob, height=1,width=60)
        campoClienteJob.place(x=100,y=25)
                
        rotuloTituloJob = tk.Label(abaJob,text="Título:")
        rotuloTituloJob.place(x=20,y=55)
        campoTituloJob = tk.Text(master=abaJob,height=1,width=60)
        campoTituloJob.place(x=100,y=55)

        rotuloDescricaoJob = tk.Label(abaJob,text="Descrição:")
        rotuloDescricaoJob.place(x=20,y=85)
        campoDescricaoJob = tk.Text(master=abaJob,height=1,width=60)
        campoDescricaoJob.place(x=100,y=85)

        botaoPesquisar = tk.Button(master=abaJob,text="PESQUISAR")
        botaoPesquisar.place(x=200,y=115)

        botaoVoltar = tk.Button(master=abaJob,text="VOLTAR",command=janelaPesquisa.destroy)
        botaoVoltar.place(x=350,y=115)

        abas.pack()
        frameJanelaPesquisa.pack()

    def criaJanelaInsercao(janela):

        janelaInsercao = tk.Toplevel(janela)
        frameJanelaInsercao = tk.Frame(master=janelaInsercao, width=900, height=800, bg="yellow")

        abas = ttk.Notebook(frameJanelaInsercao)
        abaCliente = tk.Frame(abas,width=900,height=800)
        abaProfissional = tk.Frame(abas,width=900,height=800)
        abaJob = tk.Frame(abas,width=900,height=800)

        abas.add(abaCliente,text="Cliente")
        abas.add(abaProfissional,text="Profissional")
        abas.add(abaJob,text="Job")

        #ELEMENTOS DA ABA CLIENTE

        rotuloCPF = tk.Label(abaCliente,text="CPF")
        rotuloCPF.place(x=20,y=25)
        campoCPF = tk.Text(master=abaCliente, height=1,width=60)
        campoCPF.place(x=100,y=25)
                
        rotuloNome = tk.Label(abaCliente,text="Nome:")
        rotuloNome.place(x=20,y=55)
        campoNome = tk.Text(master=abaCliente,height=1,width=60)
        campoNome.place(x=100,y=55)

        rotuloEmail = tk.Label(abaCliente,text="E-mail:")
        rotuloEmail.place(x=20,y=85)
        campoEmail = tk.Text(master=abaCliente,height=1,width=60)
        campoEmail.place(x=100,y=85)

        rotuloTelefone = tk.Label(abaCliente,text="Telefone:")
        rotuloTelefone.place(x=20,y=115)
        campoTelefone = tk.Text(master=abaCliente,height=1,width=60)
        campoTelefone.place(x=100,y=115)

        rotuloRua = tk.Label(abaCliente,text="Rua")
        rotuloRua.place(x=20,y=145)
        campoRua = tk.Text(master=abaCliente, height=1,width=60)
        campoRua.place(x=100,y=145)
                
        rotuloNumero = tk.Label(abaCliente,text="Numero:")
        rotuloNumero.place(x=20,y=175)
        campoNumero = tk.Text(master=abaCliente,height=1,width=60)
        campoNumero.place(x=100,y=175)

        rotuloCEP = tk.Label(abaCliente,text="CEP:")
        rotuloCEP.place(x=20,y=205)
        campoCEP = tk.Text(master=abaCliente,height=1,width=60)
        campoCEP.place(x=100,y=205)

        botaoPesquisar = tk.Button(master=abaCliente,text="CADASTRAR")
        botaoPesquisar.place(x=200,y=235)

        botaoVoltar = tk.Button(master=abaCliente,text="VOLTAR",command=janelaInsercao.destroy)
        botaoVoltar.place(x=350,y=235)

        #ELEMENTOS DA ABA PROFISSIONAL

        rotuloCPF = tk.Label(abaProfissional,text="CPF")
        rotuloCPF.place(x=20,y=25)
        campoCPF = tk.Text(master=abaProfissional, height=1,width=60)
        campoCPF.place(x=100,y=25)
                
        rotuloNome = tk.Label(abaProfissional,text="Nome:")
        rotuloNome.place(x=20,y=55)
        campoNome = tk.Text(master=abaProfissional,height=1,width=60)
        campoNome.place(x=100,y=55)

        rotuloEmail = tk.Label(abaProfissional,text="E-mail:")
        rotuloEmail.place(x=20,y=85)
        campoEmail = tk.Text(master=abaProfissional,height=1,width=60)
        campoEmail.place(x=100,y=85)

        rotuloTelefone = tk.Label(abaProfissional,text="Telefone:")
        rotuloTelefone.place(x=20,y=115)
        campoTelefone = tk.Text(master=abaProfissional,height=1,width=60)
        campoTelefone.place(x=100,y=115)

        rotuloRua = tk.Label(abaProfissional,text="Rua")
        rotuloRua.place(x=20,y=145)
        campoRua = tk.Text(master=abaProfissional, height=1,width=60)
        campoRua.place(x=100,y=145)
                
        rotuloNumero = tk.Label(abaProfissional,text="Numero:")
        rotuloNumero.place(x=20,y=175)
        campoNumero = tk.Text(master=abaProfissional,height=1,width=60)
        campoNumero.place(x=100,y=175)

        rotuloCEP = tk.Label(abaProfissional,text="CEP:")
        rotuloCEP.place(x=20,y=205)
        campoCEP = tk.Text(master=abaProfissional,height=1,width=60)
        campoCEP.place(x=100,y=205)

        botaoPesquisar = tk.Button(master=abaProfissional,text="CADASTRAR")
        botaoPesquisar.place(x=200,y=235)

        botaoVoltar = tk.Button(master=abaProfissional,text="VOLTAR",command=janelaInsercao.destroy)
        botaoVoltar.place(x=350,y=235)

        #ELEMENTOS DA ABA JOB

        rotuloClienteJob = tk.Label(abaJob,text="Cliente")
        rotuloClienteJob.place(x=20,y=25)
        campoClienteJob = tk.Text(master=abaJob, height=1,width=60)
        campoClienteJob.place(x=100,y=25)
                
        rotuloTituloJob = tk.Label(abaJob,text="Título:")
        rotuloTituloJob.place(x=20,y=55)
        campoTituloJob = tk.Text(master=abaJob,height=1,width=60)
        campoTituloJob.place(x=100,y=55)

        rotuloDescricaoJob = tk.Label(abaJob,text="Descrição:")
        rotuloDescricaoJob.place(x=20,y=85)
        campoDescricaoJob = tk.Text(master=abaJob,height=1,width=60)
        campoDescricaoJob.place(x=100,y=85)

        botaoPesquisar = tk.Button(master=abaJob,text="CADASTRAR")
        botaoPesquisar.place(x=200,y=115)

        botaoVoltar = tk.Button(master=abaJob,text="VOLTAR",command=janelaInsercao.destroy)
        botaoVoltar.place(x=350,y=115)

        abas.pack()
        frameJanelaInsercao.pack()
        





    def __init__(self):

        self.janela = tk.Tk()

        framePrincipal = tk.Frame(master=self.janela, width=900, height=600, bg="yellow")

        rotuloUm = tk.Label(master=framePrincipal,text="Manipulador de BD BicoHub",bg="gray")
        rotuloUm.place(x=10,y=10)

        botaoUm = tk.Button(master=framePrincipal,text="CRIAR ESTRUTURA",command= lambda: InterfaceGrafica.criaJanelaEstrutura(self.janela))
        #FAZER BIND AO MÉTODO QUE CRIA A ESTRUTURA - FEITO
        botaoUm.place(x=10,y=60)

        botaoDois = tk.Button(master=framePrincipal,text="FAZER PESQUISA",command= lambda: InterfaceGrafica.criaJanelaPesquisa(self.janela))
        #FAZER BIND AO MÉTODO DE PESQUISA
        botaoDois.place(x=10,y=120)

        botaoTres = tk.Button(master=framePrincipal,text="CADASTRAR ENTRADA", command= lambda: InterfaceGrafica.criaJanelaInsercao(self.janela))
        #FAZER BIND AO MÉTODO QUE CADASTRA NA BASE
        botaoTres.place(x=10,y=180)

        framePrincipal.pack()

        self.janela.mainloop()



    


app = InterfaceGrafica()