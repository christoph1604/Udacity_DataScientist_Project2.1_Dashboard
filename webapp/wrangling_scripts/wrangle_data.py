import pandas as pd
import plotly.graph_objs as go

# Read in the preprocessed dataset containing COVID-19 cases in the Spanish regions
# Contains small transformations to fit the data to the format required by the plotly methods

def return_figures():
    """Creates four plotly visualizations
    Args:
        None
    Returns:
        list (dict): list containing the four plotly visualizations
    """
    
    df = pd.read_csv("./data/covid19-spain-cases_transformed.csv")    
    figures = []    
    
    # Graph 1: Development of COVID-19 cases in Spain (sum)
    graph_one = []
    df_sum = df.groupby("Date").sum().Cases
    x_val = df_sum.index.to_list()
    y_val = df_sum.to_list()
    
    graph_one.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines'
          )
        )
        
    layout_one = dict(title = 'Development of COVID-19 cases in Spain',
        xaxis = dict(title = 'Date'),
        yaxis = dict(title = 'Number of cases'),
    )
    
    figures.append(dict(data=graph_one, layout=layout_one))
         
    
    # Graph 2: Development of COVID-19 cases in Spanish regions
    graph_two = [] 
    regionList = df.Region.unique().tolist()
    
    for region in regionList:
        x_val = df[df["Region"] == region].Date.tolist()
        y_val = df[df["Region"] == region].Cases.tolist()
    
        graph_two.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines', 
          name = region
          )
        )
        
    layout_two = dict(title = 'Development of COVID-19 cases in Spanish regions',
        xaxis = dict(title = 'Date'),
        yaxis = dict(title = 'Number of cases'),
        )
       
    figures.append(dict(data=graph_two, layout=layout_two))
    
    
    # Graph 3: Number of COVID-19 cases in Spanish regions at 29/04/2020 (bar plot)
    graph_three = []
    df_newest=df[df["Date"]=="2020-04-29"].sort_values(by=["Cases"], ascending=False)
    x_val= df_newest["Region"]
    y_val= df_newest["Cases"]
    
    graph_three.append(
          go.Bar(
          x = x_val,
          y = y_val
          )
        )
        
    layout_three = dict(title = 'Count of COVID-19 cases in Spanish regions at 29/04/2020',
        xaxis = dict(title = 'Region'),
        yaxis = dict(title = 'Number of cases'),
        )
        
    figures.append(dict(data=graph_three, layout=layout_three))
    
    # Graph 4: Number of COVID-19 related fatalities in Spanish regions at 29/04/2020 (pie plot)
    graph_four = []
    df_fatality=df[df["Date"]=="2020-04-29"].sort_values(by=["Dead"], ascending=False)
    x_val= df_fatality["Region"]
    y_val= df_fatality["Dead"]
    
    graph_four.append(
          go.Pie(
          labels = x_val,
          values = y_val
          )
        )
        
    graph_four_margin=dict(l=40, r=40, b=140, t=40, pad=0 )
        
    layout_four = dict(title = 'Count of COVID-19 fatalities in Spanish regions at 29/04/2020', margin=graph_four_margin)
        
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures