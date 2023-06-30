from conta import ContaCorrente, ContaPoupanca
from pessoas import Cliente


class Banco:
    conta = None
    agencias = []
    numero_contas = []
    clientes = []

    @classmethod
    def validacao(cls, cliente: Cliente) -> bool:
        dados_cliente = {"nome": cliente.nome, "idade": cliente.idade}
        if cliente.conta.numero_conta in cls.numero_contas and cliente.conta.agencia in cls.agencias:
            for n in cls.clientes:
                if dados_cliente in dict(n).values():
                    return True
                else:
                    return False

    @classmethod
    def criar_conta_corrente(cls, nome: str, idade: int, agencia: int, numero_conta: int, saldo: float = 0, limite: float = 0) -> Cliente:
        cliente = {"c" + str(len(cls.clientes) + 1): dict(nome=nome, idade=idade)}

        # if limite and limite >= 0:
        if limite >= 0:
            cls.conta = ContaCorrente(agencia, numero_conta, saldo, limite)
        else:
            print('O limite deve ser maior ou igual a zero!')
            pass

        cls.agencias.append(agencia)
        cls.numero_contas.append(numero_conta)
        cls.clientes.append(cliente)

        return Cliente(nome, idade, cls.conta)

    @classmethod
    def criar_conta_poupanca(cls, nome: str, idade: int, agencia: int, numero_conta: int, saldo: float = 0) -> Cliente:
        cliente = {"c" + str(len(cls.clientes) + 1): dict(nome=nome, idade=idade)}

        cls.conta = ContaPoupanca(agencia, numero_conta, saldo)
        cls.agencias.append(agencia)
        cls.numero_contas.append(numero_conta)
        cls.clientes.append(cliente)

        return Cliente(nome, idade, cls.conta)

    @classmethod
    def deposito(cls, cliente: Cliente, valor: float):
        if cls.validacao(cliente):
            cliente.conta.deposito(valor)

    @classmethod
    def sacar(cls, cliente: Cliente, valor: float):
        if cls.validacao(cliente):
            cliente.conta.sacar(valor)


if __name__ == "__main__":
    b = Banco()
    c1 = b.criar_conta_corrente("Celso Furtado", 42, 1, 111, 100, -100)
    c2 = b.criar_conta_poupanca("Tony Hawk", 42, 2, 222, 500)
    print(b.agencias)
    print(b.numero_contas)
    print(b.clientes, len(b.clientes))
