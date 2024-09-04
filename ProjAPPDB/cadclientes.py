from tkinter import *
from tkinter import ttk
from clientes import Clientes

class Cliente:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontepadrao = ("Arial", 14)
        self.fontebotao = ("Calibri", 13)
        self.janela.pack()

    #TITULO
        self.titulo = Label(self.janela, text="Informe os Dados:")
        self.titulo["font"] = ("Calibri", "30", "italic", "bold")
        self.titulo.pack()
        self.titulo2 = Label(self.janela, text="Cadastro de Clientes\n")
        self.titulo2["font"] = ("Calibri", "20", "italic")
        self.titulo2.pack()

    # ID CLIENTE
        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idLabel = Label(self.janela2, text="idCliente:     \n", font=self.fontepadrao)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela2)
        self.id["width"] = 18
        self.id["font"] = self.fontepadrao
        self.id.pack(side=LEFT)

        self.buscar = Button(self.janela2, font=self.fontebotao)
        self.buscar["text"] = "Buscar"
        self.buscar["width"] = 10
        self.buscar.pack(side=LEFT)
        self.buscar["command"] = self.buscarCliente  # BANCO DE DADOS

    #CLIENTE
        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.clienteLabel = Label(self.janela3, text="Cliente:     \n", font=self.fontepadrao)
        self.clienteLabel.pack(side=LEFT)
        self.cliente = Entry(self.janela3)
        self.cliente["width"] = 30
        self.cliente["font"] = self.fontepadrao
        self.cliente.pack(side=LEFT)



    #CIDADE
        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.cidadeLabel = Label(self.janela2, text="Cidade:  \n", font=self.fontepadrao)
        self.cidadeLabel.pack(side=LEFT)
        self.cidade = Entry(self.janela2)
        self.cidade["width"] = 30
        self.cidade["font"] = self.fontepadrao
        self.cidade.pack(side=LEFT)


    # ENDEREÇO
        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.enderecoLabel = Label(self.janela6, text="Endereço: \n", font=self.fontepadrao)
        self.enderecoLabel.pack(side=LEFT)
        self.endereco = Entry(self.janela6)
        self.endereco["width"] = 29
        self.endereco["font"] = self.fontepadrao
        self.endereco.pack(side=LEFT)

    # TELEFONE
        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.telefoneLabel = Label(self.janela4, text="Telefone: \n", font=self.fontepadrao)
        self.telefoneLabel.pack(side=LEFT)
        self.telefone = Entry(self.janela4)
        self.telefone["width"] = 29
        self.telefone["font"] = self.fontepadrao
        self.telefone.pack(side=LEFT)


    #EMAIL
        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.emailLabel = Label(self.janela5, text="E-mail:    \n", font=self.fontepadrao)
        self.emailLabel.pack(side=LEFT)
        self.email = Entry(self.janela5)
        self.email["width"] = 30
        self.email["font"] = self.fontepadrao
        self.email.pack(side=LEFT)


    #BOTÕES
        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.inserir = Button(self.janela8, font=self.fontebotao)
        self.inserir["text"] = "Inserir"
        self.inserir["width"] = 10
        self.inserir.pack(side=LEFT)
        self.inserir["command"] = self.inserirCliente

        self.alt = Button(self.janela8, font=self.fontebotao)
        self.alt["text"] = "Alterar"
        self.alt["width"] = 10
        self.alt.pack(side=LEFT)
        self.alt["command"] = self.alterarCliente

        self.excluir = Button(self.janela8, font=self.fontebotao)
        self.excluir["text"] = "Excluir"
        self.excluir["width"] = 10  # largura
        self.excluir.pack(side=LEFT)
        self.excluir["command"] = self.excluirCliente

        self.sair = Button(self.janela8, font=self.fontebotao)
        self.sair["text"] = "Voltar"
        self.sair["width"] = 10  # largura
        self.sair["command"] = self.janela.quit
        self.sair.pack(side=LEFT)

        # MENSAGEM
        self.mensagemLabel = Label(master, text="", font=("Arial", 14))
        self.mensagemLabel.pack(pady=10)

        # TREEVIEW para exibir informações da cidade buscada
        self.tree_frame = Frame(master)
        self.tree_frame.pack(pady=10)

        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "Cliente", "Cidade", "Endereço", "Telefone", "Email"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Cliente", text="Cliente")
        self.tree.heading("Cidade", text="Cidade")
        self.tree.heading("Endereço", text="Endereço")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Email", text="Email")
        self.tree.pack()

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

    def atualizarTabela(self):
        cli = Clientes()
        clientes = cli.selectAllCli()
        self.tree.delete(*self.tree.get_children())
        for c in clientes:
            self.tree.insert("", "end", values=(c[0], c[1], c[2], c[3], c[4], c[5]))

    def buscarCliente(self):
        cli = Clientes()
        idclientes = self.id.get()
        status = cli.selectCli(idclientes)
        if status == "Busca feita com sucesso!":
            self.id.delete(0, END)
            self.id.insert(INSERT, cli.idclientes)
            self.cliente.delete(0, END)
            self.cliente.insert(INSERT, cli.cliente)
            self.cidade.delete(0, END)
            self.cidade.insert(INSERT, cli.cidade)
            self.endereco.delete(0, END)
            self.endereco.insert(INSERT, cli.endereco)
            self.telefone.delete(0, END)
            self.telefone.insert(INSERT, cli.telefone)
            self.email.delete(0, END)
            self.email.insert(INSERT, cli.email)
        self.mensagemLabel["text"] = status
        self.atualizarTabela()

    def inserirCliente(self):
            cli = Clientes()
            cli.cliente = self.cliente.get()
            cli.cidade = self.cidade.get()
            cli.endereco = self.endereco.get()
            cli.telefone = self.telefone.get()
            cli.email = self.email.get()
            status = cli.insertCli()
            self.mensagemLabel["text"] = status
            self.limparCampos()
            self.atualizarTabela()

    def alterarCliente(self):
            cli = Clientes()
            cli.cliente = self.cliente.get()
            cli.cidade = self.cidade.get()
            cli.endereco = self.endereco.get()
            cli.telefone = self.telefone.get()
            cli.email = self.email.get()
            status = cli.updateCli()
            self.mensagemLabel["text"] = status
            self.limparCampos()
            self.atualizarTabela()

    def excluirCliente(self):
            cli = Clientes()
            cli.idclientes = self.id.get()
            status = cli.deleteCli()
            self.mensagemLabel["text"] = status
            self.limparCampos()
            self.atualizarTabela()

    def limparCampos(self):
        self.id.delete(0, END)
        self.cliente.delete(0, END)
        self.cidade.delete(0, END)
        self.telefone.delete(0, END)
        self.endereco.delete(0, END)
        self.email.delete(0, END)

root = Tk()
Cliente(root)
root.state("zoomed") #para a tela sempre aparecer maximizada
root.mainloop()
