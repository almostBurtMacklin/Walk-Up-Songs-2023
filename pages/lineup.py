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


number_count = 1

server = app.server

navy = '#00244a'
grey = '#acafa6'

df = pd.read_csv('player_numbers.csv')

listy = df.name.to_list()

#pd.DataFrame(columns = ['name', 'position_key']).to_csv('position_key.csv', index = False)

# df = pd.read_csv('position_key.csv')

# child_list = []

# for j in range(9):
#     #indy = j - 1
#     name = df.query('index == @j')['name'].iloc[0]

#     child_list.append(
#         dmc.Group(
#             grow = True,
#             children = [
#                 #dmc.Badge(id={'type':'number', 'index':j}, color = 'gray', children = [' '], fullWidth=False),
#                 dmc.Select(data = [{'label':i, 'value':i} for i in names], id = {'type':'lineup','index':j}, value = name),
#             ]
#         )
#     )




layout = html.Div(
    id='content',
    style={'margin-top':'70px'},
    children = [
        dmc.Stack(
            align = 'center',
            spacing = 28,
            #direction = 'row',
            children=[
                # html.Audio(
                #     id='audio-player',
                #     #src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode()),
                #     controls=True,
                #     autoPlay=False,
                # ),
                dmc.Paper(
                    style = {'width':'50%'},
                    shadow = 'md',
                    radius = 'md',
                    withBorder=True,
                    p = 'sm',
                    children = [
                        dmc.Stack(
                            children = [
                                dmc.Alert(
                                    id = 'dup-alert',
                                    children = "You have the same person in 2 different lineup spots!",
                                    title="Uh Oh!",
                                    color = 'red',
                                    hide = True,
                                ),
                                dmc.Title('Set Lineup', order = 4, style = {'font-family':'IntegralCF-RegularOblique', 'color':navy}),
                                dmc.Group(
                                    grow = True,
                                    align = 'apart',
                                    children = [
                                        dmc.Button('Edit', id = 'edit_button', color = 'gray'),
                                        dmc.Button('Submit', id = 'submit_button', style = {'background-color':navy}),
                                    ]
                                ),
                                dmc.Stack(
                                    id = 'lineup_list',
                                    children = [
    
                                    ]
                                )
                            ]
                        )
                    ]
                ),
            ]
        )
    ]
)


@app.callback(Output('lineup_list', 'children'),
              Input('url' ,'pathname')
)
def initalize_dropdown(n):
    df = pd.read_csv('position_key.csv')

    child_list = []

    for j in range(9):
        #indy = j - 1
        name = df.query('index == @j')['name'].iloc[0]

        child_list.append(
            dmc.Group(
                grow = True,
                children = [
                    #dmc.Badge(id={'type':'number', 'index':j}, color = 'gray', children = [' '], fullWidth=False),
                    dmc.Select(data = [{'label':i, 'value':i} for i in listy], id = {'type':'lineup','index':j}, value = name, disabled=True),
                ]
            )
        )

    return child_list

    
# @app.callback(Output('dup-alert', 'hide'),
#                 Input('submit-button', 'n_clicks'))
# def check_for_dups(n):
#     time.sleep(1.5)
#     df = pd.read_csv('position_key.csv')
#     return not df['name'].duplicated().any()
    
@app.callback(Output({'type':'lineup', 'index':ALL}, 'disabled'),
              Output('dup-alert', 'hide'),
                Input('submit_button', 'n_clicks'),
                Input('edit_button', 'n_clicks'),
                State({'type':'lineup', 'index':ALL}, 'value'),
                )
def updtae_buttons(sub,ed, n):
    trigger = ctx.triggered_id
    if trigger == 'edit_button':
        return [False, False, False,False, False, False,False, False, False], True
    
    elif trigger == 'submit_button':
        if len(n) == len(set(n)):
            dups = False
        else:
            return [False, False, False,False, False, False,False, False, False], False
        #stop
        
        #print('position:',pos)

        pos_col = pd.Series(range(9))
        
        df = pd.DataFrame()
        df['index'] = pos_col
        df['name'] = n

        # df.loc[pos,'name'] = name
        # #print(df)

        # #print(name)
        # child = []
        # for i in range(3):
        #     child.append(
        #         dmc.Button(f'Song {i + 1}', id = {'type':'play_song', 'index': f'{i + 1}-{name}-{pos}'}, style = {'background-color':navy}, n_clicks=None),
        #     )

        #df = pd.concat([df, pd.DataFrame(data = [[name, number_count]], columns = ['name', 'position_key'])])
        df.to_csv('position_key.csv', index=False)

        df1 = pd.merge(df, pd.read_csv('song_names.csv'), how  = 'left')
        
        df1['color'] = '#00244a'
        
        df1.to_csv('button_maker.csv', index = False)
        #print(df)

        return  [True, True, True, True, True, True, True, True, True], True
    
    return dash.no_update
    # else:
    #     indy = ctx.outputs_list['id']['index'] - 1
    #     print(indy)
    #     child = []
        
    #     df = pd.read_csv('position_key.csv')
    #     name = df.query('index == @indy')['name'].iloc[0]

    #     for j in range(3):
    #         child.append(
    #             dmc.Button(f'Song {j + 1}', id = {'type':'play_song', 'index': f'{j + 1}-{name}-{number_count}'}, style = {'background-color':navy}, n_clicks=None),
    #         )
    #     return child
        


        

    




if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1', port = 8050)
