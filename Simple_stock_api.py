from polygon import RESTClient
from datetime import datetime
from typing import cast
from urllib3 import HTTPResponse
import csv
import json

POLYGON_API_KEY = "" # Type your key

client = RESTClient(api_key = POLYGON_API_KEY) # POLYGON_API_KEY is used

#################
## Gather data ##
#################

company = "INTC" # You should type a stock code instead of a real company name.

aggs = cast(
    HTTPResponse,
    client.get_aggs(
        company,
        1,
        "day",        # You can choose one of [minute / hour / day / month / year] 
        "2022-01-01",
        "2022-12-12",
        raw=True,
    ),
)
# print(aggs.geturl())
# print(aggs.status)

##################
## Convert data ##
##################

data = aggs.data
str_data = data.decode('utf-8')
parsing = json.loads(str_data)
new_data = parsing['results']

remove_list = ['v','vw'] # You can remove data that you don't need

for i in parsing['results']:
    for key in remove_list:
        del i[key]
        

# Print the preprocessed data to check
# print(new_data)


###############
## Save data ##
###############

myFile = open('intel_stock_day.csv', 'w', encoding='UTF-8')
writer = csv.writer(myFile)
writer.writerow(['Open', 'Closed', 'Highest', 'lowest','Timestamp', 'Trading volume'])
for dictionary in new_data:
    writer.writerow(dictionary.values())
myFile.close()

with open('tesla_stock.csv', encoding='UTF-8') as f:
    retrieved_list = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]