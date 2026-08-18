# ==========================================
# SPRINT 1: IMPORTAÇÃO E EXPLORAÇÃO INICIAL
# ==========================================

import pandas as pd
import numpy as np

# Carregando a base de dados com o separador correto (ponto e vírgula)
df = pd.read_csv("Base Varejo.csv", sep=";")

# Visualizando as primeiras linhas para entender a estrutura dos dados
print("Primeiras linhas do dataset:")
display(df.head())

# Verificando informações gerais: quantidade de registros, colunas e tipos de dados
print("\nInformações gerais sobre a base de dados:")
df.info()

# Verificando a quantidade de registros e colunas
print(f"Quantidade de registros: {df.shape[0]}")

# Verificando a quantidade de colunas
print(f"Quantidade de colunas: {df.shape[1]}")

# Verificando os nomes das colunas
print("\nColunas:")

# Imprimindo a lista de nomes de colunas
print(df.columns.tolist())


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

# ==========================================
# SPRINT 5: ANÁLISE POR AGRUPAMENTOS
# ==========================================

# Agrupamento 1: quantidade de compras distintas por gênero
compras_por_genero = (df.groupby('CL_GENERO')['CO_ID'].nunique().sort_values(ascending=False))

print("\n--- COMPRAS DISTINTAS POR GÊNERO ---")
print(compras_por_genero)


# Visualização das compras distintas por gênero
compras_por_genero.plot(kind='bar',edgecolor='black')

plt.title('Quantidade de Compras Distintas por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade de Compras Distintas')
plt.xticks(rotation=0)
plt.show()


# Agrupamento 2: quantidade de registros de produtos por categoria
produtos_por_categoria = (df.groupby('PR_CAT')['PR_ID'].count().sort_values(ascending=False))

print("\n--- QUANTIDADE DE PRODUTOS POR CATEGORIA ---")
print(produtos_por_categoria)


# Visualização da quantidade de registros por categoria
produtos_por_categoria.plot(kind='bar',edgecolor='black')

plt.title('Quantidade de Registros de Produtos por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Quantidade de Registros')
plt.xticks(rotation=45, ha='right')
plt.show()

# ==========================================
# SPRINT 6: EXPORTAÇÃO DA BASE LIMPA
# ==========================================

# Salvando a base após as etapas de limpeza e transformação
df.to_csv("df_limpo.csv", sep=";", index=False)

print("\n--- BASE LIMPA EXPORTADA ---")
print("Arquivo 'df_limpo.csv' criado com sucesso.")
print(f"Quantidade de registros: {df.shape[0]}")
print(f"Quantidade de colunas: {df.shape[1]}")