import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import requests
from datetime import datetime, timedelta
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Crypto Dashboard",
    page_icon="📈",
    layout="wide"
)

# Título e descrição
st.title("📊 Dashboard de Criptomoedas")
st.markdown("""
Este dashboard mostra dados em tempo real das principais criptomoedas do mercado.
""")

# Função para buscar dados da API CoinGecko
def fetch_crypto_data():
    try:
        # Lista de criptomoedas para monitorar
        crypto_ids = ['bitcoin', 'ethereum', 'binancecoin', 'cardano', 'solana']
        
        # Buscar dados de preço
        price_data = requests.get(
            f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(crypto_ids)}&vs_currencies=usd&include_24hr_change=true"
        ).json()
        
        # Buscar dados históricos para o Bitcoin (exemplo)
        historical_data = requests.get(
            "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"
        ).json()
        
        return price_data, historical_data
    except Exception as e:
        st.error(f"Erro ao buscar dados: {str(e)}")
        return None, None

# Buscar dados
price_data, historical_data = fetch_crypto_data()

if price_data and historical_data:
    # Criar layout com colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Preços Atuais")
        # Criar DataFrame com preços
        prices_df = pd.DataFrame([
            {
                'Criptomoeda': crypto.capitalize(),
                'Preço (USD)': f"${price_data[crypto]['usd']:,.2f}",
                'Variação 24h': f"{price_data[crypto]['usd_24h_change']:.2f}%"
            }
            for crypto in price_data
        ])
        st.dataframe(prices_df, use_container_width=True)
    
    with col2:
        st.subheader("Variação de Preço (24h)")
        # Criar gráfico de barras para variação
        fig = px.bar(
            prices_df,
            x='Criptomoeda',
            y='Variação 24h',
            title='Variação de Preço nas Últimas 24 Horas'
        )
        fig.update_traces(marker_color=['#FF9900' if x >= 0 else '#FF0000' for x in prices_df['Variação 24h']])
        st.plotly_chart(fig, use_container_width=True)
    
    # Gráfico de linha para preço histórico do Bitcoin
    st.subheader("Preço Histórico do Bitcoin (30 dias)")
    dates = [datetime.fromtimestamp(price[0]/1000) for price in historical_data['prices']]
    prices = [price[1] for price in historical_data['prices']]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=prices,
        mode='lines',
        name='Preço do Bitcoin',
        line=dict(color='#FF9900')
    ))
    fig.update_layout(
        title='Preço do Bitcoin nos Últimos 30 Dias',
        xaxis_title='Data',
        yaxis_title='Preço (USD)',
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Métricas adicionais
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.metric(
            "Bitcoin (BTC)",
            f"${price_data['bitcoin']['usd']:,.2f}",
            f"{price_data['bitcoin']['usd_24h_change']:.2f}%"
        )
    
    with col4:
        st.metric(
            "Ethereum (ETH)",
            f"${price_data['ethereum']['usd']:,.2f}",
            f"{price_data['ethereum']['usd_24h_change']:.2f}%"
        )
    
    with col5:
        st.metric(
            "Binance Coin (BNB)",
            f"${price_data['binancecoin']['usd']:,.2f}",
            f"{price_data['binancecoin']['usd_24h_change']:.2f}%"
        )

# Adicionar informações sobre o dashboard
st.markdown("---")
st.markdown("""
### Sobre o Dashboard
- Dados atualizados em tempo real via API CoinGecko
- Monitoramento das principais criptomoedas
- Visualização de preços e variações
- Gráficos interativos com Plotly
""") 
