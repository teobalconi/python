def funcao2():
    return 'função 2 executada'

def funcao1(funcao):
    return funcao()

func = funcao1(funcao2)
print(func)