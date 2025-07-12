# 📊 Análise de Dados com Python — Empresas de Cornélio Procópio

Este projeto tem como objetivo **praticar a manipulação e visualização de dados** utilizando bibliotecas populares do ecossistema Python como `pandas`, `matplotlib`, `seaborn`, entre outras.

A análise foi feita com base em um conjunto de dados de empresas da cidade de **Cornélio Procópio (PR)**, e inclui etapas como limpeza dos dados, análise estatística básica, visualização gráfica e análise de correlação.

---

## 🧰 Bibliotecas Utilizadas

- [`pandas`](https://pandas.pydata.org/) — para manipulação de dados tabulares  
- [`numpy`](https://numpy.org/) — para operações matemáticas  
- [`seaborn`](https://seaborn.pydata.org/) — para visualizações estatísticas  
- [`matplotlib`](https://matplotlib.org/) — para criação de gráficos  
- [`sklearn.preprocessing.LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) — para codificação de dados categóricos  

---

## 📝 Etapas do Código

### 1. **Importação das Bibliotecas**
Carregamento das bibliotecas necessárias para análise e visualização de dados.

### 2. **Leitura do Arquivo Excel**
Utiliza `pandas.read_excel()` para importar o dataset com informações sobre empresas da cidade.

### 3. **Limpeza de Dados**
Remove colunas irrelevantes para a análise, mantendo apenas os dados essenciais como:
- Ramo de atividade
- Porte da empresa
- Capital social
- Faixa de faturamento
- Quantidade de filiais

### 4. **Análise Exploratória**
- Identificação dos **ramos de atividade mais comuns**
- Cálculo da **média de capital social** por ramo de atividade

### 5. **Visualizações**
Gráficos gerados com `seaborn` e `matplotlib`:
- Gráfico de barras da quantidade de empresas por ramo
- Gráfico de barras da média de capital por atividade
- Gráfico de barras empilhadas com a distribuição por **faixa de faturamento**

### 6. **Preparação para Análise de Correlação**
- Conversão de variáveis categóricas (como "porte" e "ramo de atividade") em valores numéricos com `LabelEncoder`
- Cálculo da **matriz de correlação** entre variáveis quantitativas
- Visualização da matriz com um **heatmap**

---

## 📌 Objetivo

Este código não tem fins comerciais ou de produção. Ele foi desenvolvido para **praticar conceitos fundamentais de análise de dados em Python**, como:
- Limpeza de dados  
- Agrupamento e estatísticas descritivas  
- Visualização gráfica  
- Codificação de variáveis categóricas  
- Interpretação de correlação  

---

## 📁 Arquivo Utilizado

O código utiliza um arquivo `.xlsx` com dados de empresas de Cornélio Procópio. Por questões de privacidade, esse arquivo **não está incluído** no repositório. Caso você deseje executar o código, substitua o caminho para um arquivo Excel próprio com colunas semelhantes.

---

## ✅ Requisitos para Execução

Instale as bibliotecas com:

```bash
pip install pandas matplotlib seaborn scikit-learn
