from Modelos.ClasseVinho import *
from prettytable import PrettyTable
from Utilidades.Entrada_dados import entrada_dados
from Modelos.ClasseProdutor import Produtor
from Menus.MenuProdutor import visualizar_todos as visualizar_todos_produtores
from Modelos.ClasseRegiao import Regiao
from Menus.MenuRegiao import visualizar_regioes as visualizar_todas_regioes
from Modelos.ClasseTipoVinho import TipoVinho
from Menus.MenuTipoVinho import visualizar_sotipo as visualizar_todos_tipos

def menu_vinho():
    vinho_db = Vinho()
    while True:
        import os
        os.system("cls")
        print("\nMenu de Vinhos")
        print("\n1 - Adicionar Um Novo Vinho")
        print("2 - Atualizar Stock De Vinho")
        print("3 - Eliminar Um Vinho")
        print("4 - Visualizar Todos Os Vinhos")
        print("5 - Visualizar Vinhos Com Stock")
        print("6 - Visualizar Vinhos Sem Stock")
        print("7 - Procurar por determinado Ano")
        print("8 - Procurar por determinado Nome")
        print("0 - Voltar ao menu principal")
        escolha = input("\nSelecione uma opção: ")
        try:
            escolha = int(escolha)
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if escolha == 0:
            break
        elif escolha == 1:
            adicionar_vinho(vinho_db)
        elif escolha == 2:
            atualizar_stock(vinho_db)  # feito
        elif escolha == 3:
            eliminar_vinho(vinho_db)  # feito
        elif escolha == 4:
            visualizar_todos(vinho_db)  # feito
        elif escolha == 5:
            visualizar_stock(vinho_db)  # feito
        elif escolha == 6:
            visualizar_semstock(vinho_db)  # feito
        elif escolha == 7:
            visualizar_vinhos_ano(vinho_db)  # feit
        elif escolha == 8:
            visualizar_vinho_nome(vinho_db)
        else:
            print("Opção inválida, por favor tente novamente.")

        input("\nPressione Enter para continuar...")


def adicionar_vinho(vinho_db):
    produtor_db = Produtor()
    regiao_db = Regiao()
    tiposvinho_db = TipoVinho()

    nome = entrada_dados("Nome do Vinho: ", vinho_db.validacao_nome)
    ano = entrada_dados("Ano: ", vinho_db.validacao_ano)

    print("Produtores disponiveis: ")
    visualizar_todos_produtores(produtor_db)
    id_produtor = input("ID do Produtor: ")

    print("Regioes Disponiveis: ")
    visualizar_todas_regioes(regiao_db)
    id_regiao = input("ID da Região: ")

    print("Tipo de Vinho: ")
    visualizar_todos_tipos(tiposvinho_db)
    id_tipovinho = input("ID do Tipo de Vinho: ")

    preco = entrada_dados("Preço: ", vinho_db.validacao_preco)
    quantidade = entrada_dados("Quantidade: ", vinho_db.validacao_quantidade)

    sucesso = vinho_db.adicionar_vinho(
        nome, ano, id_produtor, id_regiao, id_tipovinho, preco, quantidade
    )

    if sucesso:
        print("Vinho adicionado com sucesso.")
    else:
        print("Erro ao adicionar vinho.")


def atualizar_stock(vinho_db):
    idvinho = input("Digite o ID do vinho para alterar o stock: ")
    novo_quantidade = entrada_dados(
        "Qual o novo stock do produto?: ", vinho_db.validacao_quantidade
    )

    sucesso = vinho_db.atualizar_stock_vinho(idvinho, novo_quantidade)

    if sucesso:
        print("Stock atualizado com sucesso.")
    else:
        print("Erro ao atualizar stock do produto.")


def eliminar_vinho(vinho_db):
    Idvinho = input("Digite o ID do vinho a ser eliminado: ")
    vinho_db.eliminar_vinho(Idvinho)
    print("Vinho apagado com sucesso.")


