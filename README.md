# cripto_360

# Dashboard de Criptomoedas

Este é um dashboard interativo que mostra dados em tempo real das principais criptomoedas do mercado, utilizando a API CoinGecko.

## Funcionalidades

- Preços atuais das principais criptomoedas
- Variação de preço nas últimas 24 horas
- Gráfico histórico de preços do Bitcoin
- Métricas em tempo real
- Interface interativa e responsiva

## Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone este repositório ou baixe os arquivos
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando o Dashboard

Para executar o dashboard localmente:

```bash
streamlit run app.py
```

O dashboard estará disponível em `http://localhost:8501`

## Deploy

Para fazer deploy do dashboard, você pode usar o Streamlit Cloud (gratuito):

1. Crie uma conta em [Streamlit Cloud](https://streamlit.io/cloud)
2. Conecte seu repositório GitHub
3. Selecione o repositório e o arquivo `app.py`
4. Clique em "Deploy"

## Tecnologias Utilizadas

- Streamlit
- Pandas
- Plotly
- CoinGecko API
- Python

## Atualizações

O dashboard atualiza automaticamente os dados a cada vez que é carregado, mostrando as informações mais recentes do mercado de criptomoedas. 
