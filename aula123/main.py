import banco

banco = banco.Banco
c1 = banco.criar_conta_corrente("Celso Furtado", 42, 1, 111, 500, 200)

banco.deposito(c1, 100)
banco.sacar(c1, 500)
banco.sacar(c1, 200)
