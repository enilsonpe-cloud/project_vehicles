import pandas as pd
import plotly.express as px
import streamlit as st

# Criando a página de análise de veículos com Streamlit
st.set_page_config(
    page_title="Análise de Veículos",
    page_icon="🚗",
    layout="wide"
)

# Estilo do título
st.markdown("""
    <style>
        .big-title {
            font-size: 36px !important;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='big-title'>🚗 Análise de Veículos</p>",
            unsafe_allow_html=True)

# Carregar dados
car_data = pd.read_csv("vehicles.csv")  # lendo os dados

# Criando Botão para gerar o gráfico de histograma
hist_button = st.button('Criar histograma', key="hist1")  # criar um botão

# Verifica se o botão do histograma foi clicado
if hist_button:
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


""" Criando um gráfico de dispersão para analisar a relação entre preço e quilometragem 
    dos veículos """

# Estilo do título gráfico de dispersão
st.markdown("""
    <style>
        .custom-title {
            font-size: 36px !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='custom-title'>Gráfico de Dispersão — Preço vs Quilometragem</p>",
            unsafe_allow_html=True)

# Criando Botão para gerar o gráfico de dispersão
hist_button2 = st.button('Criar de Dispersão', key="hist2")  # criar um botão

# Verifica se o botão da dispersão foi clicado
if hist_button2:
    # Gráfico
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="condition",
        title="Preço vs Quilometragem",
        labels={
            "odometer": "Quilometragem (km)",
            "price": "Preço (R$)",
            "condition": "Condição"
        },
        opacity=0.7,
    )
    st.plotly_chart(fig, use_container_width=True)


""" Criando um gráfico de dispersão para analisar a relação entre preço e quilometragem 
    com filtros para modelo, ano e preço máximo dos veículos """

# Estilo do título gráfico de dispersão
st.markdown("""
    <style>
        .custom-title {
            font-size: 36px !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='custom-title'>Gráfico de Dispersão com filtros — Preço vs Quilometragem<</p>",
            unsafe_allow_html=True)

# Colocando os filtros em cima do gráfico
st.markdown("### Filtros")

col1, col2, col3 = st.columns(3)

# Filtro de Modelo
with col1:
    modelo = st.selectbox("Modelo", sorted(car_data["model"].unique()))

# Filtro de Ano
with col2:
    ano = st.slider(
        "Ano",
        int(car_data["model_year"].min()),
        int(car_data["model_year"].max())
    )

# Filtro de Preço
with col3:
    preco_max = st.number_input("Preço máximo", min_value=0, value=50000)


# Aplicando os filtros
df_filtrado = car_data[
    (car_data["model"] == modelo) &
    (car_data["model_year"] >= ano) &
    (car_data["price"] <= preco_max)
]

# Criando o gráfico de dispersão com os dados filtrados
fig = px.scatter(
    df_filtrado,
    x="odometer",
    y="price",
    color="condition",
    title="Preço vs Quilometragem",
    labels={"odometer": "Quilometragem", "price": "Preço"}
)

st.plotly_chart(fig, use_container_width=True)
