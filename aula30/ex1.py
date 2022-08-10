num = input('Digite um número inteiro: ')
try:
    num = int(num)
    if not num % 2:
        print('Número é PAR')
    else:
        print('Número é IMPAR')
except:
    print('Não foi digitado um número INTEIRO')