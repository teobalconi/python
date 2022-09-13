import re


def teste(cnpj_num, dig1, dig2):
    if (cnpj_num[-2] == str(dig1) and cnpj_num[-1] == str(dig2)):
        print("CNPJ válido!")
    else:
        print("CNPJ inválido!")
    # return True if (cnpj_num[-2] == str(dig1) and cnpj_num[-1] == str(dig2)) else False


def contador(start=5):
    cont = ""
    for i, k in enumerate(range(start, 1, -1)):
        # cont.join(str(k))
        cont += str(k)
    for i, k in enumerate(range(9, 1, -1)):
        cont += str(k)
    return cont


def remover_caracteres(cnpj_raw):
    return re.sub(r'[^0-9]', '', cnpj_raw)


def conta(cnpj_num, cont):
    somatorio = 0
    for i in range(len(cont)):
        somatorio += int(cnpj_num[i]) * int(cont[i])
    resultado = 11 - (somatorio % 11)
    return 0 if resultado > 9 else resultado


# Testes
if __name__ == "__main__":
    cnpj_bruto = "04.252.011/0001-10"
    cnpj = remover_caracteres(cnpj_bruto)
    # print(cnpj, len(cnpj), cnpj[0], type(cnpj))

    cont1 = contador(5)
    cont2 = contador(6)
    # print(cont1, len(cont1), cont1[0], type(cont1))

    dig1 = conta(cnpj, cont1)
    dig2 = conta(cnpj, cont2)
    #print(conta(cnpj, cont1))

    teste(cnpj, dig1, dig2)
