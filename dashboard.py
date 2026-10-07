import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configura o título, ícone e layout da página
st.set_page_config(page_title="Wine Quality", page_icon="🍷", layout="wide")

# Guarda os dados em cache para evitar carregar os arquivos
# novamente toda vez que o dashboard for atualizado
@st.cache_data
def carregar_dados():
    red = pd.read_csv("winequality-red.csv", sep=";")
    white = pd.read_csv("winequality-white.csv", sep=";")
    red["wine_type"] = "Tinto"
    white["wine_type"] = "Branco"
    return pd.concat([red, white], ignore_index=True)

df = carregar_dados()

st.title("Wine Quality — Dashboard Estatístico")
st.write("Exploração das características físico-químicas e da qualidade de vinhos tintos e brancos.")

st.sidebar.header("Filtros")

tipos = st.sidebar.multiselect(
    "Tipo de vinho",
    sorted(df["wine_type"].unique()),
    default=sorted(df["wine_type"].unique())
)

# Cria um filtro para selecionar a faixa de qualidade
qualidade = st.sidebar.slider(
    "Faixa de qualidade",
    # Menor qualidade encontrada nos dados
    int(df["quality"].min()),
    # Maior qualidade encontrada nos dados
    int(df["quality"].max()),
    (int(df["quality"].min()), int(df["quality"].max()))
)

# Filtra os dados de acordo com as opções escolhidas
# pelo usuário na barra lateral
dados = df[
    df["wine_type"].isin(tipos)
    & df["quality"].between(qualidade[0], qualidade[1])
].copy()

# Cria quatro colunas para mostrar indicadores
c1, c2, c3, c4 = st.columns(4)
c1.metric("Observações", len(dados))
c2.metric("Qualidade média", f"{dados['quality'].mean():.2f}")
c3.metric("Álcool médio", f"{dados['alcohol'].mean():.2f}")
c4.metric("pH médio", f"{dados['pH'].mean():.2f}")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribuição da qualidade")
    fig, ax = plt.subplots(figsize=(7, 4))
    # Cria um histograma mostrando a distribuição
    # das notas de qualidade para cada tipo de vinho
    sns.histplot(data=dados, x="quality", hue="wine_type", discrete=True, multiple="dodge", ax=ax)
    ax.set_xlabel("Qualidade")
    ax.set_ylabel("Quantidade")
    st.pyplot(fig)

with col2:
    st.subheader("Qualidade por tipo")
    fig, ax = plt.subplots(figsize=(7, 4))
    # Cria um boxplot comparando a qualidade
    # dos vinhos tintos e brancos
    sns.boxplot(data=dados, x="wine_type", y="quality", ax=ax)
    ax.set_xlabel("Tipo")
    ax.set_ylabel("Qualidade")
    st.pyplot(fig)

st.divider()

# Lista com as variáveis físico-químicas
# presentes no conjunto de dados
variaveis = [
    "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
    "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density",
    "pH", "sulphates", "alcohol"
]

st.subheader("Relação entre uma variável físico-química e qualidade")
# Cria uma caixa de seleção para escolher
# qual variável será analisada
variavel = st.selectbox("Escolha a variável", variaveis, index=10)

fig, ax = plt.subplots(figsize=(10, 5))
# Cria um gráfico de dispersão
# relacionando a variável escolhida com a qualidade
sns.scatterplot(
    data=dados,
    x=variavel,
    y="quality",
    hue="wine_type",
    alpha=0.35,
    ax=ax
)
ax.set_xlabel(variavel)
ax.set_ylabel("Qualidade")
st.pyplot(fig)

st.subheader("Correlação com qualidade")
# Calcula a correlação de Pearson
# entre as variáveis numéricas e a qualidade
numericas = dados[variaveis + ["quality"]].corr()["quality"].drop("quality").sort_values()

fig, ax = plt.subplots(figsize=(10, 5))
# Cria um gráfico de barras horizontais
# mostrando as correlações com a qualidade
numericas.plot(kind="barh", ax=ax)
ax.set_xlabel("Correlação de Pearson")
ax.set_ylabel("Variável")
st.pyplot(fig)

st.subheader("Tabela dos dados filtrados")
st.dataframe(dados, use_container_width=True)
