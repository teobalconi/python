from conta import ContaCorrente, ContaPoupanca
from pessoas import Cliente


class Banco:

    def __init__(self):
        self.agencias = []
        self.numero_contas = []
        self.clientes = []

    def criar_conta(self, nome, idade, agencia, numero_conta, saldo, limite=None):
        cliente = {"c" + str(len(self.clientes) + 1): dict(nome=nome, idade=idade)}

        if limite and limite > 0:
            conta = ContaCorrente(agencia, numero_conta, saldo, limite)
        else:
            conta = ContaPoupanca(agencia, numero_conta, saldo)

        self.agencias.append(agencia)
        self.numero_contas.append(numero_conta)
        self.clientes.append(cliente)

        return Cliente(nome, idade, conta)


if __name__ == "__main__":
    b = Banco()
    c1 = b.criar_conta("Celso Furtado", 42, 1, 111, 500)
    print(b.agencias)
    print(b.numero_contas)
    print(b.clientes, len(b.clientes))
