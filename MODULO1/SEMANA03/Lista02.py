#1. Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 == num2 == num3:
    print("Os três números são iguais.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Dois números são iguais.")
else:
    print("Todos os números são diferentes.")

#2. Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print("O maior número é:", num1)
    print("O menor número é:", num2)
elif num2 > num1:
    print("O maior número é:", num2)
    print("O menor número é:", num1)
else:
    print("Os dois números são iguais.")

#3. Leia 3 (três) números, verifique e escreva o maior entre os números lidos.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
    print("O maior número é:", num1)
elif num2 > num1 and num2 > num3:
    print("O maior número é:", num2)
elif num3 > num1 and num3 > num2:
        print("O maior número é:", num3)
else:
  print("Os números são iguais.")

#4. Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente do algarismo da unidade.
num = int(input("Digite um número de 2 dígitos: "))
dezena = num // 10
unidade = num % 10
if dezena == unidade:
    print("O algarismo da dezena é igual ao algarismo da unidade.")
else:
    print("O algarismo da dezena é diferente do algarismo da unidade.")

#5. Leia 3 (três) números e escreva-os em ordem crescente.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 <= num2 <= num3:
    print(num1, num2, num3)
elif num1 <= num3 <= num2:
    print(num1, num3, num2)
elif num2 <= num1 <= num3:
        print(num2, num1, num3)
elif num2 <= num3 <= num1:
        print(num2, num3, num1)
elif num3 <= num1 <= num2:
            print(num3, num1, num2)
elif num3 <= num2 <= num1:
            print(num3, num2, num1)

#6. Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180 º). Se formam, verifique se formam um triângulo acutângulo (3 ângulos < 90º), retângulo (1 ângulo = 90º) ou obtusângulo (1 ângulo > 90º). Não existe ângulo com tamanho 0º (zero grau).
angulo1 = int(input("Digite o primeiro ângulo: "))
angulo2 = int(input("Digite o segundo ângulo: "))
angulo3 = int(input("Digite o terceiro ângulo: "))
if angulo1 + angulo2 + angulo3 == 180:
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
      print("É um triângulo acutângulo.")
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("É um triângulo retângulo.")
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
          print("É um triângulo obtusângulo.")
    else:
            print("Não é um triângulo.") 
#7. Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3 (três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).
lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("É um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não é um triângulo.")

#8. Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva sua idade exata (em anos).
dia_atual = int(input("Digite o dia atual: "))
mes_atual = int(input("Digite o mês atual: "))  
ano_atual = int(input("Digite o ano atual: "))
dia_nascimento = int(input("Digite o dia de nascimento: "))
mes_nascimento = int(input("Digite o mês de nascimento: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento
if mes_atual < mes_nascimento or (mes_atual == mes_nascimento and dia_atual < dia_nascimento):
    idade -= 1
print(f"A idade exata é: {idade} anos.")

#11. Leia 1 (um) número inteiro e esc reva se este número é par ou ímpar.
num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#12. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))
if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    maior = num1
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    maior = num2
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    maior = num3
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    maior = num4
else:
    maior = num5

if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
    menor = num1
elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
    menor = num2
elif(num3 < num1 and(num3 <	num2) and(num3 <	num4) and(num3 <	num5)):
    menor =	num3
elif(num4 <	num1) and(num4 <	num2) and(num4 <	num3) and(num4 <	num5):
    menor =	num4
else:
    menor =	num5

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")