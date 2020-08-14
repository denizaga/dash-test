import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import matplotlib
import plotly.graph_objs as go


def build_hour_box(y0):
    box = go.Box(
        y=y0,
        name
    )
    return box

hours = [None,None,None,None,None,None,None,None,None,None,
         None,None,None,None,None,None,None,None,None,None,
         None,None,None,None]

hours[0] = build_hour_box([19, 2, 9])
hours[1] = build_hour_box([10, 3, 5])
hours[2] = build_hour_box([19, 2, 9])
hours[3] = build_hour_box([10, 3, 5])
hours[4] = build_hour_box([19, 2, 9])
hours[5] = build_hour_box([10, 3, 5])
hours[6] = build_hour_box([19, 2, 9])
hours[7] = build_hour_box([10, 3, 5])
hours[8] = build_hour_box([19, 2, 9])
hours[9] = build_hour_box([10, 3, 5])
hours[10] = build_hour_box([19, 2, 9])
hours[11] = build_hour_box([10, 3, 5])
hours[12] = build_hour_box([19, 2, 9])
hours[13] = build_hour_box([10, 3, 5])
hours[14] = build_hour_box([19, 2, 9])
hours[15] = build_hour_box([10, 3, 5])
hours[16] = build_hour_box([19, 2, 9])
hours[17] = build_hour_box([10, 3, 5])
hours[18] = build_hour_box([19, 2, 9])
hours[19] = build_hour_box([10, 3, 5])
hours[20] = build_hour_box([19, 2, 9])
hours[21] = build_hour_box([10, 3, 5])
hours[22] = build_hour_box([19, 2, 9])
hours[23] = build_hour_box([10, 3, 5])


data = hours


app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(figure={
                'data': data,
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)

