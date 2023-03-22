import dash
#from scout_apm.flask import ScoutApm

app = dash.Dash(__name__, suppress_callback_exceptions = True,
    title = 'Walk Up Song App', 
    #update_title=None, 
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    
)