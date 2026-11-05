import tkinter as tk

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Calculadora Simples")
        self.master.geometry("350x250")

        self.lbl_numero1 = tk.Label(self.master, text="Número 1:")
        self.lbl_numero1.pack()

        self.entrada1 = tk.Entry(self.master)
        self.entrada1.pack()

        self.lbl_numero2 = tk.Label(self.master, text="Número 2:")
        self.lbl_numero2.pack()

        self.entrada2 = tk.Entry(self.master)
        self.entrada2.pack()

        self.botao_somar = tk.Button(self.master, text="Somar", command=self.somar)
        self.botao_somar.pack(pady=15)

        self.lbl_resultado = tk.Label(self.master, text="Resultado: ")
        self.lbl_resultado.pack()

    def somar(self):
        n1 = float(self.entrada1.get())
        n2 = float(self.entrada2.get())

        resultado = n1 + n2
        self.lbl_resultado.config(text=f"Resultado: {resultado}")

janela = tk.Tk()
app = Application(master=janela)
janela.mainloop()