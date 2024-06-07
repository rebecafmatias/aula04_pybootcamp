import json

produto_01: dict = {
    'nome': 'sapato',
    'quantidade': 39,
    'preco': 10.50,
    'disponibilidade': True
}

produto_02: dict = {
    'nome': 'bolsa',
    'quantidade': 20,
    'preco': 9.30,
    'disponibilidade': True
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

# print(carrinho)

carrinho_json = json.dumps(carrinho)

print(carrinho_json)