from conta import ContaCorrente, ContaPoupanca
from pessoas import Cliente

agencias = []
numero_contas = []
clientes = []


def criar_conta(nome, idade, agencia, numero_conta, saldo, limite=None):
    cliente = {"c" + str(len(clientes) + 1): dict(nome=nome, idade=idade)}

    if limite and limite > 0:
        conta = ContaCorrente(agencia, numero_conta, saldo, limite)
    else:
        conta = ContaPoupanca(agencia, numero_conta, saldo)

    agencias.append(agencia)
    numero_contas.append(numero_conta)
    clientes.append(cliente)

    return Cliente(nome, idade, conta)


c1 = criar_conta("Celso Furtado", 42, 1, 111, 500)
print(agencias)
print(numero_contas)
print(clientes, len(clientes))