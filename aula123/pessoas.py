from conta import Conta

class Pessoas:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

class Cliente(Pessoas):
    def __init__(self, conta.Conta):


if __name__ == "__main__":
    p = Pessoas("Tellyhoe",18)
    print(f"Nome: {p.nome}, idade = {p.idade}")