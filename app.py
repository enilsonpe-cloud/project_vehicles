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
