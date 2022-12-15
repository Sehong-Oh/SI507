# FA22 SI507 Final project
## Introduction
In this project, the relationship between Tweets and stock prices is analyzed. This project is simple however, it can be a stepping stone for further research.
The project provides simple code to collect data from Twitter and Polygon(Stock market data). You can set a period that you want to collect data but, The data of 2022 are dealt with in this project.

## Data source
### Twitter
 - It requires OAuth and you can find how to get the API keys (https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).
 - We use tweets having some keywords that a certain account has mentioned.
 - The official Twitter API has a lot limitation so, we also use snscrape to collect more data.

### Polygon(Stock market data)
 - You can get a free API key on the official website (https://polygon.io/).
 - We can get a stock quote with it.

## Data structure
 - In this project, the main data set consists of a nested dictionary. 

## File list
### Main python file
- final_project.py
- You can run this file with local data files. In this project, I divided caching files because gathering Twitter data needs much time. So, I recommend that you download my local data files first and run this code to test. All local files below are needed.
- Polygon API key is needed to run the code. This code has a part getting data from the Web directly.

### Data gathering files
- Twitter.py
- stock_api.py
- twitter_api.py

### Local data files
- Tweets_tesla_from_live.csv
- Tweets_intel_from_live.csv
- Tweets_nvidia_from_live.csv
- tesla_stock_day.csv
- intel_stock_day.csv
- nvidia_stock_day.csv

## Required Packages
- pandas 
- svscrape
- twitter
- polygon
- typing
- urllib3
- datetime
- numpy
- plotly
