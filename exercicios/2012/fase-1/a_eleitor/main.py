while True:
    cpf = input()
    # cpf = "44562101-16"

    if cpf == "0000000000-00":
        break

    cpf_val, dig = cpf.split("-")
    cpf_val = ("0" * (10 - len(cpf_val))) + cpf_val
    
    dig1 = 0
    dig2 = 0

    sigma = 0

    for i in range(0,len(cpf_val) -2):
        # print(f"{cpf_val[i]} * {9 -i }")
        sigma += int(cpf_val[i]) * (9 -i )

    resto_d1 = sigma % 11

    if resto_d1 > 1:
        dig1 = 11 - resto_d1
    else:
        if cpf_val[-2:] == '01' or cpf_val[9] == '2':
            dig1 = 1 if resto_d1 ==0 else 0
        else: 
            dig2 = 0 

    # print("digito 1", dig1)

    omega = (int(cpf_val[8]) * 4) + (int(cpf_val[9]) * 3) + (dig1 * 2)

    resto_d2 = omega % 11

    if resto_d2 > 1:
        # print("1")
        dig2 = 11 - resto_d2
    else:
        if cpf_val[-2:] == '01' or cpf_val[9] == '2':
            dig2 = 1 if resto_d2 ==0 else 0

            # print("2")
        else: 
            # print("3")
            dig2 = 0 

    # print("digito 2", dig2)

    if dig == (str(dig1) + str(dig2)):
        print('correto')
    else:
        print( (str(dig1) + str(dig2)))



# erro 12202-81



