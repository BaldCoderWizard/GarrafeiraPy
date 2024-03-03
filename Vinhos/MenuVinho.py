from PreparacaoDataBase.GarrafeiraBD import Database
from Vinhos.ClasseVinho import *
from prettytable import PrettyTable 

def menu_vinho():
    vinho_db = Vinho()
    while True:
        import os 
        os.system('cls')
        print("\nMenu de Vinhos")
        print("\n1 - Adicionar Um Novo Vinho")
        print("2 - Atualizar Dados De Vinho")
        print("3 - Atualizar Stock De Vinho")
        print("4 - Eliminar Um Vinho")
        print("5 - Visualizar Todos Os Vinhos")
        print("6 - Visualizar Vinhos Com Stock")
        print("7 - Visualizar Vinhos Sem Stock")
        print("8 - Procurar por determinado Ano")
        print("9 - Procurar por determinado Nome")
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
            adicionar_vinho(vinho_db)#feito
        elif escolha == 2:
            atualizar_dados(vinho_db)#falta
        elif escolha == 3:
            atualizar_stock(vinho_db)#feito
        elif escolha == 4:
            eliminar_vinho(vinho_db)#feito
        elif escolha == 5:
            visualizar_todos(vinho_db)#feito
        elif escolha == 6:
            visualizar_stock(vinho_db)#feito
        elif escolha == 7:
            visualizar_semstock(vinho_db)#feito
        elif escolha == 8:
            visualizar_vinhos_ano(vinho_db)#feit
        elif escolha == 9:
            visualizar_vinho_nome(vinho_db)
        else:
            print("Opção inválida, por favor tente novamente.")

        input("\nPressione Enter para continuar...")



def adicionar_vinho(vinho_db):
    nome = input("Nome do Vinho: ")
    ano = input("Ano: ")
    id_produtor = input("ID do Produtor: ")
    id_regiao = input("ID da Região: ")
    id_tipovinho = input("ID do Tipo de Vinho: ")
    preco = input("Preço: ")
    quantidade = input("Quantidade: ")

    sucesso = vinho_db.adicionar_vinho(nome, ano, id_produtor, id_regiao, id_tipovinho, preco, quantidade)

    if sucesso:
        print("Vinho adicionado com sucesso.")
    else:
        print("Erro ao adicionar vinho.")

def atualizar_stock(vinho_db):
    idvinho = input("Digite o ID do vinho para alterar o stock: ")
    novo_quantidade = input("Qual o novo stock do produto?: ")

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
    tabela.field_names = ["ID", "Nome", "Ano", "Produtor", "Região", "Tipo de Vinho", "Stock", "Preço"]
    for vinho in vinhos:
        tabela.add_row([
            vinho['IdVinho'], vinho['NomeVinho'], vinho['AnoVinho'],
            vinho['NomeProdutor'], vinho['NomeRegiao'], vinho['TipoVinho'],
            vinho['Quantidade'], vinho['Preco']])
    print(tabela)

def visualizar_stock(vinho_db):
    vinhos = vinho_db.visualizar_vinho_stock()
    tabela = PrettyTable()
    tabela.title = "Vinhos com Stock"
    tabela.field_names = ["ID", "Nome", "Ano", "Produtor", "Regiao", "Tipo de Vinho", "Stock", "Preco"]
    for vinho in vinhos:
        tabela.add_row([vinho['IdVinho'], vinho['NomeVinho'], vinho['AnoVinho'], vinho['NomeProdutor'], vinho['NomeRegiao'], vinho['TipoVinho'], vinho['Quantidade'], vinho['Preco']])
    print(tabela)

def visualizar_semstock(vinho_db):
    vinhos = vinho_db.visualizar_vinho_semstock()
    for vinho in vinhos:
        print(f"ID: {vinho['IdVinho']}, Nome: {vinho['NomeVinho']}, Ano: {vinho['AnoVinho']}, Produtor: {vinho['NomeProdutor']}, Regiao: {vinho['NomeRegiao']}, Tipo de Vinho: {vinho['TipoVinho']}, Stock: {vinho['Quantidade']}, Preco: {vinho['Preco']}")

def visualizar_vinhos_ano(vinho_db):
    ano = input("Digite o Ano que deseja verificar: ")
    vinhos = vinho_db.visualizar_vinho_ano(ano)
    for vinho in vinhos:
        print(f"ID: {vinho['IdVinho']}, Nome: {vinho['NomeVinho']}, Ano: {vinho['AnoVinho']}, Produtor: {vinho['NomeProdutor']}, Regiao: {vinho['NomeRegiao']}, Tipo de Vinho: {vinho['TipoVinho']}, Stock: {vinho['Quantidade']}, Preco: {vinho['Preco']}")

def visualizar_vinho_nome(vinho_db):
    nome = input("Escreva um nome para procurar: ")
    vinhos = vinho_db.visualizar_vinho_nome(nome)
    for vinho in vinhos:
        print(f"ID: {vinho['IdVinho']}, Nome: {vinho['NomeVinho']}, Ano: {vinho['AnoVinho']}, Produtor: {vinho['NomeProdutor']}, Regiao: {vinho['NomeRegiao']}, Tipo de Vinho: {vinho['TipoVinho']}, Stock: {vinho['Quantidade']}, Preco: {vinho['Preco']}")
    
def main():
    menu_vinho()

if __name__ == "__main__":
    main()


