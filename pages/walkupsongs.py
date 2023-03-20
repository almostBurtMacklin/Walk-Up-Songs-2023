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
                    id='audio-player-walkup',
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
                            id = 'lineup-stack',
                            #style= {'width':'75%'},
                            children = [
                                dmc.Group(
                                    #grow = True,
                                    position='apart',
                                    children = [
                                        dmc.Badge('4', color='gray', fullWidth=False, size='xl', radius=1, style = {'color':navy}),
                                        dmc.Text('James', align='center', size = 'lg', style = {'font-family':'IntegralCF-RegularOblique', 'color':navy}),
                                        dmc.Group(
                                            children = [
                                                dmc.Button('Song 1', style = {'background-color':navy}),
                                                dmc.Button('Song 2', style = {'background-color':navy}),
                                                dmc.Button('Song 3', style = {'background-color':navy}),
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
    ]
)

@app.callback(Output('lineup-stack', 'children'),
              Input('url','pathname'))
def update_lneup_stack(n):
    
    df = pd.read_csv('button_maker.csv')
    ndf = pd.read_csv('player_numbers.csv')
    
    players = df.name.unique()
    #songs = df.song.to_list()
    child = []
    
    for player in players:
        
        number = ndf.query('name == @player')['number'].iloc[0]
        
        child.append(
            dmc.Group(
                position = 'apart',
                children=[
                    dmc.Badge(str(number), color='gray', fullWidth=False, size='xl', radius=1, style = {'color':navy}),
                    dmc.Text(player, align='center', size = 'lg', style = {'font-family':'IntegralCF-RegularOblique', 'color':navy}),
                    dmc.Group(
                        #style = {'justify-content':'space-between'}
                        children = [
                            dmc.Button('Song 1', style = {'background-color':navy}, id = {'type':'song','index':f'0-{player}'}),
                            dmc.Button('Song 2', style = {'background-color':navy}, id = {'type':'song','index':f'1-{player}'}),
                            dmc.Button('Song 3', style = {'background-color':navy}, id = {'type':'song','index':f'2-{player}'}),
                        ]
                    )            
                ]
            )
        )
        
    return child
        
    
    
@app.callback(Output('audio-player-walkup', 'src'),
                Output('audio-player-walkup', 'autoPlay'),
                Input({'type':'song','index':ALL}, 'n_clicks'))
def sound_selector(n):

    button = ctx.triggered_id['index']

    names = button.split('-')[1]

    df = pd.read_csv('position_key.csv')

    intter = df.query('name == @names')['index'].iloc[0]


    n_look = (int(intter) * 3) + int(button.split('-')[0])

    print(n_look)

    print('n_look index:', button.split('-')[-1])



    print('n:' , n)
    # print('n_look calc:', n_look)

    


    if all(val == None for val in n):
        return dash.no_update, False
    

    if n[int(n_look)] is None:

        print('field update')
        #print(ctx.triggered_id, n[int(n_look)])

        #file_names = ['6LACK.wav','canyoufeelit7thinning.mp3','barker1.wav','cali.wav', 'dogs.wav']
        

        button = ctx.triggered_id['index']
        #print(button)

        song = int(button.split('-')[0]) - 1
        names = button.split('-')[1]
        #n_look = button.split('-')[-1]

        #print(song, names)

        file_name = pd.read_csv('song_names.csv').query('name == @names').reset_index(drop = True)['song'].iloc[song]

        #print(file_name)

        sound_filename = 'songs/' +file_name # replace with your own .mp3 file
        encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())
        src = 'data:audio/mpeg;base64,{}'.format(encoded_sound.decode())

        gtresd

        # try:
        #     gtresd
        # except:
        #     print('working as expected')

        #return src, False
    
    else:
        

        #print('printing in else rigger and n[nlook]', ctx.triggered_id, n[int(n_look)])

        #file_names = ['6LACK.wav','canyoufeelit7thinning.mp3','barker1.wav','cali.wav', 'dogs.wav']
        

        button = ctx.triggered_id['index']
        #print(button)

        song = int(button.split('-')[0]) - 1
        names = button.split('-')[1]
        n_look = button.split('-')[-1]

        #print(song, names)

        file_name = pd.read_csv('song_names.csv').query('name == @names').reset_index(drop = True)['song'].iloc[song]

        #print(file_name)

        sound_filename = 'songs/' +file_name # replace with your own .mp3 file
        encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())
        src = 'data:audio/mpeg;base64,{}'.format(encoded_sound.decode())

        return src, True
    
@app.callback(Output({'type':'song','index':MATCH}, 'style'),
                Input({'type':'song','index':MATCH}, 'n_clicks'),
                State({'type':'song', 'index':MATCH}, 'style')
)
def update_color(n, color):

    if ctx.triggered_id is not None:
        if color == {'background-color':navy}:
            return {'background-color':grey}
        else:
            return {'background-color':navy}
    else:
        return dash.no_update