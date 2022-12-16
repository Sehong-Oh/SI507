import pandas as pd
import warnings
import snscrape.modules.twitter as sntwitter
from time import sleep
import datetime
import csv
warnings.filterwarnings(action='ignore')

###############
## Functions ##
###############

# Return : DF (url, time, id, content, username)
def read_tweet_list(twitterName, startDay, endDay):
    
    tweets_list1 = []
    tweets_df2 = pd.DataFrame(columns=['URL','Datetime', 'Tweet Id','Content', 'Username'])
    
    # # If the typed account is not valid then, return an empty dataframe
    if pd.isnull(twitterName) or twitterName == "":
        return tweets_df2
        
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+twitterName+' since:'+startDay+' until:'+endDay+'').get_items()):
        tweets_list1.append([tweet.url, tweet.date, tweet.id, tweet.content, tweet.username])
        #print(tweets_list1)
        # Creating a dataframe from the tweets list above 
        tweets_df2 = pd.DataFrame(tweets_list1, columns=['URL','Datetime', 'Tweet Id','Content', 'Username'])
    
    return tweets_df2

# The function to remove RT and Reply
def remove_rt_reply(df, contentCol):
    # The content starting with "@" is considered as a Reply
    # The content starting with "RT @" is considered as a retweet
    
    rs = df.copy(deep=True)
    row = -1
    target = rs[contentCol]
    
    
    rs['retflag'] = False
    for i in target:
        row = row + 1
        
        if(i[0:1] == "@" or i[0:2] == "RT"):
            rs['retflag'][row] = True
        else:
            rs['retflag'][row] = False
        
    rs_L1 = rs[rs['retflag'] == False]
    
    del rs_L1['retflag']
    rs_L1 = rs_L1.reset_index(drop=True)
    
    return rs_L1

def search_keyword(df,keyword,contentCol,isOnlyHashtag,isremove):
    rs = df.copy(deep=True)
    target = rs[contentCol]
    keyword_low = []

    # If we only want to find hashtags, then this part add "#" at the beginning of keywords
    if(isOnlyHashtag == True):
        for k in range(0,len(keyword),1):
            keyword[k] = '#' + keyword[k]
    else:
        keyword = keyword
        
    for k in range(0,len(keyword),1):
        keyword_low.append(keyword[k].lower())
            
    rs['findKeywordFlag'] = False
    rs['findKeyword'] = ''
    
    row = -1
    for i in target: # Contents
        i_low = i.lower()
        row = row + 1
        for k in keyword_low: # Keywords
            
            if(i_low.find(k) >= 0): 
                rs['findKeywordFlag'][row] = True
                key = rs['findKeyword'][row]
                rs['findKeyword'][row] = rs['findKeyword'][row] +  k + '|'
                
    if(isremove == True):
        rs_L1 = rs[rs['findKeywordFlag'] == True]
        rs_L1 = rs_L1.reset_index(drop=True)
    else:
        rs_L1 = rs
        
    return rs_L1


###############
## Main part ##
###############

st_day = "2022-11-11" # start date
ed_day = "2022-12-12" # end date

my_keyword = ['tesla'] # Keywords that we want to search

output_file_name = "./test" # file name and location to save
log_file_path = "./log.txt" # log file name and location

target_tweet_nmae = ['livemint'] # Tpye twitter accounts

append_mode = False 

for sid in target_tweet_nmae:
    
    # Exception
    try:
        if pd.isnull(sid) or sid == "":
            with open(log_file_path, "a") as file:
                file.write("Wrong nickname. Saved time : " + str(datetime.datetime.now()) + "\n")
            file.close()
            continue
            
        result = read_tweet_list(sid,st_day,ed_day)
        print(len(result))
        with open(log_file_path, "a") as file:
            file.write(sid + " has " + str(len(result)) + "tweets found. Saved time : " + str(datetime.datetime.now()) + "\n")
        file.close()
    except:
        with open(log_file_path, "a") as file:
            file.write(sid + " occured error. Skip this account. Saved time : " + str(datetime.datetime.now()) + "\n")
        file.close()
        continue


    # Remove Rt and Retweets
    # If you want to get data with retweets, replace result_L1 with result in search_keyword function and comment result_L1 out. 
    result_L1 = remove_rt_reply(result,'Content') 
    
    # Find tweets having keywords
    # argument : DF / list of keyword / column name / Hashtag / If there is no keyword in tweets, then remove them
    result_L2 = search_keyword(result_L1,my_keyword,'Content',False,True)
    
    sleep(10) # Prevent overload
    
    # If we get data, then convert it to a csv file
    if(len(result_L2) > 0):
                
        if append_mode == False:
            append_mode = True
            result_L2.to_csv(output_file_name + ".csv",index=False,header=True)
            
        elif append_mode == True:
            for i in range(len(result_L2)):
                result_L2.loc[[i]].to_csv(output_file_name,index=False,header=False,mode='a')


#########################
## Load the local data ##
#########################

with open('test.csv', encoding='UTF-8') as f:
    retrieved_list = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
print(retrieved_list)