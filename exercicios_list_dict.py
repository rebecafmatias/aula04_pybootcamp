# """1. Crie uma lista com os números de 1 a 10 e use um loop 
# para imprimir cada número elevado ao quadrado."""

# lista_num: list = []
# lista_num.extend(range(1,11))

# for i in lista_num:
#     print(i**2)

# """2. Dada a lista ["Python", "Java", "C++", "JavaScript"], 
# remova o item "C++" e adicione "Ruby"."""

# lista_linguagem: list = ["Python", "Java", "C++", "JavaScript"]

# lista_linguagem.remove('C++')
# lista_linguagem.append('Ruby')

# print(lista_linguagem)

# """3. Crie um dicionário para armazenar informações de um livro, 
# incluindo título, autor e ano de publicação. Imprima cada informação."""

# livros_dict: dict = {
#     'titulo': 'os miseraveis',
#     'autor': 'victor hugo',
#     'ano_publicacao': 1862 
#     }

# for i,ii in livros_dict.items():
#     print(f'{i}: {ii}')

# """4. Escreva um programa que conta o número de ocorrências 
# de cada caractere em uma string usando um dicionário."""

# palavra: str = 'trabalha'
# letras: dict = {}

# for i in palavra:
#     print(i)
#     print(letras)
#     if i in letras:
#         letras[i] += 1
#     else:
#         letras.update({i:1})
#     print(letras)

# """5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, 
# "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras."""

# frutas: list = ["maçã", "banana", "cereja"]
# tabela_precos: dict = {"maçã": 0.45, 
# "banana": 0.30, "cereja": 0.65}

# valor_final: float = 0.0

# for i in frutas:
#     valor_final = valor_final + tabela_precos[i]
#     print(valor_final)


"""6. Eliminação de Duplicatas
Objetivo: Dada uma lista de emails, remover todos os duplicados."""

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

# emails_unico = list(set(emails))

# print(emails_unico)

"""7. Filtragem de Dados
Objetivo: Dada uma lista de idades, filtrar apenas aquelas que 
são maiores ou iguais a 18."""

# idades_list: list = [29,17,25,36,10,19,18,45]

# maior_de_idade: list = []

# for i in idades_list:
#     if i >= 18:
#         maior_de_idade.append(i)
#     print(maior_de_idade)

# print(maior_de_idade)

"""8. Ordenação Personalizada
Objetivo: Dada uma lista de dicionários representando pessoas, 
ordená-las pelo nome."""

# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]

# pessoas_sorted = pessoas.copy()
# pessoas_sorted.sort(key=lambda pessoa: pessoa['nome'])

"""9. Agregação de Dados
Objetivo: Dado um conjunto de números, calcular a média."""

# numeros = [10, 20, 30, 40, 50]

# media = sum(numeros)/len(numeros)

"""10. Divisão de Dados em Grupos
Objetivo: Dada uma lista de valores, dividir em duas listas: 
uma para valores pares e outra para ímpares."""

# lista_numeros = [1,2,3,4,5,6,7,8,9,10]
# pares = []
# impares = []

# for i in lista_numeros:
#     if i%2 == 0:
#         pares.append(i)
#     else:
#         impares.append(i)
#     print(f'\nnumero iterado: {i}')
#     print(f'lista de pares: {pares}')
#     print(f'lista de impares: {impares}')


"""11. Atualização de Dados
Objetivo: Dada uma lista de dicionários representando produtos, 
atualizar o preço de um produto específico."""

# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# for i in produtos:
#     if i['id'] == 3:
#         i['preço'] = 250

# print(produtos)

"""12. Fusão de Dicionários
Objetivo: Dados dois dicionários, fundi-los em um único dicionário."""

# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# dicionario_final = {**dicionario1, **dicionario2}

# print(dicionario_final)

"""13. Filtragem de Dados em Dicionário
Objetivo: Dado um dicionário de estoque de produtos, 
filtrar aqueles com quantidade maior que 0."""

# estoque = {'bolsa': 10, 'cinto': 20, 'casaco': 5, 'calca': 0}
# estoque_positivo = {}

# for i,ii in estoque.items():
#     estoque_positivo.update({i:ii})
#     print(estoque_positivo)

"""14. Extração de Chaves e Valores
Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores."""

# dicionario = {"a": 1, "b": 2, "c": 3}
# chaves = list(dicionario.keys())
# valores = list(dicionario.values())

# print("Chaves:", chaves)
# print("Valores:", valores)

"""15. Contagem de Frequência de Itens
Objetivo: Dada uma string, contar a frequência de 
cada caractere usando um dicionário."""

texto = 'Eu amo meu cachorro'
string_texto = texto.replace(' ', '').lower()

frequencia = {}

for i in string_texto:
    if i not in frequencia:
        frequencia.update({i:1})
    else:
        frequencia[i] += 1
    print(frequencia)


