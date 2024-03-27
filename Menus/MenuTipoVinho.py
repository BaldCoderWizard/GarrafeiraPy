from Modelos.ClasseTipoVinho import *
from Utilidades.Entrada_dados import entrada_dados
from prettytable import PrettyTable

def menu_tipovinho():
    tipo_db = TipoVinho()
    while True:
        import os 
        os.system('cls')
        print("\nMenu de Tipos de Vinho")
        print("\n1 - Adicionar um novo Tipo")
        print("2 - Visualizar todos os Tipos")
        print("3 - Eliminar uma Tipo de Vinho")
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
            adicionar_tipo(tipo_db)
        elif escolha == 2:
            visualizar_tipo(tipo_db)
        elif escolha == 3:
            eliminar_tipo(tipo_db)
        else:
            print("Opção inválida, por favor tente novamente.")
        
        input("\nPressione Enter para continuar...")

def adicionar_tipo(tipo_db):
    tipovinho = entrada_dados("Tipo de Vinho: ", tipo_db.validacao_tipo)
    descricao = entrada_dados("Descricao do Tipo: ", tipo_db.validacao_descricao)
    sucesso = tipo_db.adicionar_tipovinho(tipovinho, descricao)
    if sucesso:
        print("Tipo adicionado com sucesso.")
    else:
        print("Erro ao adicionar Tipo de Vinho.")

def visualizar_tipo(tipo_db):
    tipos = tipo_db.visualizar_tipo()
    tabela = PrettyTable()
    tabela.title = "Lista de Tipos de Vinho"
    tabela.field_names =[
        "ID",
        "Tipo",
        "Descricao",
    ]
    for tipo in tipos:
       tabela.add_row(
           [
               tipo['IdTipoVinho'], 
               tipo['TipoVinho'],
               tipo['Descricao']
            ]
        )
    tabela.max_width["Descricao"] = 100
    tabela.align["Descricao"] = "l"   
    print(tabela)

def visualizar_sotipo(tipo_db):
    tipos = tipo_db.visualizar_tipo()
    print("Lista de Tipos de Vinho:")
    for tipo in tipos:
        print(f"ID: {tipo['IdTipoVinho']} - Tipo: {tipo['TipoVinho']}")


def eliminar_tipo(tipo_db):
    idtipo = entrada_dados("Qual o ID do Tipo de Vinho a eliminar?: ", tipo_db.validacao_id)
    tipo_db.eliminar_tipo(idtipo)
    
def main():
    menu_tipovinho()

if __name__ == "__main__":
    main()