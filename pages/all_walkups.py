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

df = pd.read_csv('song_names.csv')

button_child = []

for i in df.name.unique():
    name = i
    
    temp = df.query('name == @name')
    nums = pd.read_csv('player_numbers.csv').query('name == @name')['number'].iloc[0]
    
    button_child.append(
        dmc.Group(
            position = 'apart',
            children=[
                dmc.Badge(str(nums), color='gray', fullWidth=False, size='xl', radius=1, style = {'color':navy}),
                dmc.Text(name, align='center', size = 'lg', style = {'font-family':'IntegralCF-RegularOblique', 'color':navy}),
                dmc.Group(
                    #style = {'justify-content':'space-between'}
                    children = [
                        dmc.Button('Song 1', style = {'background-color': navy},id = {'type':'allsong','index':temp['song'].iloc[0]}),
                        dmc.Button('Song 2', style = {'background-color': navy},id = {'type':'allsong','index':temp['song'].iloc[1]}),
                        dmc.Button('Song 3', style = {'background-color': navy},id = {'type':'allsong','index':temp['song'].iloc[2]}),
                    ]
                )            
            ]
        )

    )


layout = html.Div(
    children = [
        dmc.Stack(
            align = 'center',
            spacing = 16,
            #direction = 'row',
            children=[
                html.Audio(
                    id='audio-player-all',
                    #src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode()),
                    controls=True,
                    autoPlay=False,
                    style = {'margin-top':'16px'}
                ),
                dmc.Paper(
                    style = {'width':'50%'},
                    shadow = 'md',
                    radius = 'md',
                    withBorder=True,
                    p = 'sm',
                    children = [
                        dmc.Stack(
                            children = button_child
                        )
                    ]
                )
            ]
        )
    ]
)

@app.callback(Output('audio-player-all', 'src'),
                Output('audio-player-all', 'autoPlay'),
                Input({'type':'allsong','index':ALL}, 'n_clicks'))
def sound_selector(n):


    file_name = ctx.triggered_id['index']
    
    #file_name = pd.read_csv('other_songs.csv')['song'].iloc[location]

    #print(file_name)

    sound_filename = 'songs/' +file_name # replace with your own .mp3 file
    encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())
    src = 'data:audio/mpeg;base64,{}'.format(encoded_sound.decode())

    return src, True