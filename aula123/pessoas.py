class Pessoas:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoas):

    # conta = Conta()
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta


if __name__ == "__main__":
    p = Pessoas("Tellyhoe", 18)
    print(f"Nome: {p.nome}, idade = {p.idade}")
