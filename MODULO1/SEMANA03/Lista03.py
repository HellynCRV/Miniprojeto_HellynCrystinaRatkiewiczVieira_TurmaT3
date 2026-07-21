#1. Leia um array A com N elementos e escreva um array B, com os mesmos elementos de A, sendo que estes deverão estar invertidos, ou seja, o 1º elemento de A deve ser o último elemento de B; o 2º elemento de A deve ser o penúltimo elemento de B e assim por diante.
#array_a = [1, 2, 3, 4, 5]
#array_b = array_a[::-1]
#print(array_b)

#2. Leia um array A com N elementos, verifique e escreva se existem ou não elementos iguais no array.
#array_a = [1, 2, 3, 4, 5, 5]
#array_b = set(array_a)
#print(len(array_a) != len(array_b))

#3. Leia 2 arrays A e B com N elementos, escreva um array C, sendo este a junção dos arrays A e B. Desta forma, o array C deverá ter 2*N elementos.
#array_a = [1, 2, 3, 4, 5]
#array_b = [6, 7, 8, 9, 10]
#array_c = array_a + array_b
#print(array_c)

#4. Leia 2 arrays A e B com N elementos, escreva um array C, que represente o conjunto união entre os arrays A e B; e um array D, que represente o conjunto interseção entre os arrays A e B.
#array_a = [1, 2, 3, 4, 5]
#array_b = [4, 5, 6, 7, 8]
#array_c = list(set(array_a) | set(array_b))  # União
#array_d = list(set(array_a) & set(array_b))  # Interseção
#print("União:", array_c)
#print("Interseção:", array_d)

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
  