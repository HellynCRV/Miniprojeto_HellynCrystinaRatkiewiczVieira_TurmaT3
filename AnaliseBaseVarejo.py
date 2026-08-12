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

# 1. Drop de Colunas:Removendo as colunas 'Unnamed' que vieram vazias
colunas_vazias = ['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13']
df = df.drop(columns=colunas_vazias)

# 2. Sprint 2 - Padronização de Texto: Removendo espaços e caixa alta
df['PR_CAT'] = df['PR_CAT'].str.strip().str.upper()
df['PR_NOME'] = df['PR_NOME'].str.strip().str.upper()

# 3. Sprint 3 - Tratamento de Nulos com Condicionais (if/else)
# Loop para preencher categorias vazias com "Sem Categoria" conforme o critério
categorias_ajustadas = []
for item in df['PR_CAT']:
    if item == "" or item == "NAN" or item == "NONE":
        categorias_ajustadas.append("Sem Categoria")
    else:
        categorias_ajustadas.append(item)
df['PR_CAT'] = categorias_ajustadas

# 4. Sprint 3 - Padronização de Datas: Convertendo a string para data
# Usando errors='coerce' conforme ensinado para tratar anomalias temporais
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')

# 5. Tratamento de Duplicatas: Removendo linhas redundantes na base
df = df.drop_duplicates()

print("--- DIAGNÓSTICO DA BASE LIMPA ---")
df.info()