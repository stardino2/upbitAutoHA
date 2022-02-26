import plotly.graph_objects as go 

def showFigure(df):
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df.open,
                                            high=df.high, low=df.low,
                                            close=df.close)]) 
    fig.update_layout(title = 'TBD', xaxis_title = 'time', yaxis_title = 'Price') 
    fig.show()
