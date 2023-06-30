from conta import Conta


class Pessoas:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self.idade = idade


class Cliente(Pessoas):

    # conta = Conta()
    def __init__(self, nome: str, idade: int, conta: Conta):
        super().__init__(nome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta: Conta):
        self._conta = conta


if __name__ == "__main__":
    p = Pessoas("Tellyhoe", 18)
    print(f"Nome: {p.nome}, idade = {p.idade}")
