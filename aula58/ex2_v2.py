def funcao1(nome='Fulano'):
    return f'Oi, {nome}'

def funcao2(saudacao='Dae fei', nome='Sicrano'):
    return f'{saudacao}, {nome}'

def main(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

f1 = main(funcao1, nome="Beltrano")
f2 = main(funcao2, nome = 'Vatapá', saudacao = 'É nóis')
print(f1)
print(f2)