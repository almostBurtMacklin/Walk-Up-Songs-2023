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

df.to_csv('button_maker.csv')

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
                        # dmc.Stack(
                        #     align = 'center',
                        #     spacing = 28,
                        #     #direction = 'row',
                        #     children=[
                        #         html.Audio(
                        #             id='audio-player',
                        #             #src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode()),
                        #             controls=True,
                        #             autoPlay=False,
                        #         ),
                        #         dmc.Paper(
                        #             style = {'width':'50%'},
                        #             shadow = 'md',
                        #             radius = 'md',
                        #             withBorder=True,
                        #             p = 'sm',
                        #             children = [
                        #                 dmc.Stack(
                        #                     children = [
                        #                         dmc.Alert(
                        #                             id = 'dup-alert',
                        #                             children = "You have the same person in 2 different lineup spots!",
                        #                             title="Uh Oh!",
                        #                             color = 'red',
                        #                             hide = True,
                        #                         ),
                        #                         dmc.Title('Lineup', order = 4),
                        #                         dmc.Stack(
                        #                             children = child_list
                        #                         )
                        #                     ]
                        #                 )
                        #             ]
                        #         ),
                                
                        #         # dmc.Group(
                        #         #     children = [
                        #         #         dmc.Button('Play 1', id = {'type':'play_button', 'index':0}),
                        #         #         dmc.Button('Play 1', id = {'type':'play_button', 'index':1}),
                        #         #         dmc.Button('Play 1', id = {'type':'play_button', 'index':2}),
                        #         #         dmc.Button('Play 1', id = {'type':'play_button', 'index':3}),
                        #         #         dmc.Button('Play 1', id = {'type':'play_button', 'index':4})
                        #         #     ]
                        #         # )
                        #     ]
                        # )
                    ]
                )
            ]
        )
    ]
)

# @app.callback(Output('audio-player', 'src'),
#                 Output('audio-player', 'autoPlay'),
#                 Input({'type':'play_song','index':ALL}, 'n_clicks'))
# def sound_selector(n):

#     button = ctx.triggered_id['index']

#     names = button.split('-')[1]

#     df = pd.read_csv('position_key.csv')

#     intter = df.query('name == @names')['index'].iloc[0]


#     n_look = (int(intter) * 3)

#     print(n_look)

#     print('n_look index:', button.split('-')[-1])



#     print('n:' , n)
#     # print('n_look calc:', n_look)

    


#     if all(val == None for val in n):
#         return dash.no_update, False
    

#     if n[int(n_look)] is None:

#         print('field update')
#         #print(ctx.triggered_id, n[int(n_look)])

#         #file_names = ['6LACK.wav','canyoufeelit7thinning.mp3','barker1.wav','cali.wav', 'dogs.wav']
        

#         button = ctx.triggered_id['index']
#         #print(button)

#         song = int(button.split('-')[0]) - 1
#         names = button.split('-')[1]
#         #n_look = button.split('-')[-1]

#         #print(song, names)

#         file_name = pd.read_csv('song_names.csv').query('name == @names').reset_index(drop = True)['song'].iloc[song]

#         #print(file_name)

#         sound_filename = 'songs/' +file_name # replace with your own .mp3 file
#         encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())
#         src = 'data:audio/mpeg;base64,{}'.format(encoded_sound.decode())

#         gtresd

#         # try:
#         #     gtresd
#         # except:
#         #     print('working as expected')

#         #return src, False
    
#     else:
        

#         #print('printing in else rigger and n[nlook]', ctx.triggered_id, n[int(n_look)])

#         #file_names = ['6LACK.wav','canyoufeelit7thinning.mp3','barker1.wav','cali.wav', 'dogs.wav']
        

#         button = ctx.triggered_id['index']
#         #print(button)

#         song = int(button.split('-')[0]) - 1
#         names = button.split('-')[1]
#         n_look = button.split('-')[-1]

#         #print(song, names)

#         file_name = pd.read_csv('song_names.csv').query('name == @names').reset_index(drop = True)['song'].iloc[song]

#         #print(file_name)

#         sound_filename = 'songs/' +file_name # replace with your own .mp3 file
#         encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())
#         src = 'data:audio/mpeg;base64,{}'.format(encoded_sound.decode())

#         return src, True

# @app.callback(Output({'type':'play_song','index':MATCH}, 'style'),
#                 Input({'type':'play_song','index':MATCH}, 'n_clicks'),
#                 State({'type':'play_song', 'index':MATCH}, 'style')
# )
# def update_color(n, color):

#     if ctx.triggered_id is not None:
#         if color == {'background-color':navy}:
#             return {'background-color':grey}
#         else:
#             return {'background-color':navy}
#     else:
#         return dash.no_update
    
# @app.callback(Output('dup-alert', 'hide'),
#                 Input({'type':'lineup', 'index':ALL}, 'value'))
# def check_for_dups(n):
#     time.sleep(1.5)
#     df = pd.read_csv('position_key.csv')
#     return not df['name'].duplicated().any()
    
# @app.callback(Output({'type':'buttons', 'index':MATCH}, 'children'),
#                 Input({'type':'lineup', 'index':MATCH}, 'value'),
#                 State('testing-store', 'data')
#                 )
# def updtae_buttons(name, test):
#     global number_count
#     # pos = ctx.triggered_id['index']
#     # print('position:',pos)
#     # try:
#     #     df = pd.read_csv('position_key.csv')
#     # except:
#     #     print('broken')
#     #     df = pd.DataFrame()

#     # df.loc[pos -1,'name'] = name
#     # print(df)

#     # df = pd.concat([df, pd.DataFrame(data = [[name, number_count]], columns = ['name', 'position_key'])], ignore_index=True)
#     # print('dups')
#     # print(df)

#     # df.drop_duplicates(subset=['name'], keep = 'last', inplace=True)
#     # print('dropped dups')
#     # print(df)

#     # df['position_key'] = df.index + 1
#     # print('final')
#     # print(df)


#     if name is not None:

#         try:
#             pos = ctx.triggered_id['index']
#         except:
#             pos = ctx.outputs_list['id']['index']
#         #print('position:',pos)
        
#         df = pd.read_csv('position_key.csv')

#         df.loc[pos,'name'] = name
#         #print(df)

#         #print(name)
#         child = []
#         for i in range(3):
#             child.append(
#                 dmc.Button(f'Song {i + 1}', id = {'type':'play_song', 'index': f'{i + 1}-{name}-{pos}'}, style = {'background-color':navy}, n_clicks=None),
#             )

#         #df = pd.concat([df, pd.DataFrame(data = [[name, number_count]], columns = ['name', 'position_key'])])
#         df.to_csv('position_key.csv', index=False)
#         #print(df)

#         number_count += 1
#         return child
#     # else:
#     #     indy = ctx.outputs_list['id']['index'] - 1
#     #     print(indy)
#     #     child = []
        
#     #     df = pd.read_csv('position_key.csv')
#     #     name = df.query('index == @indy')['name'].iloc[0]

#     #     for j in range(3):
#     #         child.append(
#     #             dmc.Button(f'Song {j + 1}', id = {'type':'play_song', 'index': f'{j + 1}-{name}-{number_count}'}, style = {'background-color':navy}, n_clicks=None),
#     #         )
#     #     return child
        


        

    
#analytics = dash_user_analytics.DashUserAnalytics(app, automatic_routing=False)

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
    app.run_server(debug=False, host = '127.0.0.1', port = 8050)
