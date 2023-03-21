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
from app import app

navy = '#00244a'
grey = '#acafa6'

layout = html.Div(
    children = [
        dmc.Stack(
            align = 'center',
            spacing = 16,
            #direction = 'row',
            children=[
                html.Audio(
                    id='audio-player-pre',
                    #src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode()),
                    controls=True,
                    autoPlay=False,
                    style = {'margin-top':'16px'}
                ),
                dmc.Paper(
                    style = {'width':'75%'},
                    shadow = 'md',
                    radius = 'md',
                    withBorder=True,
                    p = 'sm',
                    children = [
                        dmc.SimpleGrid(
                            cols = 4,
                            children = [
                                dmc.Button('Star Spangled Banner',className = 'classic_button', id = {'type':'pre', 'index':0}),
                                dmc.Button('Can You Feel It',className = 'classic_button', id = {'type':'pre', 'index':1}),
                                dmc.Button('Locksley (Panthers Win)',className = 'classic_button', id = {'type':'pre', 'index':2}),
                                dmc.Button('Angels in the Outfield', className = 'classic_button', id = {'type':'pre', 'index':3}),
                                dmc.Button('Jeopardy Theme', className = 'classic_button', id = {'type':'pre', 'index':4}),
                                dmc.Button('Little Less Conversation', className = 'classic_button', id = {'type':'pre', 'index':5}),
                                dmc.Button('Player Intro (FOX)', className = 'classic_button', id = {'type':'pre', 'index':6}),
                                dmc.Button('On To The Next', className = 'classic_button', id = {'type':'pre', 'index':7}),
                                dmc.Button('Pre Game Rumble', className = 'classic_button', id = {'type':'pre', 'index':8}),
                                dmc.Button('Barker Walk Up (Lineups)', className = 'classic_button', id = {'type':'pre', 'index':9}),
                                dmc.Button('Welcome To The Jungle', className = 'classic_button', id = {'type':'pre', 'index':10}),
                                dmc.Button('Opposing Team Mound Visit', className = 'classic_button', id = {'type':'pre', 'index':11}),
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

    
    
    
    
@app.callback(Output('audio-player-pre', 'src'),
                Output('audio-player-pre', 'autoPlay'),
                Input({'type':'pre','index':ALL}, 'n_clicks'))
def sound_selector(n):


    location = ctx.triggered_id['index']
    
    file_name = pd.read_csv('other_songs.csv')['song'].iloc[location]

    #print(file_name)

    sound_filename = 'songs/' +file_name # replace with your own .mp3 file
    encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())
    src = 'data:audio/mpeg;base64,{}'.format(encoded_sound.decode())

    return src, True

    
# @app.callback(Output({'type':'song','index':MATCH}, 'style'),
#                 Input({'type':'song','index':MATCH}, 'n_clicks'),
#                 State({'type':'song', 'index':MATCH}, 'style')
# )
# def update_color(n, color):

#     if ctx.triggered_id is not None:
#         if color == {'background-color':navy}:
            
#             loca = int(ctx.triggered_id['index'].split('-')[0])
#             playa = ctx.triggered_id['index'].split('-')[1]
            
            
#             df = pd.read_csv('button_maker.csv')
#             song_name = df.query('name == @playa')['song'].iloc[loca]
#             print(song_name)
#             df.loc[df['song'] == song_name, 'color'] = grey
            
            
#             print(df)
#             df.to_csv('button_maker.csv', index=False)
#             #print(ctx.triggered_id)
            
#             return {'background-color':grey}
#         else:
#             return {'background-color':navy}
#     else:
#         return dash.no_update