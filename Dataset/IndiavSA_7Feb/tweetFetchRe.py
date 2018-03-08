import tweepy
import csv

def limit_handled(cursor):
	while True:
		try:
			yield cursor.next()
		except tweepy.RateLimitError:
			time.sleep(15 * 60)


access_token = "776985857819422720-fRvqysQzvHB2R9IepsTh8eNh1fu5f5Z"
access_token_secret = "NiEZXjD8iPpshNpI6i4uGq5c9jlmHpGNFaXxcFl6EqzwK"
consumer_key = "cMllJepz8tXNW4jxThdgr6c2g"
consumer_secret = "pRlGEUrp7VjBiHOSYwDcD7Y8dTxzys0BcB5fcfMhdXXlyVJLyX"

print('in module')
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    csvFile = open('TW_INDSA_7feb_part2e.csv', 'a')
    csvWriter = csv.writer(csvFile)

    for tweet in limit_handled(tweepy.Cursor(api.search,q="#INDvSA OR #SAvIND OR #ODI", since="2018-02-07",until="2018-02-08",lang="en").items()):
		csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
		print "Print ho ja baba"
except tweepy.error.TweepError:
    print "mar gaya baba"
    raise