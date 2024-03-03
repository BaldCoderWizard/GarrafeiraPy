from Regioes.MenuRegiao import menu_regiao
from Produtores.MenuProdutor import menu_produtor
from Castas.MenuCasta import menu_casta
from TipoVinhos.MenuTipoVinho import menu_tipovinho
from Vinhos.MenuVinho import menu_vinho
from VinhosCastas.MenuVinhoCasta import menu_vinho_casta

def menu_principal():
    while True:
        import os 
        os.system('cls')
        print("\nGarrafeira Pessoal 1.0 \n\nEscolha uma Opcao:")
        print("\n1 - Região")
        print("2 - Produtor")
        print("3 - Casta")
        print("4 - Tipo de Vinho")
        print("5 - Vinhos")
        print("6 - Castas dos Vinhos")
        print("0 - Sair")

        escolha = input("\nSelecione uma opção: ")
        try:
            escolha = int(escolha)
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if escolha == 0:
            break
        elif escolha == 1:
            menu_regiao()
        elif escolha == 2:
            menu_produtor()
        elif escolha == 3:
            menu_casta()
        elif escolha == 4:
            menu_tipovinho()
        elif escolha == 5:
            menu_vinho()
        elif escolha == 6:
            menu_vinho_casta()
        else:
            print("Opção inválida, por favor tente novamente.")
        
        
        
if __name__ == "__main__":
    menu_principal()
