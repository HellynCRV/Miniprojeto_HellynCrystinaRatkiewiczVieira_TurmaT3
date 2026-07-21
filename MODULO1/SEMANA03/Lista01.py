#LISTA 1:
#1. Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)
#velocidade_ms = float(input("Digite a velocidade em m/s: "))
#velocidade_kmh = velocidade_ms * 3.6
#print("Velocidade em km/h:", velocidade_kmh)

#2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.
#horas = int(input("Digite o valor em horas: "))
#minutos = int(input("Digite o valor em minutos: "))
#total_minutos = horas * 60 + minutos
#print("Total em minutos:", total_minutos)

#3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.
#minutos_totais = int(input("Digite o valor em minutos: "))
#horas = minutos_totais // 60
#minutos_restantes = minutos_totais % 60
#print("Equivalente em horas e minutos:", horas, "horas e", minutos_restantes, "minutos")

#4. Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).

#recebendo do usuário
#valor_do_dolar = float(input("Digite o valor do dólar:"))
#valor_em_dolar = float(input("Digite o valor em dólares:"))

#processamento
#converter_real = (valor_do_dolar * valor_em_dolar)

#output
#print(f"O valor em reais é: {converter_real}")

#5. Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).

#recebendo do usuário
#numero_inteiro = int(input("Digite um número inteiro de 3 dígitos:"))

#processamento
#c = numero_inteiro // 100
#d = (numero_inteiro // 10) % 10
#u = numero_inteiro % 10
#soma = c + d + u

#output
#print(f"A soma dos elementos é: {soma}")

#6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

#velocidade_km_h = float(input("Digite a velocidade em km/h:"))

#velocidade_m_s = velocidade_km_h / 3.6

#print(f"A velocidade em m/s é: {velocidade_m_s:.2f}")

#7. Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.

#a = int(input("Digite o primeiro número:"))
#b = int(input("Digite o segundo número:"))
#c = int(input("Digite o terceiro número:"))

#soma_a_b = (a + b)
#diferenca_b_c = (b - c)

#print (f"A soma dos dois primeiros núumeros é: {soma_a_b}")
#print (f"A diferença dos dois últimos números é: {diferenca_b_c}")

#8. Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

#a = int(input ("Digite o primeiro número:"))
#b = int(input("Digite o segundo número:"))

#calculo = (a + b) / (a - b)

#print( f"A divisão da soma pela subtração dos números digitados é: {calculo}")

#9. Leia 2 números (A, B) e escreva-os em ordem inversa (B, A).

#a = int(input ("Digite o primeiro número:"))
#b = int(input("Digite o segundo número:"))

#print (f"Os números na ordem inversa é: {b} e {a}")

#10. Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1º pelo 2º.

#a = int(input ("Digite o primeiro número:"))
#b = int(input("Digite o segundo número:"))

#quociente = a // b
#resto = a % b

#print (f"O quociente da divisão é: {quociente}")
#print (f"O resto da divisão é: {resto}")

#11. Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)
#numero_inteiro = int(input("Digite um número inteiro de 3 dígitos:"))
#numero_inverso = (numero_inteiro % 10) * 100 + ((numero_inteiro // 10) % 10) * 10 + (numero_inteiro // 100)
#print(f"O inverso do número é: {numero_inverso}")

#12. Leia o salário de um trabalhador e escreva seu novo salário com um aumento de 25%.
#salario_atual = float(input("Digite o salário atual: "))
#salario_aumento = ((salario_atual * 0.25) + (salario_atual))
#print(f"O salrário com aumento de 25% é:  {salario_aumento}")

#13. Leia um valor em real (R$), calcule e escreva 70% deste valor.
#valor = float(input("Digite um valor em R$: "))
#valor_atual = (valor*0.70)
#print(f"O valor equivalente a 70% do valor digitado é: {valor_atual}")

#14. Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.
#nota1 = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))
#nota3 = float(input("Digite a terceira nota: "))
#peso1 = float(input("Digite o peso da primeira nota: "))
#peso2 = float(input("Digite o peso da segunda nota: "))
#peso3 = float(input("Digite o peso da terceira nota: "))
#media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
#print(f"A média ponderada é: {media_ponderada}")

