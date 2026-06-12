import pandas as pd
import plotly.express as px
import streamlit as st

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

# Botão para gerar o gráfico de histograma
hist_button = st.button('Criar histograma', key="hist1")  # criar um botão

if hist_button:
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
