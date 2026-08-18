
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

# ==========================================
# SPRINT 2: TRANSFORMAÇÃO E PADRONIZAÇÃO
# ==========================================

# Padronização dos textos das colunas de categoria e nome do produto
df['PR_CAT'] = df['PR_CAT'].str.strip().str.upper()
df['PR_NOME'] = df['PR_NOME'].str.strip().str.upper()

# Conversão da coluna DATA para o formato datetime
# Valores que não puderem ser convertidos serão considerados NaT
df['DATA'] = pd.to_datetime(
    df['DATA'],
    format='%d/%m/%Y',
    errors='coerce'
)

print("\n--- TIPOS DE DADOS APÓS A TRANSFORMAÇÃO ---")
print(df.dtypes)


# ==========================================
# SPRINT 3: LIMPEZA DE NULOS E DUPLICATAS
# ==========================================

print("\n--- DIAGNÓSTICO DE VALORES NULOS ---")
print(df.isnull().sum())

print("\n--- DIAGNÓSTICO DE DUPLICATAS ---")
print(f"Quantidade de registros duplicados: {df.duplicated().sum()}")

# Verificando possíveis datas que não puderam ser convertidas
print("\n--- DIAGNÓSTICO DA COLUNA DATA ---")
print(f"Datas inválidas ou não convertidas: {df['DATA'].isna().sum()}")

# Validação do identificador de número de compra (CO_ID)
print("\n--- VALIDAÇÃO DO IDENTIFICADOR CO_ID ---")
print(f"Quantidade de CO_ID duplicados: {df['CO_ID'].duplicated().sum()}")

# Tratamento das colunas residuais 'Unnamed'
colunas_vazias = [
    'Unnamed: 10',
    'Unnamed: 11',
    'Unnamed: 12',
    'Unnamed: 13'
]

df = df.drop(
    columns=colunas_vazias,
    errors='ignore'
)

# Tratamento das categorias vazias ou nulas
categorias_ajustadas = []

for item in df['PR_CAT']:
    if pd.isna(item) or item == "" or item == "NAN" or item == "NONE":
        categorias_ajustadas.append("Sem Categoria")
    else:
        categorias_ajustadas.append(item)

df['PR_CAT'] = categorias_ajustadas

# Remoção de registros completamente duplicados
df = df.drop_duplicates()

print("\n--- DIAGNÓSTICO DA BASE APÓS A LIMPEZA ---")
df.info()

# =====================================================================
# SPRINT 4: GERAÇÃO DE ESTATÍSTICAS BÁSICAS E VISUALIZAÇÃO
# =====================================================================
import matplotlib.pyplot as plt

print("--- PARÂMETROS ESTATÍSTICOS DA COLUNA FILHOS (CL_FHL) ---")

# Calculando os parâmetros estatísticos solicitados
total_filhos = df['CL_FHL'].count()
minimo_filhos   = df['CL_FHL'].min()
maximo_filhos   = df['CL_FHL'].max()
media_filhos    = df['CL_FHL'].mean()
mediana_filhos  = df['CL_FHL'].median()
desvio_filhos   = df['CL_FHL'].std()
moda_filhos     = df['CL_FHL'].mode()

# Exibindo os resultados de forma clara e estruturada
print(f"Total de Registros na Coluna FILHOS: {total_filhos}")
print(f"Valor Mínimo Registrado:     {minimo_filhos}")
print(f"Valor Máximo Registrado:     {maximo_filhos}")
print(f"Média Aritmética:            {media_filhos:.2f}")
print(f"Mediana (Tendência Central): {mediana_filhos}")
print(f"Desvio Padrão (Dispersão):   {desvio_filhos:.2f}")
print(f"Moda (Valor mais Frequente): {moda_filhos}")

print("\n--- VISUALIZAÇÃO DA DISTRIBUIÇÃO COM MATPLOTLIB ---")
# Criando a contagem de valores para o gráfico de barras
df['CL_FHL'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')

# Aplicando os títulos e rótulos usando a biblioteca Matplotlib
plt.title('Distribuição do Número de Filhos por Cliente')
plt.xlabel('Quantidade de Filhos')
plt.ylabel('Total de Clientes (Frequência)')

# Exibindo o gráfico na tela de forma limpa
plt.show()
