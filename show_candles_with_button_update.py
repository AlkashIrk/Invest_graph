import plotly.graph_objects as go

import pandas as pd
from datetime import datetime


button_style = {
            'display':'inline-block',
            'height':'38px',
            'padding': '0 30px',
            'color': '#555',
            'text-align':'center',
            'font-size':'11px',
            'font-weight':'600',
            'line-height':'38px',
            'letter-spacing':'.1rem',
            'text-transform':'uppercase',
            'text-decoration':'none',
            'white-space':'nowrap',
            'background-color':'transparent',
            'border-radius':'4px',
            'border':'1px solid #bbb',
            'cursor':'pointer',
            'box-sizing':'border-box',
            }


def update_fig():
    df = pd.read_csv('./data/finance-charts-apple.csv')
    fig = go.Figure(data=[go.Candlestick(name='Свечи', x=df['Date'],
                                         open=df['AAPL.Open'],
                                         high=df['AAPL.High'],
                                         low=df['AAPL.Low'],
                                         close=df['AAPL.Close'])])

    fig.add_trace(go.Scatter(name='Средняя', x=df['Date'], y=(df['AAPL.High'] + df['AAPL.Low']) / 2,
                             marker_color='rgba(0, 0, 102, .6)'))
    return fig




fig = update_fig()

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Button("Update", id="button_2",style=button_style),
    html.Div(children=dcc.Graph(figure=fig), id="content")
])

@app.callback(
    Output("content", "children"),
    Input("button_2", "n_clicks"))
def first_callback(n):
    fig = update_fig()
    graph = dcc.Graph(figure=fig)
    return graph

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
