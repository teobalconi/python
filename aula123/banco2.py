from conta import ContaCorrente, ContaPoupanca
from pessoas import Cliente


class Banco:
    conta = None
    agencias = []
    numero_contas = []
    clientes = []

    @classmethod
    def criar_conta(cls, nome, idade, agencia, numero_conta, saldo, limite=None):
        cliente = {"c" + str(len(cls.clientes) + 1): dict(nome=nome, idade=idade)}

        if limite and limite > 0:
            cls.conta = ContaCorrente(agencia, numero_conta, saldo, limite)
        else:
            cls.conta = ContaPoupanca(agencia, numero_conta, saldo)

        cls.agencias.append(agencia)
        cls.numero_contas.append(numero_conta)
        cls.clientes.append(cliente)

        return Cliente(nome, idade, cls.conta)


if __name__ == "__main__":
    b = Banco()
    c1 = b.criar_conta("Celso Furtado", 42, 1, 111, 500)
    print(b.agencias)
    print(b.numero_contas)
    print(b.clientes, len(b.clientes))
