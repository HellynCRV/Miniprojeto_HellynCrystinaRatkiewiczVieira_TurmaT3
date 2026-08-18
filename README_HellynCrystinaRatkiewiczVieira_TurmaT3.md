# Análise Exploratória de Dados - Base Varejo

## Sobre o projeto

Este projeto apresenta uma Análise Exploratória de Dados (AED) aplicada a uma base de dados de varejo. O objetivo foi realizar a importação, transformação, limpeza e análise dos dados utilizando Python e Pandas.

O projeto foi desenvolvido como parte do Mini-Projeto Avaliativo do Módulo 1 da disciplina de Visualização de Dados e Business Intelligence.

## Etapas desenvolvidas

### Sprint 1 - Importação e reconhecimento da base

A base `Base Varejo.csv` foi importada utilizando o Pandas, considerando o ponto e vírgula como separador. Foram verificadas a quantidade de registros, quantidade de colunas, nomes das colunas, tipos de dados e as primeiras linhas da base.

### Sprint 2 - Transformação e padronização

Foram realizadas transformações nas colunas de texto, utilizando `str.strip()` e `str.upper()`. A coluna `DATA` também foi convertida para o formato `datetime`.

### Sprint 3 - Limpeza de dados

Foram identificados valores nulos, registros duplicados e possíveis inconsistências nas datas. As colunas `Unnamed` foram removidas por não apresentarem informações relevantes. As categorias vazias ou nulas foram tratadas como `Sem Categoria` e os registros completamente duplicados foram removidos.

Também foi realizada a validação do identificador `CO_ID`. Como uma mesma compra pode possuir diferentes produtos, a repetição do `CO_ID` não foi considerada, isoladamente, uma duplicidade de registro.

### Sprint 4 - Estatística descritiva

Foram calculadas estatísticas descritivas da coluna `CL_FHL`, correspondente ao número de filhos dos clientes, incluindo contagem, mínimo, máximo, média, mediana, desvio padrão e moda.

### Sprint 5 - Agrupamentos e visualização

Foram utilizados agrupamentos com `groupby()` para analisar as compras distintas por gênero e a quantidade de registros de produtos por categoria. Também foram produzidos gráficos de barras para facilitar a interpretação dos resultados.

## Reflexão sobre ETL e qualidade dos dados

O processo realizado pode ser relacionado ao conceito de ETL: os dados foram inicialmente extraídos e carregados para o ambiente Python, depois transformados e tratados para melhorar sua qualidade e, por fim, preparados para utilização em análises posteriores.

A etapa de limpeza demonstrou a importância da qualidade dos dados para uma análise confiável. Foram encontrados registros duplicados e colunas sem informações relevantes, além de categorias classificadas como `#N/D`. O tratamento desses problemas contribui para reduzir inconsistências e melhorar a utilização da base em análises e ferramentas de BI.

## Principais insights

- O gênero feminino apresentou 9.615 compras distintas, enquanto o masculino apresentou 8.856.
- A categoria `ALIMENTOS` apresentou a maior quantidade de registros de produtos, com 384.197 ocorrências.
- As categorias `HIGIENE` e `LIMPEZA` apresentaram 137.702 e 128.632 registros, respectivamente.
- A categoria `ACESSORIOS` apresentou 12.871 registros, sendo a menor entre as categorias identificadas.
- Foram encontrados 3.228 registros classificados como `#N/D`, indicando uma inconsistência de classificação que pode ser tratada em uma etapa posterior.
- A limpeza removeu 96.553 registros completamente duplicados, reduzindo a base de 830.000 para 733.447 registros.