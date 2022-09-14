from conta import ContaCorrente, ContaPoupanca
from pessoas import Cliente

cc = ContaCorrente(1,111,500,100)
c1 = Cliente("Celso Furtado", 45, cc)


print(c1.conta.limite)
c1.conta.sacar(600)