import abc


class Conta:
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo
        self._extrato = []
        if isinstance(saldo, (int, float)) and saldo >= 0:
            self._extrato.append(saldo)
            return
        print(f"Saldo digitado está incorreto: {saldo}")

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, numero_conta):
        self._numero_conta = numero_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def deposito(self, valor):
        if isinstance(valor, (float, int)) and valor > 0:
            self._saldo += valor
            self._extrato.append(valor)
            print(f"Depósito de R${valor} realizado! Seu saldo é: R${self._saldo}")
        else:
            print(f"Valor digitado ({valor}) não é um número válido")
            return

    def extrato(self):
        print("Extrato:", end="\n")
        print(f"Saldo anterior: R${self._extrato[0]}", end="\n")
        for mov in self._extrato[1:]:
            if mov > 0:
                print(f"Depósito: R${mov}")
            elif mov + 1 < 0:
                print(f"Saque: R${mov}")
        print(f"Saldo atual: R${self._saldo}")

    @abc.abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite):
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def sacar(self, valor):
        if isinstance(valor, (float, int)) and valor > 0:
            if self._saldo + self._limite >= valor:
                self._saldo -= valor
                self._extrato.append(-valor)
                print(f"Saque de R${valor} realizado. Seu saldo é: R${self._saldo}")
            else:
                print(f"Saldo insuficiente: R${self._saldo}. Limite: R${self._limite}")
        else:
            print(f"Valor digitado ({valor}) não é um número válido")
            return


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor):
        if isinstance(valor, (float, int)) and valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                self._extrato.append(-valor)
                print(f"Saque de R${valor} realizado. Seu saldo é: R${self._saldo}")
            else:
                print(f"Saldo insuficiente: R${self._saldo}.")
        else:
            print(f"Valor digitado ({valor}) não é um número válido")
            return


if __name__ == "__main__":
    ## TESTE CONTA ##
    # c = Conta(1, 123, 0)
    # c.deposito(100)

    ## TESTE CONTA CORRENTE ##

    # cc = ContaCorrente(1, 123, 200, 500)
    # cc.deposito(100)
    # cc.sacar(100)
    # cc.sacar(200)
    # cc.sacar(500)
    # cc.extrato()

    ## TESTE CONTA POUPANÇA ##

    # cp = ContaPoupanca(1, 123, 500)
    # cp.deposito(500)
    # cp.sacar(800)
    # cp.extrato()
