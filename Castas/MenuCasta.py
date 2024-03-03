from PreparacaoDataBase.GarrafeiraBD import Database
from Castas.ClasseCasta import *


def menu_casta():
    casta_db = Casta()
    while True:
        import os 
        os.system('cls')
        print("\nMenu Castas")
        print("\n1 - Adicionar uma nova Casta")
        print("2 - Visualizar todas as Castas")
        print("3 - Eliminar uma Casta")
        print("0 - Voltar ao menu principal")
        escolha = input("Selecione uma opção: ")
        try:
            escolha = int(escolha)
        except ValueError:
            print("\nPor favor, insira um número válido.")
            continue

        if escolha == 0:
            break
        elif escolha == 1:
            adicionar_casta(casta_db)
        elif escolha == 2:
            visualizar_casta(casta_db)
        elif escolha == 3:
            eliminar_casta(casta_db)
        else:
            print("Opção inválida, por favor tente novamente.")

        input("\nPressione Enter para continuar...")


def entrada_dados(mensagem, metodo_validacao, opcional=False):
    while True:
        entrada = input(mensagem)
        if opcional and entrada == '':
            return entrada
        elif metodo_validacao(entrada):
            return entrada
        else:
            print("Entrada inválida, tente novamente.")

def adicionar_casta(casta_db):
    casta = entrada_dados("Nome da Casta: ", casta_db.validacao_casta)
    descricao = entrada_dados("Descricao da Casta: ", casta_db.validacao_descricao)
    sucesso = casta_db.adicionar_casta(casta, descricao)
    if sucesso:
        print("Produtor adicionado com sucesso.")
    else:
        print("Erro ao adicionar Produtor.")

def visualizar_casta(casta_db):
    castas = casta_db.visualizar_casta()
    print(f"\nLista de Castas:")
    for casta in castas:
        print(f"ID: {casta['IdCasta']}, Nome: {casta['Casta']}, Descricao: {casta['Descricao']}")
def eliminar_casta(casta_db):
    IdCasta = input("Qual o ID da Casta a eliminar?: ")
    casta_db.eliminar_casta(IdCasta)
    print("A Casta foi apagada com sucesso")

def main():
    menu_casta()
    
if __name__ == "__main__":
    main()
