def funcao1(nome='Fulano'):
    return f'Oi, {nome}'

def funcao2(saudacao='Dae fei', nome='Sicrano'):
    return f'{saudacao}, {nome}'

def main():
    func1 = funcao1('Cid')
    func2 = funcao2('Opa', 'Zé')
    return func1, func2

f1 , f2 = main()
print(f1)
print(f2)