"""1. Crie uma lista com os números de 1 a 10 e use um loop 
para imprimir cada número elevado ao quadrado."""

lista_num: list = []
lista_num.extend(range(1,11))

for i in lista_num:
    print(i**2)

"""2. Dada a lista ["Python", "Java", "C++", "JavaScript"], 
remova o item "C++" e adicione "Ruby"."""

lista_linguagem: list = ["Python", "Java", "C++", "JavaScript"]

lista_linguagem.remove('C++')
lista_linguagem.append('Ruby')

print(lista_linguagem)

"""3. Crie um dicionário para armazenar informações de um livro, 
incluindo título, autor e ano de publicação. Imprima cada informação."""

livros_dict: dict = {
    'titulo': 'os miseraveis',
    'autor': 'victor hugo',
    'ano_publicacao': 1862 
    }

for i,ii in livros_dict.items():
    print(f'{i}: {ii}')

"""4. Escreva um programa que conta o número de ocorrências 
de cada caractere em uma string usando um dicionário."""

palavra: str = 'trabalha'
letras: dict = {}

for i in palavra:
    print(i)
    print(letras)
    if i in letras:
        letras[i] += 1
    else:
        letras.update({i:1})
    print(letras)

"""5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, 
"banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras."""

frutas: list = ["maçã", "banana", "cereja"]
tabela_precos: dict = {"maçã": 0.45, 
"banana": 0.30, "cereja": 0.65}

valor_final: float = 0.0

for i in frutas:
    valor_final = valor_final + tabela_precos[i]
    print(valor_final)