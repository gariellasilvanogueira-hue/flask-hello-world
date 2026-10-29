import os
from datetime import datetime
from tabulate import tabulate
from flask import Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    print ('Acesso a Pagina inicial', flush=True)
    mensagem = os.getenv('MENSAGEM', 'Ola, Fasf!')
    return f'<h1>{mensagem}</h1><p>Aula de PaaS<p>'

@app.route('/sobre')
def sobre():
    return 'Computacao em Nuvem -FASF AULA DO NILTON'
    
anotacoes = []

def adicionar_anotacao():
    data = datetime.now().strftime("%d/%m/%Y")
    assunto = input("Digite o assunto: ")
    anotacao = input("Digite sua anotação: ")

    anotacoes.append([data, assunto, anotacao])
    print("\nAnotação adicionada com sucesso!\n")

def mostrar_anotacoes():
    if not anotacoes:
        print("\nNenhuma anotação registrada.\n")
        return

    cabecalho = ["Data", "Assunto", "Anotação"]

    print(tabulate(
        anotacoes,
        headers=cabecalho,
        tablefmt="grid"
    ))

def menu():
    while True:
        print("===== TABELA DE ANOTAÇÕES =====")
        print("1 - Adicionar anotação")
        print("2 - Mostrar anotações")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_anotacao()
        elif opcao == "2":
            mostrar_anotacoes()
        elif opcao == "3":
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida!\n")

menu()
