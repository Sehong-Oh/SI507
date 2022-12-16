import time
from typing import cast
from polygon import RESTClient
from urllib3 import HTTPResponse
from time import sleep
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json

POLYGON_API_KEY = "e3rteVluK3B4muCkvySKP9_zrvVQV8rr"
client = RESTClient(api_key = POLYGON_API_KEY)

def get_price_date(stock_data,start_date=None,end_date=None):
    x = []
    y1 = []
    y2 = []
    for one in stock_data:
        date = int(int(one['Timestamp']) / 1000)
        x.append(datetime.fromtimestamp(date))
        y1.append(one['Closed'])
        y2.append(one['Trading volume'])
        
    if start_date != None and end_date != None:
        s_year, s_month, s_day = start_date
        e_year, e_month, e_day = end_date
        d1 = datetime(s_year, s_month, s_day)
        d2 = datetime(e_year, e_month, e_day)
        for date in x:
            if date < d1:
                x = x[1:]
        for date in x:
            if date > d2:
                x = x[:-1]

    fig = go.Figure()

    # Set x-axis title
    fig.update_xaxes(title_text="Time")
    fig.update_yaxes(title_text="Price")   


    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
                go.Scatter(x=x, y=y1,
                mode='lines', 
                name='Price'))
    fig.add_trace(
                go.Scatter(x=x, y=y2,
                mode='lines', 
                name='Volume'),
                secondary_y=True,
                )                        
    fig.update_layout(autotypenumbers='convert types')

    # Add figure title
    fig.update_layout(
        title_text=f"Stock Price and Volume from {x[0]} to {x[-1]}"
    )
    # Set x-axis title
    fig.update_xaxes(title_text="Time")

    # Set y-axes titles
    fig.update_yaxes(title_text="Stock price", secondary_y=False)
    fig.update_yaxes(title_text="Vomlue", secondary_y=True)
    fig.show()     
    return x, y1, y2

def get_stock_data(company, date, range = 30):
    if company == "Tesla":
        code = "TSLA"
    elif company == "Intel":
        code = "INTC"
    elif company == "Nvidia":
        code = "NVDA"
    mmddyy = date
    a = date.split(' ')
    y, m, d = a[0].split('-')
    hour, minuite = a[1].split(':')
    date_time = datetime(int(y), int(m), int(d), int(hour), int(minuite))
    date_time1 = (time.mktime(date_time.timetuple()))


    aggs = cast(
        HTTPResponse,
        client.get_aggs(
            code,
            1,
            "minute",
            str(int(date_time1)-600)+"000",
            str(int(date_time1)+int(range) * 60)+"000",
            raw=True,
        ),
    )

    data = aggs.data
    str_data = data.decode('utf-8')
    parsing = json.loads(str_data)
    try:
        new_data = parsing['results']
    except:
        print("Please type a valid date. The stock market was probably closed that date")
        exit()

    remove_list = ['v','vw','o','h','l']
    for i in parsing['results']:
        for key in remove_list:
            del i[key]
    
    
    x = []
    y1 = []
    y2 = []    

    for one in new_data:
        date = int(int(one['t']) / 1000)
        x.append(datetime.fromtimestamp(date))
        y1.append(one['c'])
        y2.append(one['n'])
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
                go.Scatter(x=x, y=y1,
                mode='lines', 
                name='Price'))
    fig.add_trace(
                go.Scatter(x=x, y=y2,
                mode='lines', 
                name='Volume'),
                secondary_y=True,
                )                        
    fig.update_layout(autotypenumbers='convert types')

    # Add figure title
    fig.update_layout(
        title_text=f"Stock Price and Volume around {mmddyy}"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Time")

    # Set y-axes titles
    fig.update_yaxes(title_text="Stock price", secondary_y=False)
    fig.update_yaxes(title_text="Vomlue", secondary_y=True)               
    
    fig.show()

        
