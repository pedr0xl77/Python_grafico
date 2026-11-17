import tkinter as tk

limpar_visor = False  # Variável para controlar se o visor deve ser limpo antes de digitar

def digitar(numero):
    global limpar_visor

    operadores = ["+", "-", "×", "÷"]

    if numero in operadores:
        limpar_visor = False  # Não limpar o visor se for um operador
        
        if visor.get() and visor.get()[-1] in operadores: # Se o último caractere no visor for um operador, substitui pelo novo operador
            visor.delete(len(visor.get()) - 1, tk.END)

    if limpar_visor:
        visor.delete(0, tk.END)
        limpar_visor = False
    
    # Reseta a cor para preto caso estivesse mostrando "Erro" antes
    visor.config(fg="black")
    visor.insert(tk.END, numero)

def limpar():
    global limpar_visor
    visor.delete(0, tk.END)
    visor.config(fg="black") # Reseta a cor do visor
    limpar_visor = False

def apagar():
    visor.delete(len(visor.get()) - 1, tk.END)

def calcular():
    global limpar_visor
    try:
        expressao = visor.get().replace("×", "*").replace("÷", "/")
        resultado = float(eval(expressao))
        
        # Se for um número inteiro (ex: 5.0), remove o decimal
        if resultado % 1 == 0:
            resultado = int(resultado)
        else:
            resultado = round(resultado, 2)
            
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
        visor.config(fg="black") # Garante cor normal em caso de sucesso
        
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")
        visor.config(fg="red") # Deixa o texto vermelho apenas no erro
        
    limpar_visor = True  # Sinaliza que o visor deve ser limpo na próxima digitação

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("320x490")

visor = tk.Entry(janela, font=("Arial", 24), width=16, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

teclado = tk.Frame(janela)
teclado.grid(row=1, column=0, padx=10, pady=10)

# --- LINHA 0 ---
btnC = tk.Button(teclado, text="C", font=("Arial", 14), width=5, height=2, command=limpar)
btnC.grid(row=0, column=0, padx=5, pady=5)

btnBackSpace = tk.Button(teclado, text="⌫", font=("Arial", 14), width=5, height=2, command=apagar)
btnBackSpace.grid(row=0, column=1, padx=5, pady=5)

btnDivisao = tk.Button(teclado, text="÷", font=("Arial", 14), width=5, height=2, command=lambda: digitar("÷"))
btnDivisao.grid(row=0, column=2, padx=5, pady=5)

btnMultiplicação = tk.Button(teclado, text="×", font=("Arial", 14), width=5, height=2, command=lambda: digitar("×"))
btnMultiplicação.grid(row=0, column=3, padx=5, pady=5)

# --- LINHA 1 ---
btn7 = tk.Button(teclado, text="7", font=("Arial", 14), width=5, height=2, command=lambda: digitar("7"))
btn7.grid(row=1, column=0, padx=5, pady=5)

btn8 = tk.Button(teclado, text="8", font=("Arial", 14), width=5, height=2, command=lambda: digitar("8"))
btn8.grid(row=1, column=1, padx=5, pady=5)

btn9 = tk.Button(teclado, text="9", font=("Arial", 14), width=5, height=2, command=lambda: digitar("9"))
btn9.grid(row=1, column=2, padx=5, pady=5)

btnMenos = tk.Button(teclado, text="-", font=("Arial", 14), width=5, height=2, command=lambda: digitar("-"))
btnMenos.grid(row=1, column=3, padx=5, pady=5)

# --- LINHA 2 ---
btn4 = tk.Button(teclado, text="4", font=("Arial", 14), width=5, height=2, command=lambda: digitar("4"))
btn4.grid(row=2, column=0, padx=5, pady=5)

btn5 = tk.Button(teclado, text="5", font=("Arial", 14), width=5, height=2, command=lambda: digitar("5"))
btn5.grid(row=2, column=1, padx=5, pady=5)

btn6 = tk.Button(teclado, text="6", font=("Arial", 14), width=5, height=2, command=lambda: digitar("6"))
btn6.grid(row=2, column=2, padx=5, pady=5)

btnMais = tk.Button(teclado, text="+", font=("Arial", 14), width=5, height=2, command=lambda: digitar("+"))
btnMais.grid(row=2, column=3, padx=5, pady=5)

# --- LINHA 3 ---
btn1 = tk.Button(teclado, text="1", font=("Arial", 14), width=5, height=2, command=lambda: digitar("1"))
btn1.grid(row=3, column=0, padx=5, pady=5)

btn2 = tk.Button(teclado, text="2", font=("Arial", 14), width=5, height=2, command=lambda: digitar("2"))
btn2.grid(row=3, column=1, padx=5, pady=5)

btn3 = tk.Button(teclado, text="3", font=("Arial", 14), width=5, height=2, command=lambda: digitar("3"))
btn3.grid(row=3, column=2, padx=5, pady=5)

btnIgual = tk.Button(teclado, text="=", font=("Arial", 14), width=5, height=5, command=calcular)
btnIgual.grid(row=3, column=3, rowspan=2, padx=5, pady=5)

# --- LINHA 4 ---
btn0 = tk.Button(teclado, text="0", font=("Arial", 14), width=11, height=2, command=lambda: digitar("0"))
btn0.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

btnPonto = tk.Button(teclado, text=".", font=("Arial", 14), width=5, height=2, command=lambda: digitar("."))
btnPonto.grid(row=4, column=2, padx=5, pady=5)

janela.mainloop()