import twitter
import csv

# Put your keys below
twitter_consumer_key = ""
twitter_consumer_secret = ""  
twitter_access_token = ""
twitter_access_secret = ""

twitter_api = twitter.api.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)


#################
## Gather data ##
#################

# You can change an account here
# This is to get Twitter data from a certain account
account = "@livemint"
statuses = twitter_api.GetUserTimeline(screen_name=account, count=200, include_rts=True, exclude_replies=False)

livemint_list = []
for t in statuses:
    dic = {}
    dic['data'] = t.created_at[:10]
    dic['tweet'] = t.text
    dic['hashtags'] = t.hashtags
    livemint_list.append(dic)

# print(livemint_list)



###############
## Save data ##
###############

# This is to save Twitter data as a csv file
file_name = "livemint_tweets.csv"
myFile = open(file_name, 'w', encoding='UTF-8')
writer = csv.writer(myFile)
writer.writerow(['Data', 'Tweet', 'Hashtags'])
for dictionary in livemint_list:
    writer.writerow(dictionary.values())
myFile.close()

# This to open a csv file
with open('livemint_tweets.csv', encoding='UTF-8') as f:
    retrieved_list = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

# print(retrieved_list)
