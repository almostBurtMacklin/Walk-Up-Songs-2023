import dash
from dash import Input, Output, State, html, dcc, dash_table, MATCH, ALL, ctx
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import os
import base64
import pages

df = pd.read_csv('button_maker.csv')
df['color']  = '#00244a'

df.to_csv('button_maker.csv', index = False)

from app import app


number_count = 1

server = app.server

navy = '#00244a'
grey = '#acafa6'

names = ['Sarah', 'James', 'Emily', 'Michael', 'Olivia', 'William', 'Ava', 'Benjamin', 'Sophia']

#pd.DataFrame(columns = ['name', 'position_key']).to_csv('position_key.csv', index = False)

df = pd.read_csv('position_key.csv')

child_list = []

for j in range(9):
    #indy = j - 1
    name = df.query('index == @j')['name'].iloc[0]

    child_list.append(
        dmc.Group(
            grow = True,
            children = [
                dmc.Badge(id={'type':'number', 'index':j}, color = 'gray', children = [' '], fullWidth=False),
                dmc.Select(data = [{'label':i, 'value':i} for i in names], id = {'type':'lineup','index':j}, value = name),
                dmc.Group(
                    id = {'type':'buttons', 'index':j},
                    grow = True,
                    children = [
                        # dmc.Button('Song 1', id = {'type':'play_song', 'index': f'1-{names[j]}'}, style = {'background-color':navy}),
                        # dmc.Button('Song 2', id = {'type':'play_song', 'index': f'2-{names[j]}'}, style = {'background-color':navy}),
                        # dmc.Button('Song 3', id = {'type':'play_song', 'index': f'3-{names[j]}'}, style = {'background-color':navy}),
                    ]
                )
            ]
        )
    )

def create_main_nav_link(icon, label, href):
    return dcc.Link(
        dmc.Group(
            position='center',
            spacing=10,
            style={'margin-bottom':5},
            children=[
                dmc.ThemeIcon(
                    DashIconify(icon=icon, width=18),
                    size=25,
                    radius=5,
                    color='indigo',
                    variant="filled",
                    style={'margin-left':10}
                ),
                dmc.Text(label, size="sm", color="gray", style={'font-family':'IntegralCF-Regular'}),
            ]
        ),
        href=href,
        style={"textDecoration": "none"},
    )

def create_accordianitem(icon, label, href):
    return dcc.Link(
        dmc.Group(
            position='left',
            spacing=10,
            style={'margin-bottom':10},
            children=[
                dmc.ThemeIcon(
                    DashIconify(icon=icon, width=18),
                    size=30,
                    radius=30,
                    color='grey',
                    variant="light",
                ),
                dmc.Text(label, size="sm", color="gray", style={'font-family':'IntegralCF-Regular'}),
            ]
        ),
        href=href,
        style={"textDecoration": "none"},
    )

app.layout = dmc.MantineProvider(
    withGlobalStyles=True, 
    children = [
        dcc.Store(id='testing-store', data = 2),

        html.Div(
            children = [
                dmc.Header(
                    height=70,
                    fixed=True,
                    pl=0,
                    pr=0,
                    pt=0,
                    style = {'background-color': navy, 'color': 'whitesmoke'},
                    children=[
                        dmc.Container(
                            fluid=True,
                            children=[
                                dmc.Group(
                                    position="apart",
                                    align="center",
                                    children=[
                                        dmc.Center(
                                            children=[
                                                dcc.Link(
                                                    dmc.ThemeIcon(
                                                        html.Img(src= '..\\assets\\panthers_logo.png', style={'width':43}),
                                                        radius='sm',
                                                        size=44,
                                                        variant="filled",
                                                        color="gray",
                                                    ),
                                                    href=app.get_relative_path("/"),
                                                ),
                                                dcc.Link(
                                                    href=app.get_relative_path("/"),
                                                    style={"paddingTop": 2, "paddingLeft":10, "paddingBottom":5, "paddingRight":10, "textDecoration": "none"},
                                                    children=[
                                                        dmc.MediaQuery(
                                                            smallerThan="sm",
                                                            styles={"display": "none"},
                                                            children=[
                                                                dmc.Stack(
                                                                    align='center', 
                                                                    spacing=0, 
                                                                    children=[
                                                                        dmc.Text("Walk Up Songs - 2023", size="lg", color="white", style={'font-family':'IntegralCF-ExtraBold'}),
                                                                        dmc.Badge("Kansas City Christian School", variant="outline", color="gray", size="sm",  style={'margin-top':4})
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                dmc.MediaQuery(
                                                    largerThan="sm",
                                                    styles={"display": "none"},
                                                    children=[
                                                        dmc.Stack(
                                                            align='flex-start', 
                                                            spacing=0,
                                                            children=[
                                                                dmc.Text("Walk Up Songs - 2023", size="sm", color="gray", style={'font-family':'IntegralCF-ExtraBold'}),
                                                                dmc.Badge("Kansas City Christian School", variant="outline", color="gray", size="xs")
                                                            ]
                                                        )
                                                    ]
                                                ),
                                            ]
                                        ),
                                        dmc.Group(
                                            children = [
                                                dmc.Divider(orientation='vertical'),
                                                dcc.Link('Set Lineup', className='navLinks', href=app.get_relative_path('/lineup')),
                                                dmc.Divider(orientation='vertical'),
                                                dcc.Link('Pre/Post Game Songs', className='navLinks', href = app.get_relative_path('/other_songs')),
                                                dmc.Divider(orientation='vertical'),
                                                dcc.Link('Lineup Walk Up Songs', className='navLinks',  href = app.get_relative_path('/walkup_songs')),
                                                dmc.Divider(orientation='vertical'),
                                                dcc.Link('All Walk Up Songs', className='navLinks',  href = app.get_relative_path('/all_walkups')),
                                                dmc.Divider(orientation='vertical'),
                                            ]
                                        )
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),

                dcc.Location(id='url'),
                html.Div(
                    id='content',
                    style={'margin-top':'70px'},
                    children = [
                        
                    ]
                )
            ]
        )
    ]
)

@app.callback(Output('content', 'children'),
                [Input('url', 'pathname')])
def display_content(pathname):
    page_name = app.strip_relative_path(pathname)
    if not page_name:  # None or ''
        return pages.lineup.layout
    elif page_name == 'lineup':
        return pages.lineup.layout  
    elif page_name == 'walkup_songs':
        return pages.walkupsongs.layout
    elif page_name =='other_songs':
        return pages.other_songs.layout
    elif page_name =='all_walkups':
        return pages.all_walkups.layout



if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1', port = 8050)
