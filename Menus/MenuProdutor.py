from Modelos.ClasseProdutor import *
from Utilidades.Entrada_dados import entrada_dados
from prettytable import PrettyTable


def menu_produtor():
    produtor_db = Produtor()
    while True:
        import os

        os.system("cls")
        print("\nMenu Produtores")
        print("\n1 - Adicionar um novo Produtor")
        print("2 - Atualizar dados de um Produtor")
        print("3 - Eliminar um Produtor")
        print("4 - Visualizar todos os Produtores")
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
            adicionar_produtor(produtor_db)
        elif escolha == 2:
            atualizar_produtor(produtor_db)
        elif escolha == 3:
            eliminar_produtor(produtor_db)
        elif escolha == 4:
            visualizar_todos(produtor_db)
        else:
            print("Opção inválida, por favor tente novamente.")

        input("\nPressione Enter para continuar...")


def adicionar_produtor(produtor_db):
    nome = entrada_dados("Nome do Produtor: ", produtor_db.validacao_nome)
    id_regiao = entrada_dados("ID da Região: ", produtor_db.validacao_id)
    telefone = entrada_dados("Telefone: ", produtor_db.validacao_telefone)
    website = entrada_dados("URL: ", produtor_db.validacao_website)
    email = entrada_dados("E-mail: ", produtor_db.validacao_email)

    sucesso = produtor_db.adicionar_produtor(nome, id_regiao, telefone, website, email)

    if sucesso:
        print("Produtor adicionado com sucesso.")
    else:
        print("Erro ao adicionar Produtor.")


# Atualizar
def atualizar_produtor(produtor_db):
    id_produtor = entrada_dados(
        "Digite o ID do produtor que deseja atualizar: ", produtor_db.validacao_id
    )
    novo_nome = entrada_dados("Novo nome do Produtor: ", produtor_db.validacao_nome)
    novo_telefone = entrada_dados("Novo telefone: ", produtor_db.validacao_telefone)
    novo_website = entrada_dados("Novo website: ", produtor_db.validacao_website)
    novo_email = entrada_dados("Novo e-mail: ", produtor_db.validacao_email)

    sucesso = produtor_db.atualizar_produtor(
        id_produtor, novo_nome, novo_telefone, novo_website, novo_email
    )

    if sucesso:
        print("Produtor atualizado com sucesso.")
    else:
        print("Erro ao atualizar Produtor.")


def visualizar_todos(produtor_db):
    produtores = produtor_db.visualizar_produtores()
    tabela = PrettyTable()
    tabela.title = "Listagem de Produtores"
    tabela.field_names = [
        "ID",
        "Nome",
        "Regiao",
        "Telefone",
        "Website",
        "Email",
    ]
    for produtor in produtores:
        tabela.add_row(
            [
                produtor["IdProdutor"],
                produtor["Nome"],
                produtor["IdRegiao"],
                produtor["Telefone"],
                produtor["Website"],
                produtor["Email"],
            ]
        )
    print(tabela)


def eliminar_produtor(produtor_db):
    IdProdutor = entrada_dados(
        "Digite o ID do Produtor a ser eliminado: ", produtor_db.validacao_id
    )
    produtor_db.eliminar_produtor(IdProdutor)


def main():
    menu_produtor()


if __name__ == "__main__":
    main()
