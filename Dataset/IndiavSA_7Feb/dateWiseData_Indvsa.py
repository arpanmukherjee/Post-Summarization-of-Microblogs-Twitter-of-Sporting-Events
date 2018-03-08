import tweepy
import csv

access_token = "776985857819422720-fRvqysQzvHB2R9IepsTh8eNh1fu5f5Z"
access_token_secret = "NiEZXjD8iPpshNpI6i4uGq5c9jlmHpGNFaXxcFl6EqzwK"
consumer_key = "cMllJepz8tXNW4jxThdgr6c2g"
consumer_key_secret = "pRlGEUrp7VjBiHOSYwDcD7Y8dTxzys0BcB5fcfMhdXXlyVJLyX"

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('Mytweets2_SAvIND.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="#SAvIND",\
                           since="2018-02-06",until="2018-02-07").items():
    #print tweet.created_at, tweet.text
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])





# import tweepy
# import csv

# consumer_key = '####'
# consumer_secret = '####'
# access_token = '####'
# access_token_secret = '####'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# # Open/Create a file to append data
# csvFile = open('tweets.csv', 'a')
# #Use csv Writer
# csvWriter = csv.writer(csvFile)


# for tweet in tweepy.Cursor(api.search,q="#ps4",count=100,\
#                            lang="en",\
#                            since_id=2014-06-12).items():
#     print tweet.created_at, tweet.text
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])