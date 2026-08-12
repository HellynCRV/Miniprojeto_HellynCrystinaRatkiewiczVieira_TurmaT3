# ==========================================
# SPRINT 1: IMPORTAÇÃO E EXPLORAÇÃO INICIAL
# ==========================================

import pandas as pd
import numpy as np

# Carregando a base de dados com o separador correto (ponto e vírgula)
df = pd.read_csv("Base Varejo.csv", sep=";")

# Visualizando as primeiras linhas para entender a estrutura dos dados
print("Primeiras linhas do dataset:")
print(df.head())

# Verificando informações gerais: quantidade de registros, colunas e tipos de dados
print("\nInformações gerais sobre a base de dados:")
df.info()


# =====================================================================
# SPRINT 2 & 3: TRANSFORMAÇÃO DE TIPOS E TRATAMENTO DE NULOS
# =====================================================================

# Tratamento de nulos das dimensões físicas
# Justificativa técnica: As colunas extras 'Unnamed' apresentam 100% de valores ausentes (nulos).
# Optou-se pela exclusão de colunas (Trimming), pois não possuem relevância para as regras de negócio.
colunas_vazias = ['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13']
df = df.drop(columns=colunas_vazias, errors='ignore')  # errors='ignore' evita erros caso as colunas não existam

# SPRINT 2: Padronização de Texto
df['PR_CAT'] = df['PR_CAT'].str.strip().str.upper()
df['PR_NOME'] = df['PR_NOME'].str.strip().str.upper()

# Lógica condicional (if/else) para preencher categorias vazias
# Garante que campos em branco ou strings ruidosas sejam mapeados uniformemente
categorias_ajustadas = []
for item in df['PR_CAT']:
    if item == "" or item == "NAN" or item == "NONE":
        categorias_ajustadas.append("Sem Categoria")
    else:
        categorias_ajustadas.append(item)
df['PR_CAT'] = categorias_ajustadas

# Conversão de string de data utilizando o módulo datetime
# O parâmetro errors='coerce' é empregado para mitigar eventuais inconsistências de datas
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')

# Validação da regra do identificador de número de compra (CO_ID)
# Remoção de duplicatas idênticas para preservar a unicidade de cada transação estruturada
df = df.drop_duplicates()

print("--- DIAGNÓSTICO DA BASE LIMPA ---")
df.info()
