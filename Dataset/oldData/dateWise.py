import tweepy
import csv

access_token = "2822909874-ZJ1vra8PUwN9WeO7gjh52S1jjkPCXLCXdESHZRa"
access_token_secret = "Aio1oFCNXg5d19Eh24KJLaoiCUM9BGdOKc8pWzaFfatFa"
consumer_key = "Lm90f1Did8j2jFV0wIz4zokX8"
consumer_key_secret = "p3aLTqwfWCaD0onbtZcqcqZzufIg4ZRrTDe9QeXaAXobSQmGXz"

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('tweets_AUSvIND_part2.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="#AUSvIND",\
                           since="2018-02-02",until="2018-02-05").items():
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