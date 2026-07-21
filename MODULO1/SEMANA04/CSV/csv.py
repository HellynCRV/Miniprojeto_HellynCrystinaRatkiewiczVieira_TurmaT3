dados = [
    ['Produto', 'Preço', 'Estoque'],
    ['notebook', 2500.00, 10],
    ['mouse', 50.00, 100],
    ['teclado', 150.00, 50],
    ['monitor', 800.00, 5]
]
import csv

with open ('produtos.csv', mode='r', encoding='utf-8') as arq:
    conteudo_bruto = arq.read()
    print(conteudo_bruto)
    print(type(conteudo_bruto))
