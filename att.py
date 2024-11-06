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

def excluir_livro():
    titulo = input("Digite o título do livro que deseja excluir: ")
    if titulo in livros:
        livros.remove(titulo)
        print(f"Livro {titulo} removido da biblioteca.")
    else:
        print(f"Livro {titulo} não encontrado.")

def adicionar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    funcionarios.append(nome)
    print(f"Funcionário {nome} adicionado com sucesso!")

def adicionar_leitor():
    nome = input("Digite o nome do leitor: ")
    leitores.append(nome)
    print(f"Leitor {nome} adicionado com sucesso!")

def excluir_leitor():
    nome = input("Digite o nome do leitor que deseja excluir: ")
    if nome in leitores:
        leitores.remove(nome)
        print(f"Leitor {nome} removido com sucesso!")
    else:
        print(f"Leitor {nome} não encontrado.")

while True:
    mostrar_menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        excluir_livro()
    elif opcao == "3":
        adicionar_funcionario()
    elif opcao == "4":
        adicionar_leitor()
    elif opcao == "5":
        excluir_leitor()
    elif opcao == "6":
        print(funcionarios)
    elif opcao == "7":
        print(leitores)
    elif opcao == "8":
        print("\nLIVROS CADASTRADOS:")
        print(livros if livros else "Nenhum livro cadastrado.")
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")

    input("\nPressione Enter para continuar...")