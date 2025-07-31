from screens import ajuda, selecionar_ano
import utils

def show_screen():
    utils.clear_screen()

    ajuda.show_screen
    opcoes = {
            "a":{"texto":"\t\033[1ma\033[0m - ajuda", "screen":ajuda.show_screen},
            "s":{"texto":"\t\033[1ms\033[0m - selecionar desafio", "screen": selecionar_ano.show_screen},
            "p":{"texto":"\t\033[1mp\033[0m - ver progresso", "screen":None},
            # "ajuda":{"texto":"a - ajuda", "screen":None},
            }
    entradas_validas = [ i for i in opcoes]

    print("\n\nOlá bem-vindo a ferramenta de treino para o intrefatecs - \033[4m\033[1mPython\033[0m")
    print("\nDigite qual opcão você deseja acessar:\n")

    # inprime os textos das opcoes na tela
    for i in opcoes:
        print(opcoes[i]["texto"])
                                                                                    
    print()
    while True:
        opcao = input("Sua opção: ")
        if opcao not in entradas_validas:
            print("\033[31mOpção invalida\033[0m")
        else:
            opcoes[opcao]['screen']()


