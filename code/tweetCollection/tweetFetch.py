from retrying import retry
import tweepy
import csv



@retry(wait_exponential_multiplier=10000,wait_exponential_max=10000)
def extract_tweet():
    
    # put these values
    access_token = ""
    access_token_secret = ""
    consumer_key = ""
    consumer_secret = ""

    print('in module')
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        print " authorized"
        csvFile = open('TW_RMPSGUCL_15feb.csv', 'a')
        csvWriter = csv.writer(csvFile)

        #for tweet in tweepy.Cursor(api.search,q="#INDvSA OR #SAvIND OR #ODI", since="2018-02-13").items():    
        for tweet in tweepy.Cursor(api.search,q="#RMvsPSG OR #PSGvsRM OR #UCL", since="2018-02-14").items():    
          #print "in for"
          csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
          print "Print ho ja baba"
          #csvFile.close()
    except tweepy.error.TweepError:
        print "mar gaya baba"
        raise


extract_tweet()


