import utils
from screens import hello
import os
import webbrowser

path_exercicios = "./exercicios"
path_exercicios_absoluto = os.path.abspath(path_exercicios)
def show_screen():
    utils.clear_screen()
    print("\nSelecione o ano\n")
    ano_selecionado = ""

    anos = os.listdir(path_exercicios)
    anos.sort()
    for i in anos:
        print(i, end=" - ")
    print("\n")

    while True:
        ano_selecionado = input("Ano selecionado (v para voltar a tela incial): ").strip()

        if ano_selecionado == "v":
            hello.show_screen()

        if ano_selecionado not in anos:
            print("\033[31mOpção invalida\033[0m")
        else:
            break

    print(f"\nAno selecionado: \033[1m{ano_selecionado}\033[0m\n")

    
    print("Selecione a fase: \n")
    fases = os.listdir(f"{path_exercicios}/{ano_selecionado}")
    fases.sort()
    for i in fases :
        print(i, end=" - ")
    print("\n")

    while True:
        fase_selecionado = input("Escolha uma opção: ").strip()

        if fase_selecionado not in fases:
            print("\033[31mOpção invalida\033[0m")
        else:
            break

    print(f"fase selecionada: \033[1m{fase_selecionado}\033[0m")
    abrir_pdf =""

    desafios = os.listdir(f"{path_exercicios}/{ano_selecionado}/{fase_selecionado}")
    desafios.sort()

    while abrir_pdf != 'S' and abrir_pdf != "N":
        abrir_pdf = input("Deseja abrir os PDF dos desafios: S/N: ").upper()
        print(abrir_pdf)   

    if abrir_pdf== 'S':
        print("asdf")
        pdfs = list(filter(lambda i: i.endswith(".pdf"), desafios))
        print(pdfs)
        for i in pdfs:
            webbrowser.open(f"file://{path_exercicios_absoluto}/{ano_selecionado}/{fase_selecionado}/{i}")
            print(f"file://{path_exercicios_absoluto}/{ano_selecionado}/{i}")

    desafios = list(filter(lambda i: not i.endswith(".pdf"), desafios))


    print("Selecione um desafio: \n")
    for i in desafios :
        print(i, end=" - ")
    print("\n")

    while True:
        desafio_selecionado = input("Escolha uma opção: ").strip()

        if desafio_selecionado not in desafios:
            print("\033[31mOpção invalida\033[0m")
        else:
            break

        
    



    ...
