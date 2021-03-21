import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('./data/finance-charts-apple.csv')

fig = go.Figure(data=[go.Candlestick(name='Свечи', x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

fig.add_trace(go.Scatter(name='Средняя',x=df['Date'], y=(df['AAPL.High']+df['AAPL.Low'])/2,marker_color='rgba(0, 0, 102, .6)'))

fig.show()
