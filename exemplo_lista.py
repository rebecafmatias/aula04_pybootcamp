produto_01: str = 'sapato'
produto_02: str = 'camisa'
produto_03: str = 'bolsa'

lista_produtos: list = []

print(lista_produtos)

lista_produtos.append(produto_01)
lista_produtos.append(produto_02)
lista_produtos.append(produto_03)

print(lista_produtos)

lista_produtos.pop() #remove o último objeto adicionado (maior performance do que remove)

print(lista_produtos)