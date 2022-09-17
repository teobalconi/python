from conta import ContaCorrente, ContaPoupanca
from pessoas import Cliente


class Banco:
    conta = None
    agencias = []
    numero_contas = []
    clientes = []

    @classmethod
    def validacao(cls, cliente):
        dados_cliente = {"nome": cliente.nome, "idade": cliente.idade}
        if cliente.conta.numero_conta in cls.numero_contas and cliente.conta.agencia in cls.agencias:
            for n in cls.clientes:
                if dados_cliente in dict(n).values():
                    return True
                else:
                    return False

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

    @classmethod
    def deposito(cls, cliente, valor):
        if cls.validacao(cliente):
            cliente.conta.deposito(valor)

    @classmethod
    def sacar(cls, cliente, valor):
        if cls.validacao(cliente):
            cliente.conta.sacar(valor)


if __name__ == "__main__":
    b = Banco()
    c1 = b.criar_conta("Celso Furtado", 42, 1, 111, 500)
    print(b.agencias)
    print(b.numero_contas)
    print(b.clientes, len(b.clientes))
