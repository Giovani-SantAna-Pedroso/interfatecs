from os import system, name
import subprocess


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')



def testar_script(script_path, in_file, out_file):
    # Ler conteúdo dos arquivos de entrada e saída esperada
    with open(in_file, 'r') as f:
        entrada = f.read()
    with open(out_file, 'r') as f:
        esperado = f.read().strip()

    # Executar o script Python passando a entrada via stdin
    processo = subprocess.run(
        ['python', script_path],
        input=entrada,
        text=True,
        capture_output=True
    )

    saida = processo.stdout.strip()

    if saida == esperado:
        print("Saída correta!")
        return True
    else:
        print("Saída incorreta.")
        print("Esperado:")
        print(esperado)
        print("Recebido:")
        print(saida)
        return False

# Exemplo de uso:
# testar_script('meu_script.py', 'entrada.in', 'saida.out')
