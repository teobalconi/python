import re
while True:
    #cpf = "168.995.350-09"
    cpf = input("Digite o CPF a ser validado (formato: xxx.xxx.xxx-xx) ou SAIR para encerrar: \n")

    if cpf == 'sair':
        break
    elif not re.match("^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$",cpf):
        print("CPF Formato incorreto")
        continue

    #Separa os números
    n1, n2, n3 = cpf.split(".")
    n3 , dig = n3.split("-")
    num1 = (n1 + n2 + n3)

    # Verificação Dígito 1
    soma1 = 0
    for i, k in enumerate(range(10, 1, -1)):
        soma1 += (int(num1[i])*k)

    conta1 = (11 - (soma1 % 11))
    digito1 = 0 if conta1 > 9 else conta1

    # Verificação Dígito 2
    num2 = num1 + str(digito1)
    soma2 = 0
    for i, k in enumerate(range(11, 1, -1)):
        soma2 += (int(num2[i])*k)

    conta2 = (11 - (soma2 % 11))
    digito2 = 0 if conta2 > 9 else conta2

    if (n1 == n2) and (n1 == n3):
        msg = "CPF INVÁLIDO"
    elif (digito1 == int(dig[0])) and (digito2 == int(dig[1])):
        msg = "CPF válido"
    else:
        msg = "CPF INVÁLIDO"
    print(msg)
