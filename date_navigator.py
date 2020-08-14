# Copyright Caterpillar 2020
# Date: 17/08/2020
# Author: Deniz Aga

from datetime import datetime as dt, timedelta
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import re


class DateNavigator:
    def __init__(self, p_app):
        # Application reference
        self.app = p_app

        self.app.callback(
            Output('output-container-date-picker-single', 'children'),
            [Input('my-date-picker-single', 'date')])(self.update_date)
        self.app.callback(
                Output('my-date-picker-single', 'date'),
                [Input('forward-btn', 'n_clicks'),
                 Input('back-btn', 'n_clicks')],
                [State('my-date-picker-single', 'date')])(self.increment_decrement_date)

        # Forward and back buttons for inc/dec date
        self.back = html.Button('<', id='back-btn', n_clicks=0)
        self.forward = html.Button('>', id='forward-btn', n_clicks=0)

        # Date picker object
        self.date_picker = dcc.DatePickerSingle(
                id='my-date-picker-single',
                min_date_allowed=dt(2019, 12, 31),
                max_date_allowed=dt(2023, 12, 31),
                initial_visible_month=dt.today(),
                date=str(dt.now())
            )

        # Result object
        self.result = html.Div(id='output-container-date-picker-single', children='Result:')

        # Use flex to center date picker in center of screen
        self.date_row = html.Div([self.back, self.date_picker, self.forward], style={'display': 'flex',
                                                                'align-items': 'center',
                                                                'justify-content': 'center'})

    def get_div(self):
        return html.Div([self.date_row, self.result])

    # This callback handles the date picker, it will also be triggered by increment_decrement_date
    def update_date(self, date):
        string_prefix = 'You have selected: '
        if date is not None:
            date = dt.strptime(re.split('T| ', date)[0], '%Y-%m-%d')
            date_string = date.strftime('%B %d, %Y')
            return string_prefix + date_string

    # This callback handles the date increment decrement
    def increment_decrement_date(self, f_clicks, b_clicks, p_date):
        # Get the triggered element
        triggered = [t["prop_id"] for t in dash.callback_context.triggered]

        date = None
        # Have to check the date, for some reason this method gets called onLoad of page
        if p_date is not None:
            date = dt.strptime(re.split('T| ', p_date)[0], '%Y-%m-%d')

            if triggered[0] == 'forward-btn.n_clicks':
                date += timedelta(days=1)
            elif triggered[0] == 'back-btn.n_clicks':
                date -= timedelta(days=1)
            else:
                date = dt.now()

        return date

