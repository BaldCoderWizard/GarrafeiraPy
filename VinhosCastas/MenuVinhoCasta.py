from PreparacaoDataBase.GarrafeiraBD import Database
from VinhosCastas.ClasseVinhoCasta import *


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


def adicionar_casta_vinho(vc_db):
    idvinho = input("ID do Vinho: ")
    idcasta = input("ID da Casta: ")

    sucesso = vc_db.adicionar_casta_vinho(idvinho, idcasta)

    if sucesso:
        print("Casta adicionada com sucesso.")
    else:
        print("Erro ao adicionar casta.")


def remover_casta_vinho(vc_db):
    idvinho = input("Digite o ID do vinho para eliminar Casta: ")
    idcasta = input("Qual o ID da casta a remover?: ")

    sucesso = vc_db.remover_casta_vinho(idvinho, idcasta)

    if sucesso:
        print("Casta removida com sucesso.")
    else:
        print("Erro ao remover casta do vinho.")

def visualizar_todos(vc_db):
    vinhos = vc_db.visualizar_todos()
    for vinho in vinhos:
        print(f"ID: {vinho['IdVinho']}, Nome: {vinho['NomeVinho']}, Ano: {vinho['AnoVinho']}, Castas: {vinho['Castas']}")
#Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, GROUP_CONCAT(casta.Casta ORDER BY casta.Casta SEPARATOR ', ') AS Castas FROM vinho

def visualizar_casta_vinho(vc_db):
    idvinho = input("Escreva o ID do vinho para verificar as suas castas: ")
    vinhos = vc_db.visualizar_casta_vinho(idvinho)
    for vinho in vinhos:
        print(f"ID: {vinho['IdVinho']}, Nome: {vinho['NomeVinho']}, Ano: {vinho['AnoVinho']}, Tipo de Vinho: {vinho['TipoVinho']}, Castas: {vinho['Castas']}")

#Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, tipovinho.TipoVinho as TipoVinho, GROUP_CONCAT(casta.Casta ORDER BY casta.Casta SEPARATOR ', ') AS Castas FROM vinho

def visualizar_vinho_casta(vc_db):
    nome = input("Escreva a Casta a procurar: ")
    vinhos = vc_db.visualizar_vinho_casta(nome)
    for vinho in vinhos:
        print(f"ID: {vinho['IdVinho']}, Nome: {vinho['NomeVinho']}, Ano: {vinho['AnoVinho']}, Tipo de Vinho: {vinho['TipoVinho']}")
#Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, tipovinho.TipoVinho as TipoVinho FROM vinho
   
def main():
    menu_vinho_casta()

if __name__ == "__main__":
    main()


