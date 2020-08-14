import dash
from date_navigator import DateNavigator
from datetime import datetime as dt, timedelta
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

# Create Dash app with custom style sheet
app = dash.Dash(__name__,  title='Fishbowl Performance Charts')

# Custom index
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        <div>My Custom header</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>My Custom footer</div>
    </body>
</html>
'''

# Custom colors
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
    DateNavigator(app).get_div()])

# app.layout = dn.get_div()

if __name__ == '__main__':
    app.run_server(debug=True)

