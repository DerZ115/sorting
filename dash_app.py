from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from pathlib import Path
import numpy as np

result_path = Path("results")

data = {
    "sort_type": [],
    "sort_name": [],
    "n": [],
    "time_mean": [],
    "time_std": []
    }

for type_dir in result_path.iterdir():
    sort_type = type_dir.stem[:-1]
    for file in type_dir.iterdir():
        sort_name = file.stem
        df = pd.read_csv(file, header=None)
        n = df.iloc[:,0].values
        df = df.iloc[:,1:]
        data["time_mean"].append(df.mean(axis=1).values)
        data["time_std"].append(df.std(axis=1).values)
        data["n"].append(n)
        data["sort_type"].append(np.full((len(n)), sort_type))
        data["sort_name"].append(np.full((len(n)), sort_name))
        
data = {key: np.concatenate(val) for key, val in data.items()}

data = pd.DataFrame(data)
data['time_mean'] = data['time_mean'] / 10**9
data['time_std'] = data['time_std'] / 10**9


app = Dash()

app.layout = [
    html.H1(children='Sorting Algorithms', style={'textAlign':'center'}),
    dcc.Dropdown(data.sort_name.unique(), 
                 ["SelectionSort"], 
                 id='dropdown-sort',
                 multi=True),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-sort', 'value')
)
def update_graph(value):
    data_filtered = data[data.sort_name.isin(value)]
    return px.line(data_filtered, x='n', y='time_mean', color="sort_name")

if __name__ == '__main__':
    app.run(debug=True)