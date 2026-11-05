import tkinter as tk


class Application:
    def __init__(self, master=None):
        master.title("teclado da calculadora")



        botao_7 = tk.Button(master, text="7", width=5, height=2)
        botao_7.grid(row=0, column=0)

        botao_8 = tk.Button(master, text="8", width=5, height=2)
        botao_8.grid(row=0, column=1)

        botao_9 = tk.Button(master, text="9", width=5, height=2)
        botao_9.grid(row=0, column=2)

        self.entrada = tk.Entry(master, width=20)
        self.entrada.grid(row=1, column=0, columnspan=3, pady=10)

        botao_7.config(command=lambda: self.digitar("7"))
        botao_8.config(command=lambda: self.digitar("8"))
        botao_9.config(command=lambda: self.digitar("9"))

    def digitar(self, numero):
        self.entrada.insert(tk.END, numero)

janela = tk.Tk()
app = Application(master=janela)
janela.mainloop()