#USANDO O LOOP FOR
#soma_notas_pesos = 0
#soma_pesos = 0

# O loop vai rodar 3 vezes (para i = 1, 2 e 3)
#for i in range(1, 4):
    #nota = float(input(f"Digite a {i}ª nota: "))
    #peso = float(input(f"Digite o peso da {i}ª nota: "))
    
    #soma_notas_pesos += nota * peso
    #soma_pesos += peso

#media_ponderada = soma_notas_pesos / soma_pesos

#print(f"A média ponderada é: {media_ponderada:.2f}")

#15. Leia o valor da base e altura de um triângulo, calcule e escreva sua área. (área=(base * altura)/2)
#base = float(input("Digite a medida da base: "))
#altura = float(input("Digite a medida da altura: "))
#area = ((base * altura)/2)
#print(f"A área é: {area}")

#16. Leia o valor do lado de um quadrado, calcule e escreva sua área. (área = lado2)
#lado = float(input("Digite a medida do lado: "))
#area = (lado * lado)
#print(f"A área é: {area}")

#17. Leia o valor da base e altura de um retângulo, calcule e escreva sua área. (área = base * altura)
#base = float(input("Digite a medida da base: "))
#altura = float(input("Digite a medida da altura: "))
#area = (base * altura)
#print(f"A área é: {area}")

#18. Leia o valor do raio de uma circunferência, calcule e escreva seu comprimento.(c = 2 * p * r)
#raio = float(input("Digite a medida do raio: "))
#pi = 3.14
#comprimento = (2 * pi * raio)
#print(f"O comprimento é: {comprimento}")

#19. Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3) / 3) (p = 3,14)
#raio = float(input("Digite a medida do raio: "))
#pi = 3.14
#volume = ((4 * pi * (raio ** 3)) / 3)
#print(f"O volume é: {volume}")

#20. Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)
#temperatura_c = float(input("Digite a temperatura em °C: "))
#temperatura_f = ((9 * temperatura_c + 160) / 5)
#print(f"A temperatura em °F é: {temperatura_f}")

#21. Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).
#temperatura_f = float(input("Digite a temperatura em °F: "))
#temperatura_c = ((5 * temperatura_f - 160) / 9)
#print(f"A temperatura em °C é: {temperatura_c}")

#22. Leia um valor em km, calcule e escreva o equivalente em m.
#km = float(input("Digite a medida em km: "))
#m = (km * 1000)
#print(f"A medida em m é: {m}")

#23. Leia um valor em kg (quilograma), calcule e escreva o equivalente em g (grama).
#kg = float(input("Digite a medida em kg: "))
#g = (kg * 1000)
#print(f"A medida em g é: {g}")

#24. Leia um valor em m, calcule e escreva o equivalente em cm.
#m = float(input("Digite a medida em m: "))
#cm = (m * 100)
#print(f"A medida em cm é: {cm}")

#25. Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.
#metros = int(input("Digite o número de metros: "))
#km = metros // 1000
#m = metros % 1000
#print(f"{km} Km e {m} m")

#26. Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.
#dias = int(input("Digite a quantidade de dias: "))
#semanas = (dias // 7)
#dias_restantes = (dias % 7)
#print(f"Semanas: {semanas}")
#print(f"Dias: {dias_restantes}")

#27. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.
#segundos = int(input("Digite a quantidade de segundos: "))
#horas = (segundos // 3600)
#minutos = ((segundos % 3600) // 60)
#segundos_restantes = ((segundos % 3600) % 60)
#print(f"Horas: {horas}")
#print(f"Minutos: {minutos}")
#print(f"Segundos: {segundos_restantes}")

#28. Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.
#horas = int(input("Digite a quantidade de horas: "))
#semanas = (horas // 168)
#dias = ((horas % 168) // 24)
#horas_restantes = ((horas % 168) % 24)
#print(f"Semanas: {semanas}")
#print(f"Dias: {dias}")
#print(f"Horas: {horas_restantes}")

