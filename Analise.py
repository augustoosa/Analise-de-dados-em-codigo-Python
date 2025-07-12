# Importação das bibliotecas necessárias para manipulação de dados, visualização e análise
import pandas as pd
import re
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Leitura do arquivo Excel contendo os dados das empresas e armazenando-o na variável 'data'
data = pd.read_excel('/Users/Augusto/Downloads/Empresas cornelio procopio/cornelioprocopio extenso.xlsx')

# Remoção de colunas irrelevantes para a análise atual, mantendo o dataset mais enxuto
data.drop([
    'cnpj','raiz_cnpj','matriz_filial','razao_social','situacao_cadastral','socios',
    'data_inicio_atividade','cnae_fiscal','cnae_principal_desc_secao','cnae_principal_desc_divisao',
    'cnae_principal_desc_grupo','cnae_principal_desc_classe','cnae_principal_desc_subclasse',
    'cnae_fiscal_secundaria','cnae_fiscal_secundaria2','descricao_tipo_logradouro','logradouro',
    'numero','complemento','cep','municipio','uf','macrorregiao','mesorregiao','microrregiao','coords',
    'qualificacao_do_responsavel','dominio','email','correio_eletronico',
    'correio_eletronico_pertence_contador','linkedin','facebook','whatsapp','instagram','twitter',
    'TELEFONE 1','TELEFONE 2','TELEFONE 3','TELEFONE 4','TELEFONE 5','TELEFONE 6',
    'telefones_concatenados','produto_ncm'
], axis=1, inplace=True)

# Verifica os ramos de atividade mais frequentes entre as empresas
data['ramo_de_atividade'].value_counts()

# Cálculo da média do capital social agrupado por ramo de atividade
media_por_ramo = data.groupby('ramo_de_atividade').capital_social.mean().sort_values(ascending=False)
media_por_ramo

# Gráfico de barras mostrando a quantidade de empresas por ramo de atividade
ax = sns.countplot(x='ramo_de_atividade', data=data, order=media_por_ramo.index)
ax.set_xticklabels(labels=media_por_ramo.index, rotation='vertical')
ax.set_ylabel('Quantidade de Empresas')
ax.set_xlabel('Ramo de Atividade')
ax.set_title('Quantidade de Empresas por Ramo')

# Gráfico de barras exibindo a média de capital social por ramo de atividade
ax = sns.barplot(media_por_ramo)
ax.set_xticklabels(labels=media_por_ramo.index, rotation='vertical')
ax.set_ylabel('Média do Capital Social')
ax.set_xlabel('Ramo de Atividade')
ax.set_title('Média do Capital por Atividade Econômica')

# Gráfico de barras empilhadas mostrando a distribuição de empresas por faixa de faturamento e ramo
from seaborn import objects as so
fig = plt.figure()
(so.Plot(data, x="ramo_de_atividade", color="faixa_faturamento_grupo")
    .add(so.Bar(), so.Count(), so.Stack())
    .on(fig)
    .plot())

# Rotaciona os rótulos do eixo X para melhor visualização
for ax in fig.axes:
    ax.tick_params("x", rotation=90)

# Importa codificador para transformar variáveis categóricas em numéricas
from sklearn.preprocessing import LabelEncoder

# Seleciona colunas relevantes para análise de correlação
analise = data.loc[:, ['qtde_filiais', 'ramo_de_atividade', 'porte', 'capital_social', 'faixa_faturamento_grupo']]

# Codificação de variáveis categóricas em valores numéricos
le = LabelEncoder()
analise['ramo_de_atividade'] = le.fit_transform(analise['ramo_de_atividade'])
analise['porte'] = le.fit_transform(analise['porte'])
analise['faixa_faturamento_grupo'] = le.fit_transform(analise['faixa_faturamento_grupo'])

# Calcula a matriz de correlação entre as variáveis numéricas
corr = analise.corr()

# Visualiza a matriz de correlação em formato de mapa de calor
plt.figure(figsize=(10, 8))
ax = sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values,
                 linewidths=0.25, vmax=1.0, square=True, cmap='coolwarm',
                 linecolor='black', annot=False)
plt.title("Matriz de Correlação entre Variáveis")
plt.show()
