import dash
from dash import Input, Output, State, html, dcc, dash_table, MATCH, ALL, ctx
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, time, timedelta
import os
import base64

from app import app


server = app.server

navy = '#00244a'
grey = '#acafa6'

names = ['Sarah', 'James', 'Emily', 'Michael', 'Olivia', 'William', 'Ava', 'Benjamin', 'Sophia']


child_list = []

for j in range(9):
    child_list.append(
        dmc.Group(
            grow = True,
            children = [
                dmc.Select(data = [{'label':i, 'value':i} for i in names], value = names[j]),
                dmc.Button('Song 1', id = {'type':'play_song', 'index': f'1-{names[j]}'}),
                dmc.Button('Song 2', id = {'type':'play_song', 'index': f'2-{names[j]}'}),
                dmc.Button('Song 3', id = {'type':'play_song', 'index': f'3-{names[j]}'}),
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
                                                                dmc.Badge("Kansas City Christian School", variant="outline", color="grey", size="xs")
                                                            ]
                                                        )
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
                dmc.Modal(
                    id = 'the-modal',
                    overflow = 'inside',
                    size = 'xl',
                    children = [
                        
                    ],
                    opened = False
                ),

                # dmc.Navbar(
                #     fixed=True,
                #     width={"base": 300},
                #     pl='sm',
                #     pr='xs',
                #     pt=0,
                #     hidden=True,
                #     hiddenBreakpoint='sm',
                #     children=[
                #         dmc.ScrollArea(
                #             offsetScrollbars=True,
                #             type="scroll",
                #             children=[
                #                 dmc.Stack(
                #                     align = 'center',
                #                     spacing = 'xs',
                #                     children =[
                #                         dmc.Text('Built By: Andrew Schutte', style = {'font-family':'IntegralCF-RegularOblique'}, size = 'sm'),
                #                         #dmc.Text('Kansas City, USA', style = {'font-family':'IntegralCF-RegularOblique'}, size = 'sm')
                #                     ]
                #                 ),
                                
                #                 #html.Img(src='https://plotly.chiefs.work/ticketing/assets/SA.svg', id  = 'sa-logo', style={'width':160, 'margin-left':50}),
                #                 dmc.Divider(label='Customer Exploration', style={"marginBottom": 20, "marginTop": 5}),
                #                 dmc.Stack(
                #                     align = 'flex-start',
                #                     children=[
                #                         create_main_nav_link(
                #                             icon="mdi:people-group",
                #                             label="Customer Base",
                #                             href=app.get_relative_path("/"),
                #                         ),
                #                         create_main_nav_link(
                #                             icon="mdi:magnify",
                #                             label="Churn Investigation",
                #                             href=app.get_relative_path("/churn"),
                #                         ),
                #                         create_main_nav_link(
                #                             icon="ooui:text-summary-ltr",
                #                             label="Churn Prediction",
                #                             href=app.get_relative_path("/summary"),
                #                         ),
                #                     ],
                #                 ),

                #             ],
                #         )
                #     ],
                # ),

                dcc.Location(id='url'),
                html.Div(
                    id='content',
                    style={'margin-top':'70px'},
                    children = [
                        dmc.Stack(
                            align = 'center',
                            spacing = 28,
                            #direction = 'row',
                            children=[
                                html.Audio(
                                    id='audio-player',
                                    #src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode()),
                                    controls=True,
                                    autoPlay=False,
                                ),
                                dmc.Paper(
                                    style = {'width':'50%'},
                                    shadow = 'md',
                                    radius = 'md',
                                    withBorder=True,
                                    p = 'sm',
                                    children = [
                                        dmc.Stack(
                                            children = [
                                                dmc.Title('Lineup', order = 4),
                                                dmc.Stack(
                                                    children = child_list
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                
                                dmc.Group(
                                    children = [
                                        dmc.Button('Play 1', id = {'type':'play_button', 'index':0}),
                                        dmc.Button('Play 1', id = {'type':'play_button', 'index':1}),
                                        dmc.Button('Play 1', id = {'type':'play_button', 'index':2}),
                                        dmc.Button('Play 1', id = {'type':'play_button', 'index':3}),
                                        dmc.Button('Play 1', id = {'type':'play_button', 'index':4})
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

@app.callback(Output('audio-player', 'src'),
                Output('audio-player', 'autoPlay'),
                Input({'type':'play_song','index':ALL}, 'n_clicks'))
def sound_selector(n):

    #file_names = ['6LACK.wav','canyoufeelit7thinning.mp3','barker1.wav','cali.wav', 'dogs.wav']
    

    button = ctx.triggered_id['index']
    #print(button)

    song = int(button.split('-')[0]) - 1
    names = button.split('-')[1]

    print(song, names)

    file_name = pd.read_csv('song_names.csv').query('name == @names').reset_index(drop = True)['song'].iloc[song]

    print(file_name)

    sound_filename = 'songs/' +file_name # replace with your own .mp3 file
    encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())
    src = 'data:audio/mpeg;base64,{}'.format(encoded_sound.decode())

    return src, True

@app.callback(Output({'type':'play_song','index':MATCH}, 'color'),
                Input({'type':'play_song','index':MATCH}, 'n_clicks'),
                State({'type':'play_song', 'index':MATCH}, 'color')
)
def update_color(n, color):
    if color == 'blue':
        return 'orange'
    else:
        return 'blue'
#analytics = dash_user_analytics.DashUserAnalytics(app, automatic_routing=False)

# @app.callback(Output('content', 'children'),
#                 [Input('url', 'pathname')])
# def display_content(pathname):
#     page_name = app.strip_relative_path(pathname)
#     if not page_name:  # None or ''
#         return pages.customerbase.layout
#     elif page_name == 'churn':
#         return pages.churn.layout
#     elif page_name == 'summary':
#         return pages.summary.layout



if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1', port = 8050)
