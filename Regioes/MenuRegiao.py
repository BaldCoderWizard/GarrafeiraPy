from PreparacaoDataBase.GarrafeiraBD import Database
from Regioes.ClasseRegiao import *
from prettytable import PrettyTable

def menu_regiao():
    regiao_db = Regiao()
    while True:
        import os 
        os.system('cls')
        print("\nMenu Regiões")
        print("\n1 - Inserir nova região")
        print("2 - Atualizar região existente")
        print("3 - Excluir região")
        print("4 - Listar todas as regiões")
        print("0 - Voltar ao menu principal")
        escolha = input("\nSelecione uma opção: ")
        try:
            escolha = int(escolha)
        except ValueError:
            print("\nPor favor, insira um número válido.")
            continue

        if escolha == 0:
            break
        elif escolha == 1:
            adicionar_regiao(regiao_db)
        elif escolha == 2:
            atualizar_regiao(regiao_db)
        elif escolha == 3:
            apagar_regiao(regiao_db)
        elif escolha == 4:
            visualizar_regioes(regiao_db)
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

def adicionar_regiao(regiao_db):
    regiao = entrada_dados("Digite o nome da região a ser adicionada: ", regiao_db.validacao_regiao)
    regiao_db.adicionar_regiao(regiao)

def visualizar_regioes(regiao_db):
    regioes = regiao_db.visualizar_regiao()
    tabela = PrettyTable()
    tabela.title = "Lista de Regioes"
    tabela.field_names = ["ID", "Regiao"]
    for regiao in regioes:
        tabela.add_row([regiao['IdRegiao'],regiao['Regiao']])
    print(tabela)

def atualizar_regiao(regiao_db):
    id_regiao = input("Digite o ID da região a ser atualizada: ")
    nova_regiao = input("Digite o novo nome da região: ")
    regiao_db.atualizar_regiao(id_regiao, nova_regiao)
    print("Região atualizada com sucesso.")

def apagar_regiao(regiao_db):
    id_regiao = input("Digite o ID da região a ser apagada: ")
    regiao_db.apagar_regiao(id_regiao)

def main():
    menu_regiao()

if __name__ == "__main__":
    main()

