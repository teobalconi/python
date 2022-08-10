nome = input('Digite seu primeiro nome: ')

try:
    if len(nome)<=4:
        print('Seu nome é curto!')
    elif len(nome) > 6:
        print('Seu nome é muito grande!')
    else:
        print('Seu nome é normal!')
except:
    print('Texto digitado não é um nome válido!')