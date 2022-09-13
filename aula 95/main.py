import re
import cnpj_functions as func

while True:
    #cnpj = "04.252.011/0001-10"
    cnpj = input("Digite o CNPJ a ser validado (formato: xx.xxx.xxx/xxxx-xx) ou SAIR para encerrar: \n")

    if cnpj == 'sair':
        break
    elif not re.match("^[0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2}$", cnpj):
        print("CNPJ: Formato incorreto")
        continue

    # Separa os números
    cnpj_num = func.remover_caracteres(cnpj)
    # Gera os números bases para os cálculos
    cont1 = func.contador(5)
    cont2 = func.contador(6)
    # Calcula os dígitos
    dig1 = func.conta(cnpj_num, cont1)
    dig2 = func.conta(cnpj_num, cont2)
    #Verifica se os dígitos são iguais
    func.teste(cnpj_num, dig1, dig2)
