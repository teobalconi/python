from random import randint

cpf = str(randint(100000000,999999999))

# Verificação Dígito 1
soma1 = 0
for i, k in enumerate(range(10, 1, -1)):
    soma1 += (int(cpf[i])*k)

conta1 = (11 - (soma1 % 11))
digito1 = 0 if conta1 > 9 else conta1

# Verificação Dígito 2
cpf += str(digito1)
soma2 = 0
for i, k in enumerate(range(11, 1, -1)):
    soma2 += (int(cpf[i])*k)

conta2 = (11 - (soma2 % 11))
digito2 = 0 if conta2 > 9 else conta2
cpf += str(digito2)

print(f"O CPF é: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]} ")

