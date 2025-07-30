while True:
    D, N = input().split(" ")

    if D =="0" and N == "0":
        break

    newN = N.replace(D, "")
    print(int("0" if newN == "" else newN))

