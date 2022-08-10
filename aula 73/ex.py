carrinho = []

carrinho.append(("Produto 1", 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = sum([float(valor) for produto,valor  in carrinho])
print(total)