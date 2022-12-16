# FA22 SI507 Final project
## Introduction
In this project, the relationship between Tweets and stock prices is analyzed. This project is simple however, it can be a stepping stone for further research.
The project provides simple code to collect data from Twitter and Polygon(Stock market data). You can set a period that you want to collect data but, The data of 2022 are dealt with in this project.
###
**final_project.py** is the main python file to run the program. Before running the code, we need to download **all local data files** and **function.py**. You can also generate new local files by yourself with Simple_stock_api.py for stock market data and snscrape.py for twitter data. Simple_twitter_api.py can be also used to gather Twitter data however, it sometime does not work due to the conflict of the library. Please check the required package list at the bottom of README

## Data source
### Twitter
 - It requires OAuth and you can find how to get the API keys (https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).
 - We use tweets having some keywords that a certain account has mentioned.
 - The official Twitter API has a lot limitation so, we also use snscrape to collect more data.

### Polygon(Stock market data)
 - You can get a free API key on the official website (https://polygon.io/).
 - We can get a stock quote with it.

## Data structure
 - In this project, the main data set consists of a nested dictionary. The dictionary has three keys with company names (Tesla, Intel, and Nvidia). Each company consists of a dictionary with Twitter and stock data (Key names are tweets and stock respectively). Tweets and stock have a list having much information such as date, contents of tweets, and stock quote. You can check the data structure by looking at **structure.json** file.
 - For example, Tesla has two keys. One is tweets and the other is stock. In the tweets, there is a list having dictionaries that consists of URL, Date, Content, and so on. The reason why there is a list of dictionaries is that the data is stored in chronological order. In the stock, there is also a list having dictionaries in chronological order. Each element of the list has an open stock price, the highest stock price, and so on.

## File list
### Main python file
- final_project.py (It has to be with function.py)
- You can run this file with local data files and a function file. In this project, I divided caching files because gathering Twitter data needs much time. So, I recommend that you download my local data files first and run this code to test. All local files below are needed.
- Polygon API key is needed to run the code. This code has a part getting data from the Web directly.

### Data gathering files
- snscrape.py (For Twitter)
- stock_api.py (For stock market information)
- twitter_api.py (For Twitter, this is optional)

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
