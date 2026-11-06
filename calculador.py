import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("320x490")  # Aumentado levemente a altura para caber todas as linhas confortavelmente

visor = tk.Entry(janela, font=("Arial", 24), width=16, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

teclado = tk.Frame(janela)
teclado.grid(row=1, column=0, padx=10, pady=10)

# --- LINHA 0 ---
btnC = tk.Button(teclado, text="C", font=("Arial", 14), width=5, height=2)
btnC.grid(row=0, column=0, padx=5, pady=5)

btnBackSpace = tk.Button(teclado, text="⌫", font=("Arial", 14), width=5, height=2)
btnBackSpace.grid(row=0, column=1, padx=5, pady=5)

btnDivisao = tk.Button(teclado, text="%", font=("Arial", 14), width=5, height=2)
btnDivisao.grid(row=0, column=2, padx=5, pady=5)

btnMultiplicação = tk.Button(teclado, text="x", font=("Arial", 14), width=5, height=2)
btnMultiplicação.grid(row=0, column=3, padx=5, pady=5)

# --- LINHA 1 ---
btn7 = tk.Button(teclado, text="7", font=("Arial", 14), width=5, height=2)
btn7.grid(row=1, column=0, padx=5, pady=5)

btn8 = tk.Button(teclado, text="8", font=("Arial", 14), width=5, height=2)
btn8.grid(row=1, column=1, padx=5, pady=5)

btn9 = tk.Button(teclado, text="9", font=("Arial", 14), width=5, height=2)  # Corrigido o texto de "8" para "9"
btn9.grid(row=1, column=2, padx=5, pady=5)

btnMenos = tk.Button(teclado, text="-", font=("Arial", 14), width=5, height=2)
btnMenos.grid(row=1, column=3, padx=5, pady=5)

# --- LINHA 2 ---
btn4 = tk.Button(teclado, text="4", font=("Arial", 14), width=5, height=2)
btn4.grid(row=2, column=0, padx=5, pady=5)

btn5 = tk.Button(teclado, text="5", font=("Arial", 14), width=5, height=2)  # Corrigido o texto de "6" para "5"
btn5.grid(row=2, column=1, padx=5, pady=5)

btn6 = tk.Button(teclado, text="6", font=("Arial", 14), width=5, height=2)
btn6.grid(row=2, column=2, padx=5, pady=5)

# MAIS GRANDE: rowspan=2 dobra a altura, e aumentamos o height para preencher o visual
btnMais.grid(row=2, column=3, rowspan=2, padx=5, pady=5)
btnMais = tk.Button(teclado, text="=", font=("Arial", 14), width=5, height=5)

# --- LINHA 3 ---
btn1 = tk.Button(teclado, text="1", font=("Arial", 14), width=5, height=2)
btn1.grid(row=3, column=0, padx=5, pady=5)

btn2 = tk.Button(teclado, text="2", font=("Arial", 14), width=5, height=2)
btn2.grid(row=3, column=1, padx=5, pady=5)

btn3 = tk.Button(teclado, text="3", font=("Arial", 14), width=5, height=2)
btn3.grid(row=3, column=2, padx=5, pady=5)
# O botão '+' ocupa a coluna 3 desta linha automaticamente devido ao rowspan

# --- LINHA 4 ---
# ZERO GRANDE: columnspan=2 dobra a largura, e aumentamos ligeiramente o width
btn0 = tk.Button(teclado, text="0", font=("Arial", 14), width=11, height=2)
btn0.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

btnPonto = tk.Button(teclado, text=".", font=("Arial", 14), width=5, height=2)
btnPonto.grid(row=4, column=2, padx=5, pady=5)

janela.mainloop()
