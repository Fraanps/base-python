import tkinter as ttk
import orm
from tkinter import messagebox

def adiciona_filmes():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.adiciona_filme(nome, ano, nota)
    messagebox.showinfo("Sucesso", "Filme cadastrado com sucesso!")


def atualiza_filmes():
    id = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.atualiza_filme(id,nome, ano, nota)
    messagebox.showinfo("Sucesso", "Filme atualizado com sucesso!")


def excluir_filmes():
    id = entry_id.get()
    orm.exclui_filme(id)
    messagebox.showinfo("Sucesso", "Filme excluído com sucesso!")



# interface gráfica
root = ttk.Tk()
root.title("Gerenciador de Filmes")

# definindo um tamanho inicial para a janela
#root.geometry("400x200")

# label_teste = ttk.Label(root, text="Isso é um teste!")
# label_teste.pack(pady=20)

# Rótulos e campos de entrada
label_id = ttk.Label(root, text='ID:')
label_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_id = ttk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = ttk.Label(root, text="Nome: ")
label_nome.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_nome = ttk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_ano = ttk.Label(root, text="Ano: ")
label_ano.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_ano = ttk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=10, pady=5)

label_nota = ttk.Label(root, text="Nota: ")
label_nota.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_nota = ttk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, padx=10, pady=5)

button_adicionar = ttk.Button(root, text="Adicionar Filme", command=adiciona_filmes)
button_adicionar.grid(row=4, column=0, columnspan=2, pady=5)

button_atualizar = ttk.Button(root, text="Atualizar Filme", command=atualiza_filmes)
button_atualizar.grid(row=5, column=0, columnspan=2, pady=5)

button_excluir = ttk.Button(root, text="Excluir Filme", command=excluir_filmes())
button_excluir.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
