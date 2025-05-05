import random
import string
import paperclip
import tkinter as tk
from tkinter import messagebox

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho < 4:
            messagebox.showwarning("Aviso", "A senha deve ter pelo menos 4 caracteres.")
            return
        
        caracteres = ""
        if var_maiuscula.get():
            caracteres += string.ascii_uppercase
        if var_minuscula.get():
            caracteres += string.ascii_lowercase
        if var_numeros.get():
            caracteres += string.digits
        if var_especiais.get():
            caracteres += string.punctuation
        
        if not caracteres:
            messagebox.showwarning("Aviso", "Selecione pelo menos um tipo de caractere.")
            return
        
        senha = "".join(random.sample(caracteres, tamanho))
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para o tamanho da senha.")

def copiar_senha():
    senha = entry_senha.get()
    if senha:
        pyperclip.copy(senha)
        messagebox.showinfo("Copiado!", "Senha copiada para a área de transferência.")
    else:
        messagebox.showwarning("Aviso", "Gere uma senha antes de copiar.")

# Criando a interface gráfica
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("400x350")

# Elementos da interface
tk.Label(root, text="Tamanho da senha:", font=("Arial", 12)).pack()
entry_tamanho = tk.Entry(root)
entry_tamanho.pack()

var_maiuscula = tk.BooleanVar()
var_minuscula = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_especiais = tk.BooleanVar()

tk.Checkbutton(root, text="Letras Maiúsculas", variable=var_maiuscula).pack()
tk.Checkbutton(root, text="Letras Minúsculas", variable=var_minuscula).pack()
tk.Checkbutton(root, text="Números", variable=var_numeros).pack()
tk.Checkbutton(root, text="Caracteres Especiais", variable=var_especiais).pack()

tk.Button(root, text="Gerar Senha", command=gerar_senha).pack()
entry_senha = tk.Entry(root, font=("Arial", 14), justify="center")
entry_senha.pack()

tk.Button(root, text="Copiar Senha", command=copiar_senha).pack()

root.mainloop()
