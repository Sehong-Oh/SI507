import csv
import json
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

##################
## Save as json ##
##################

with open("structure.json","w") as f:
    json.dump(data,f, indent=4)

# print(len(data['Tesla']['Tweets']))
# print(len(data['Intel']['Tweets']))
# print(len(data['Nvidia']['Tweets']))

#########################
## Check the structure ##
#########################

print("Companies", type(data), "consist of three companies below")
for key, value in data.items():
    print(key, type(data[key]), "consists of two below")
    for key1, value1 in data[key].items():
        print(key1, type(data[key][key1]))