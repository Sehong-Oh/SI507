import snscrape.modules.twitter as sntwitter
import pandas as pd
import numpy as np
import time
from polygon import RESTClient
from typing import cast
from urllib3 import HTTPResponse
import twitter
import snscrape.modules.twitter as sntwitter
from time import sleep
from datetime import datetime
import csv
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import ast
import json
from function import get_price_date, get_stock_data

POLYGON_API_KEY = "e3rteVluK3B4muCkvySKP9_zrvVQV8rr"
client = RESTClient(api_key = POLYGON_API_KEY) # POLYGON_API_KEY is used

twitter_consumer_key = "U2n0CHFMm3NvCVrG62rHBJ19T"
twitter_consumer_secret = "miN4WIXIZyuiJFdXM4yCis0koIQ3RB0fBMllfFNQeXOanNXhja"  
twitter_access_token = "1598850371471843328-657PzIhW2tpLhgYQLZsQAeHwX9KaJ0"
twitter_access_secret = "NIXQ01t1kcdsI8VsAyoQ65b2QeMQd1vAuHS2kz4yN7CM7"

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)


###############
## Data Load ##
###############

data = {}
data['Tesla'] = {"Tweets":"", "Stock":""}
data['Intel'] = {"Tweets":"", "Stock":""}
data['Nvidia'] = {"Tweets":"", "Stock":""}

with open('snscrape/Tweets_tesla_from_live.csv', encoding='UTF-8') as f:
    tweet_tesla = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
with open('snscrape/Tweets_intel_from_live.csv', encoding='UTF-8') as f:
    tweet_intel = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
with open('snscrape/Tweets_nvidia_from_live.csv', encoding='UTF-8') as f:
    tweet_nvidia = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

with open('tesla_stock_day.csv', encoding='UTF-8') as f:
    tesla_stock = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
with open('intel_stock_day.csv', encoding='UTF-8') as f:
    intel_stock = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]          
with open('nvidia_stock_day.csv', encoding='UTF-8') as f:
    nvidia_stock = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
              

data['Tesla']['Tweets'] = tweet_tesla
data['Tesla']['Stock'] = tesla_stock
data['Intel']['Tweets'] = tweet_intel
data['Intel']['Stock'] = intel_stock
data['Nvidia']['Tweets'] = tweet_nvidia
data['Nvidia']['Stock'] = nvidia_stock

print("Which company are you interested in?")
print("Tesla")
print("Intel")
print("Nvidia")
question1 = input("Please, tpye one of the names exactly: ")
print("")
next = True
if question1.lower() == "tesla":
    company = "Tesla"
elif question1.lower() == "intel":
    company = "Intel"
elif question1.lower() == "nvidia":
    company = "Nvidia"
else:
    print("Please, try again")
    next = False

if next:
    print(f"1. Do you want to see the {company} stock price in 2022?")
    print("2. Do you wnat to select a certain period")
    print(f"3. Do you want to see the tweets metioning {company} by Livemint")
    print("4. Quit")
    question2 = 0
    while question2 != 1 or 2 or 3 or 4: 
        question2 = input("Please, type a number: ")
        print("")
        question2 = int(question2)
        if question2 == 4:
            break
        elif question2 == 1:
            new_x, new_y = get_price_date(data[company]['Stock'])
            break
        elif question2 == 2:
            print("Unfortunatley, we only provide the data from 2022-01-01 to 2022-12-12")
            date1 = input("Please, tpye the starting date with a yyyy-mm-dd form: ")
            date1 = date1.split("-")
            date1 = (int(date1[0]), int(date1[1]), int(date1[2]))
            date2 = input("Please, tpye the ending date with a yyyy-mm-dd form from: ")
            date2 = date2.split("-")
            date2 = (int(date2[0]), int(date2[1]), int(date2[2]))
            new_x, new_y = get_price_date(data[company]['Stock'],start_date=date1,end_date=date2)
            break
        elif question2 == 3:
            print("How many tweets do you want see? You will can the lastest tweets")
            print("We have", len(data[company]['Tweets']),"tweets this year")
            number = int(input("Please, type a number: "))
            for i in range(0,number):
                print("Date:", data[company]['Tweets'][i]['Datetime'][:16])
                print("Tweet:", data[company]['Tweets'][i]['Content'])
                print("")
            print(f"Now you can choose one date above and look at the variation of {company} stock price")
            date3 = input("Please, copy and past the date: ")
            get_stock_data(company, date3)
            break