#29. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.
#meses = int(input("Digite a quantidade de meses: "))
#anos = (meses // 12)
#meses_restantes = (meses % 12)
#print(f"Anos: {anos}")
#print(f"Meses: {meses_restantes}")

#31. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.
#binario = input("Digite um número binário de 4 dígitos: ")
#decimal = int(binario, 2)
#print(f"O equivalente na base decimal é: {decimal}")

#32. Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.  
#numero_inteiro = int(input("Digite um número inteiro de 3 dígitos: "))
#numero_inverso = (numero_inteiro % 10) * 100 + ((numero_inteiro // 10) % 10) * 10 + (numero_inteiro // 100)
#diferenca = numero_inteiro - numero_inverso
#print(f"A diferença entre o número e seu inverso é: {diferenca}")

#33. Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso. (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).
#numero_inteiro = int(input("Digite um número inteiro de 3 dígitos: "))
#numero_inverso = (numero_inteiro % 10) * 100 + ((numero_inteiro // 10) % 10) * 10 + (numero_inteiro // 100)
#soma = numero_inteiro + numero_inverso
#print(f"A soma do número com seu inverso é: {soma}")

#34. Leia 3 números, calcule e escreva a média dos números.
#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))
#numero3 = float(input("Digite o terceiro número: "))
#media = (numero1 + numero2 + numero3) / 3
#print(f"A média dos números é: {media}")

#35. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.: número = 9534 ; soma = 9+5+3+4 = 21.
#numero_inteiro = int(input("Digite um número inteiro de 4 dígitos: "))
#soma = (numero_inteiro // 1000) + ((numero_inteiro // 100) % 10) + ((numero_inteiro // 10) % 10) + (numero_inteiro % 10)
#print(f"A soma dos elementos é: {soma}")

#36. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.
#anos = int(input("Digite a idade em anos: "))
#meses = int(input("Digite a idade em meses: "))
#dias = int(input("Digite a idade em dias: "))
#dias_totais = (anos * 365) + (meses * 30) + dias
#print(f"A idade em dias é: {dias_totais}")

#37. Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.
#dias = int(input("Digite a idade em dias: "))
#anos = (dias // 365)
#meses = ((dias % 365) // 30)
#dias_restantes = ((dias % 365) % 30)
#print(f"Anos: {anos}")
#print(f"Meses: {meses}")
#print(f"Dias: {dias_restantes}")

#38. Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.
#fracao1_numerador = int(input("Digite o numerador da primeira fração: "))
#fracao1_denominador = int(input("Digite o denominador da primeira fração: "))
#fracao2_numerador = int(input("Digite o numerador da segunda fração: "))
#fracao2_denominador = int(input("Digite o denominador da segunda fração: "))
#soma_numerador = (fracao1_numerador * fracao2_denominador) + (fracao2_numerador * fracao1_denominador)
#soma_denominador = (fracao1_denominador * fracao2_denominador)
#print(f"O resultado da soma das frações é: {soma_numerador}/{soma_denominador}")

#39. Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:
#A = int(input("Digite o valor de A: "))
#B = int(input("Digite o valor de B: "))
#C = int(input("Digite o valor de C: "))

#R = (A + B) ** 2    
#S = (B + C) ** 2
#D = (R + S)/2
#print(f"O valor de D é: {D}")

#40. Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele fuma, o nº de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).
#Anos_fumando = int(input("Digite o número de anos que você fuma: "))
#Cigarros_por_dia = int(input("Digite o número de cigarros fumados por dia: "))
#Preco_carteira = float(input("Digite o preço de uma carteira de cigarros: "))

# Cálculo da quantidade de dinheiro gasta por um fumante
#total_cigarros = Anos_fumando * 365 * Cigarros_por_dia
#total_carteiras = total_cigarros / 20
#dinheiro_gasto = total_carteiras * Preco_carteira
#print(f"A quantidade de dinheiro gasta por você é: R$ {dinheiro_gasto:.2f}")