def visualizar_todos(vinho_db):
    vinhos = vinho_db.visualizar_vinho()
    tabela = PrettyTable()
    tabela.title = "Listagem de Vinhos"
    tabela.field_names = [
        "ID",
        "Nome",
        "Ano",
        "Produtor",
        "Região",
        "Tipo de Vinho",
        "Stock",
        "Preço",
    ]
    for vinho in vinhos:
        tabela.add_row(
            [
                vinho["IdVinho"],
                vinho["NomeVinho"],
                vinho["AnoVinho"],
                vinho["NomeProdutor"],
                vinho["NomeRegiao"],
                vinho["TipoVinho"],
                vinho["Quantidade"],
                vinho["Preco"],
            ]
        )
    print(tabela)

def visualizar_vinho_simples(vinho_db):
    vinhos = vinho_db.visualizar_vinho()
    for vinho in vinhos:
        print(f"ID: {vinho['IdVinho']}, Nome: {vinho['NomeVinho']}")


def visualizar_stock(vinho_db):
    vinhos = vinho_db.visualizar_vinho_stock()
    tabela = PrettyTable()
    tabela.title = "Vinhos com Stock"
    tabela.field_names = [
        "ID",
        "Nome",
        "Ano",
        "Produtor",
        "Regiao",
        "Tipo de Vinho",
        "Stock",
        "Preco",
    ]
    for vinho in vinhos:
        tabela.add_row(
            [
                vinho["IdVinho"],
                vinho["NomeVinho"],
                vinho["AnoVinho"],
                vinho["NomeProdutor"],
                vinho["NomeRegiao"],
                vinho["TipoVinho"],
                vinho["Quantidade"],
                vinho["Preco"],
            ]
        )
    print(tabela)


def visualizar_semstock(vinho_db):
    vinhos = vinho_db.visualizar_vinho_semstock()
    tabela = PrettyTable()
    tabela.title = "Vinhos sem Stock"
    #query = """Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, produtor.Nome as NomeProdutor, regiao.Regiao as NomeRegiao, tipovinho.TipoVinho as TipoVinho, vinho.Quantidade as Quantidade, vinho.Preco as Preco from vinho

    tabela.field_names = ["ID", "Nome", "Ano", "Produtor", "Regiao", "Tipo de Vinho", "Stock", "Preco"]
    for vinho in vinhos:
        tabela.add_row(
            [
                vinho["IdVinho"],
                vinho["NomeVinho"],
                vinho["AnoVinho"],
                vinho["NomeProdutor"],
                vinho["NomeRegiao"],
                vinho["TipoVinho"],
                vinho["Quantidade"],
                vinho["Preco"],
            ]
        )
    print(tabela)


def visualizar_vinhos_ano(vinho_db):
    ano = entrada_dados("Digite o Ano que deseja verificar: ", vinho_db.validacao_ano)
    vinhos = vinho_db.visualizar_vinho_ano(ano)
    tabela = PrettyTable()
    tabela.title = f"Vinhos de {ano}"
    tabela.field_names = ["ID", "Nome", "Ano", "Produtor", "Regiao", "Tipo de Vinho", "Stock", "Preco"]
    for vinho in vinhos:
        tabela.add_row(
            [
                vinho["IdVinho"],
                vinho["NomeVinho"],
                vinho["AnoVinho"],
                vinho["NomeProdutor"],
                vinho["NomeRegiao"],
                vinho["TipoVinho"],
                vinho["Quantidade"],
                vinho["Preco"],
            ]
        )
    print(tabela)


def visualizar_vinho_nome(vinho_db):
    nome = entrada_dados(
        "Escreva uma letra ou nome para procurar: ", vinho_db.validacao_nome
    )
    vinhos = vinho_db.visualizar_vinho_nome(nome)
    tabela = PrettyTable()
    tabela.title = f"Vinhos com: {nome}"
    tabela.field_names = ["ID", "Nome", "Ano", "Produtor", "Regiao", "Tipo de Vinho", "Stock", "Preco"]
    for vinho in vinhos:
        tabela.add_row(
            [
                vinho["IdVinho"],
                vinho["NomeVinho"],
                vinho["AnoVinho"],
                vinho["NomeProdutor"],
                vinho["NomeRegiao"],
                vinho["TipoVinho"],
                vinho["Quantidade"],
                vinho["Preco"],
            ]
        )
    print(tabela)


def main():
    menu_vinho()


if __name__ == "__main__":
    main()
