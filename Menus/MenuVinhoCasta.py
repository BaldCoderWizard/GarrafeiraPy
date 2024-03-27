from Modelos.ClasseVinhoCasta import *
from Modelos.ClasseVinho import Vinho
from Modelos.ClasseCasta import Casta
from Menus.MenuVinho import visualizar_vinho_simples
from Menus.MenuCasta import visualizar_casta_simples
from prettytable import PrettyTable
from Utilidades.Entrada_dados import entrada_dados

vinho_db = Vinho()
casta_db = Casta()


def menu_vinho_casta():
    vc_db = VinhoCasta()
    while True:
        import os 
        os.system('cls')
        print("\nMenu Vinhos e Castas")
        print("1 - Adicionar uma Casta a um Vinho")
        print("2 - Remover uma Casta de um Vinho")
        print("3 - Visualizar Vinhos e Castas")
        print("4 - Visualizar Castas de um Vinho")
        print("5 - Visualizar Vinhos com uma Casta")
        print("0 - Voltar ao menu principal")
        escolha = input("Selecione uma opção: ")
        try:
            escolha = int(escolha)
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if escolha == 0:
            break
        elif escolha == 1:
            adicionar_casta_vinho(vc_db)#feito
        elif escolha == 2:
            remover_casta_vinho(vc_db)#falta
        elif escolha == 3:
            visualizar_todos(vc_db)
        elif escolha == 4:
            visualizar_casta_vinho(vc_db)#feito
        elif escolha == 5:
            visualizar_vinho_casta(vc_db)#feito
        else:
            print("Opção inválida, por favor tente novamente.")

        input("\nPressione Enter para continuar...")


def adicionar_casta_vinho(vc_db):
    print("Vinhos disponiveis: ")
    visualizar_vinho_simples(vinho_db)
    idvinho = entrada_dados("ID do Vinho: ", vc_db.validacao_id)
    print("Castas disponiveis:")
    visualizar_casta_simples(casta_db)
    idcasta = entrada_dados("ID da Casta: ", vc_db.validacao_id)

    sucesso = vc_db.adicionar_casta_vinho(idvinho, idcasta)

    if sucesso:
        print("Casta adicionada com sucesso.")
    else:
        print("Erro ao adicionar casta.")


def remover_casta_vinho(vc_db):
    idvinho = entrada_dados("Digite o ID do vinho para eliminar Casta: ", vc_db.validacao_id)
    idcasta = entrada_dados("Qual o ID da casta a remover?: ", vc_db.validacao_id)

    sucesso = vc_db.remover_casta_vinho(idvinho, idcasta)

    if sucesso:
        print("Casta removida com sucesso.")
    else:
        print("Erro ao remover casta do vinho.")

def visualizar_todos(vc_db):
    vinhos = vc_db.visualizar_todos()
    tabela = PrettyTable()
    tabela.title = "Todos os Vinhos e as suas Castas"
    tabela.field_names = [
        "ID",
        "Nome",
        "Ano",
        "Castas"
    ]
    for vinho in vinhos:
        tabela.add_row(
            [
                vinho["IdVinho"],
                vinho["NomeVinho"],
                vinho["AnoVinho"],
                vinho["Castas"],
            ]
        )
    print(tabela)

def visualizar_casta_vinho(vc_db):
    idvinho = entrada_dados("Escreva o ID do vinho para verificar as suas castas: ", vc_db.validacao_id)
    vinhos = vc_db.visualizar_casta_vinho(idvinho)
    tabela = PrettyTable()
    tabela.title = "Castas"
    tabela.field_names = [
        "ID",
        "Nome",
        "Ano",
        "Tipo de Vinho",
        "Castas"
    ]
    for vinho in vinhos:
        tabela.add_row(
            [
                vinho["IdVinho"],
                vinho["NomeVinho"],
                vinho["AnoVinho"],
                vinho['TipoVinho'],
                vinho["Castas"],
            ]
        )
    print(tabela)

def visualizar_vinho_casta(vc_db):
    nome = entrada_dados("Escreva a Casta a procurar: ", vc_db.validacao_nome)
    vinhos = vc_db.visualizar_vinho_casta(nome)
    tabela = PrettyTable()
    tabela.title = f"Vinhos com a casta {nome}"
    tabela.field_names = [
        "ID",
        "Nome",
        "Ano",
        "Tipo de Vinho",
    ]
    for vinho in vinhos:
        tabela.add_row(
            [
                vinho["IdVinho"],
                vinho["NomeVinho"],
                vinho["AnoVinho"],
                vinho['TipoVinho'],
            ]
        )
    print(tabela)
   
def main():
    menu_vinho_casta()

if __name__ == "__main__":
    main()


