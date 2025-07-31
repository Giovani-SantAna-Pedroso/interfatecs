from screens import hello
import utils

def show_screen():
    utils.clear_screen()
    print("""
          \n
Texto ajuda
Texto ajuda
Texto ajuda
Texto ajuda
Texto ajuda
Texto ajuda
          \n
          """)
    input("Precione enter para voltar: ")
    hello.show_screen()
    
