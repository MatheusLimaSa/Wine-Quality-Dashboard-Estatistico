# Projeto-Dashboard---Matheus-Lima-e-Bernardo-Lopes
# 🍷 Wine Quality — Dashboard Estatístico

Projeto de **Modelagem Estatística** desenvolvido em dupla por **Matheus Lima** e **Bernardo Lopes**.

O projeto utiliza o conjunto de dados **Wine Quality** para analisar a relação entre características físico-químicas de vinhos e suas respectivas notas de qualidade.

## 👥 Autores

- **Matheus Lima**
- **Bernardo Lopes**

## 🎯 Objetivo

Investigar quais características físico-químicas apresentam relação com a qualidade dos vinhos e utilizar técnicas estatísticas para analisar esses relacionamentos.

Os resultados também são apresentados por meio de um **dashboard interativo desenvolvido em Python e Streamlit**.

## 📊 Dados

O projeto utiliza dois arquivos:

- `winequality-red.csv` — vinhos tintos
- `winequality-white.csv` — vinhos brancos

Entre as características analisadas estão:

- Acidez fixa
- Acidez volátil
- Ácido cítrico
- Açúcar residual
- Cloretos
- Dióxido de enxofre livre
- Dióxido de enxofre total
- Densidade
- pH
- Sulfatos
- Álcool

A variável `quality` representa a qualidade atribuída ao vinho.

## 📈 Análises realizadas

- Análise exploratória dos dados
- Estatística descritiva
- Distribuição das notas de qualidade
- Comparação entre vinhos tintos e brancos
- Correlação de Pearson
- Testes de hipóteses
- Intervalos de confiança
- Regressão linear
- Avaliação do modelo
- Previsão de qualidade
- Dashboard interativo

## 🖥️ Dashboard

O dashboard permite filtrar os dados por:

- Tipo de vinho: **Tinto** ou **Branco**
- Faixa de qualidade

Também apresenta:

- Quantidade de observações
- Qualidade média
- Álcool médio
- pH médio
- Distribuição das notas de qualidade
- Comparação da qualidade entre os tipos de vinho
- Relação entre características físico-químicas e qualidade
- Correlação das variáveis com a qualidade
- Tabela dos dados filtrados

## 🛠️ Tecnologias

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Statsmodels
- Scikit-learn
- Streamlit
- Jupyter Notebook

## 📁 Estrutura do projeto

```text
Wine-Quality/
│
├── winequality-red.csv
├── winequality-white.csv
├── winequality.names
│
├── Wine_Quality_Projeto.ipynb
├── dashboard.py
├── requirements.txt
└── README.md
```

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
cd Wine-Quality
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o dashboard

```bash
streamlit run dashboard.py
```

Depois, abra no navegador o endereço fornecido pelo Streamlit, normalmente:

```text
http://localhost:8501
```

## 📓 Notebook

O arquivo `Wine_Quality_Projeto.ipynb` contém o desenvolvimento da análise estatística, incluindo:

- Importação e preparação dos dados
- Análise exploratória
- Estatística descritiva
- Testes de hipóteses
- Intervalos de confiança
- Regressão linear
- Avaliação do modelo
- Previsões
- Conclusões

## 📌 Pergunta principal

> **Quais características físico-químicas apresentam maior relação com a qualidade do vinho e até que ponto elas permitem prever a nota de qualidade?**

## 👨‍💻 Autores

**Matheus Lima**  
**Bernardo Lopes**

Projeto acadêmico desenvolvido para a disciplina de **Modelagem Estatística**.
