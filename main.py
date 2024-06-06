"""Type Hint"""

idade: int = 30
altura: float = 1.78
nome: str = 'Rebeca'
is_estudante: bool = True

"""Refatorando código aula 03"""

nome_completo: str = input('Digite seu nome completo: ')
nome_final: list = nome_completo.split()

idade_valida: bool = False
salario_valido: bool = False


while len(nome) <= 1:
    nome_completo = input('Você digitou um valor inválido. \nInforme seu nome completo (nome + sobrenome): ')
    nome_final = nome_completo.split()

while idade_valida == False:
    try:
        idade_: int = int(input('Digite sua idade: ').strip())
        idade_valida = True
    except ValueError:
        print('Você digitou um valor inválido, tente novamente. \nExemplo idade: 25')
        idade_valida = False

while salario_valido == False:
    try:
        salario_: float = float(input('Digite seu salário: ').strip())
        salario_valido = True
    except ValueError:
        print('Você digitou um valor inválido, tente novamente. \nExemplo salário: 1580.50')
        salario_valido = False
