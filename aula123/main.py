import banco2

b = banco2.Banco
c1 = b.criar_conta("Celso Furtado", 42, 1, 111, 500)

print(c1.conta.saldo)
print(c1.conta.numero_conta, c1.conta.agencia)
print(b.clientes)
print(b.agencias)
print(b.numero_contas)
