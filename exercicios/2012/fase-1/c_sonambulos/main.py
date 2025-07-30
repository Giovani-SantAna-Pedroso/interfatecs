while True:
    N = int(input())

    if N == 0:
        break

    destino = N % 4

    if destino == 1:
        print("Carlos")
    elif destino == 2:
        print("Zeca")
    elif destino == 3:
        print("Pedro")
    else :
        print("Mara")
