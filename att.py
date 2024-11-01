# Alunas: Lara de Araujo, Jamile Reis, Lamony das Merces
# Turma: G93313

import os
os.system ("cls || clear")

#funcoes: adicionar livro, excluir livro, adicionar funcinario, adicionar leitor, excluir leitor
livros = []
funcionarios = []
leitores = []

def mostrar_menu():
        
    print("""
    ======= BIBLIOTECA =======
    --------------------------------
    |Código | Descrição            |
    |-------|----------------------|
    | 1     | Adicionar Livro      |
    | 2     | Excluir Livro        |
    | 3     | Adicionar Funcionário|
    | 4     | Adicionar Leitor     |
    | 5     | Excluir Leitor       |
    | 6     | Funcionários         |
    | 7     | Leitores             |
    | 8     | Livros               |
    | 0     | Sair                 |""")
#6 = funcionarios 7 = leitores 8 = livros

def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    livros.append(titulo)
    print(f"Livro {titulo} adicionado com sucesso!")
