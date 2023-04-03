import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import random as rd
import webbrowser
import os
classes=[]
desc=[]
type=[]
for i in range(100):
    a=rd.randint(0,7)
    classes.append(a)
    if a==0:
        desc.append("Safe")
    elif a==1:
        desc.append("Hair and Makeup")
    elif a==2:
        desc.append("Infotainment")
    elif a==3:
        desc.append("Texting on left")
    elif a==4:
        desc.append("Texting on right")
    elif a==5:
        desc.append("Talking on left")
    elif a==6:
        desc.append("Talking on right")
    elif a==7:
        desc.append("Drowsy")
    if i<=99:
        type.append("History Drive")

for i in range(16):
    type.append("Last Drive")
for i in range(1):
    classes.append(5)
    desc.append("Talking on left")
for i in range(2):
    classes.append(6)
    desc.append("Talking on right")
for i in range(2):
    classes.append(2)
    desc.append("Infotainment")
for i in range(2):
    classes.append(0)
    desc.append("Safe")
for i in range(5):
    classes.append(7)
    desc.append("Drowsy")
for i in range(1):
    classes.append(4)
    desc.append("Texting on right")
for i in range(2):
    classes.append(3)
    desc.append("Texting on left")
for i in range(1):
    classes.append(1)
    desc.append("Hair and Makeup")

df1=pd.DataFrame({"Type":type,"Subject":classes,"Desc":desc})
df1.to_csv("drive1.csv",index=False)



external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout=html.Div([
    html.Div([
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                {"label":x,"value":x} for x in sorted(df1.Type.unique())
            ],
            value='Desc',
            multi=False,
            clearable=False,
            style={'width': "40%",
                   'backgroundColor': '#f9f9f9'}
        )
    ]),


    html.Div([
        dcc.Graph(id='the_graph',figure={})
    ]),

])



@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]

)

def update_graph(value):
    print(value)
    dff=df1[df1["Type"]==value]
    print(dff.head())
    piechart=px.pie(
        data_frame=dff,
        names="Desc",
        hole=.1,
    )
    return(piechart)

if __name__ == '__main__':
    app.run_server()
    webbrowser.open_new_tab("http://localhost:63342/Dataset_new/fds/Fds%20project/final/index.html?_ijt=iam4fvd39i8khf50b4mipvo3ag&_ij_reload=RELOAD_ON_SAVE")
