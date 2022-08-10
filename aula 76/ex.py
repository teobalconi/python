lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

lista_soma = zip(lista_a,lista_b)


# Método 1
soma = []
for a,b in lista_soma:
    soma.append(a+b)

print(f'Método 1: {soma}')

# Método 2

lista_soma_2 = [a+b for (a,b) in zip(lista_a,lista_b)]

print(f'Método 2 (lis comprehension): {lista_soma_2}')