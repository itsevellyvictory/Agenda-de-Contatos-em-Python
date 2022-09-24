
#Crie, em Python, uma Agenda, que possua contatos e campos principais como nome, CPF, e e-mail. 
#A Agenda deve conter uma função para  buscar um contato pelo nome, além de adicionar e excluir um contato.

from os import system #biblioteca para limpar a tela
    
lista_contatos = []

def add_contato(): #funcao que adiciona contato
     nome = (str(input("\nDigite o nome do contato: ")))
     num = (int(input("\nDigite o número: ")))
     cpf = (str(input("\nDigite o seu CPF: ")))
     email = (str(input("\nDigite o seu e-mail: ")))
     system('cls')
     lista_add = {}
     lista_add['Nome'] = nome
     lista_add['Numero'] = num
     lista_add['CPF'] = cpf
     lista_add['Email'] = email
     lista_contatos.append(lista_add)
     print("\n####################################")
     print("\nContato Adicionado com Sucesso!")
     print("\n####################################")
     
def mostra_contato(): #funcao para mostrar o contato
    system('cls')
    for contato in lista_contatos:
        for chave, valor in contato.items():
            print(f'{chave}: {valor}')

def remove_contato(): #funcao para remover o contato
    nome = (str(input("\nDigite o nome que deseja remover: "))).lower()
    for c in lista_contatos:
        if c['Nome'].lower() == nome.lower():
           i = lista_contatos.index(c) 
           lista_contatos.pop(i)
           break
        else:
            print("\nEsse contato NÃO existe")


while True:
        print('1 - Adicionar Contato')
        print('2 - Mostrar Contato')
        print('3 - Remover Contato')
        print('4 - Sair')

        op = (int(input("\nDigite sua opção: ")))

        if op == 1:
            add_contato()
        if op ==2:
            mostra_contato()
        if op ==3:
            remove_contato()
        if op ==4:
            break
            print("Vai com Deus")