import csv

file_path: str = "exemplo.csv"

dados_csv: list = []

with open(file = file_path,mode = 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for i in leitor_csv:
        dados_csv.append(i)
        print(dados_csv)
        
print(dados_csv)