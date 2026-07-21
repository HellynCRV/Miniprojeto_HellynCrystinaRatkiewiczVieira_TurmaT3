dados = [
    ['Produto', 'Preço', 'Estoque'],
    ['Notebook', 4500.00, 10],
    ['Smartphone', 2500.00, 20],
    ['Tablet', 1500.00, 15],
    ['Monitor', 800.00, 5]
]

import csv
with open('produtos.csv', 'w') as arquivo_produtos:
    escritor = csv.writer(arquivo_produtos)
    escritor.writerows(dados)
print("PRINT COM CSV READER")
with open('produtos.csv', 'r') as arquivo_produtos:
    escritor = csv.reader(arquivo_produtos)
    for linha in escritor:
        print(type(linha))

print("\nPRINT COM OPEN READ()")
with open('produtos.csv', 'r') as arquivo_produtos:
    escritor = arquivo_produtos.read()
    print(type(escritor))