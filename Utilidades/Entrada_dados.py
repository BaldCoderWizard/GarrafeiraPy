def entrada_dados(mensagem, metodo_validacao, opcional=False):
    while True:
        entrada = input(mensagem)
        if opcional and entrada == '':
            return entrada
        elif metodo_validacao(entrada):
            return entrada
        else:
            print("Tente novamente.")