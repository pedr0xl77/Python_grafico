from tkinter import *

class Application:
    def __init__(self, master = None):
        self.fontePadrao = ("Arial", "10")
        self.prieiroContainer = Frame(master)
        self.prieiroContainer["pady"] = 10
        self.prieiroContainer.pack()
        
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack
        
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack
        
        self.titulo = Label(self.prieiroContainer, text="Dados do Usuario")
        self.titulo["Font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        
        self.nomeLabel = Label(self.segundoContainer,text="Nome")
        self.nomeLabel.pack(side=LEFT)
        
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        
        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
        
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        
root = Tk()
Application(root)
root.mainloop()
