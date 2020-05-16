import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    
    df = pd.read_csv("./data/covid19-spain-cases_transformed.csv")
    regionList = df.Region.unique().tolist()
    
    graph_one = [] 
    
    for region in regionList:
        x_val = df[df["Region"] == region].Date.tolist()
        y_val = df[df["Region"] == region].Cases.tolist()
    
        graph_one.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines', 
          name = region
          )
        )
        
    layout_one = dict(title = 'Development of COVID-19 cases in Spanish regions',
        xaxis = dict(title = 'Date'),
        yaxis = dict(title = 'Number of cases'),
        )
    
    
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))

    return figures