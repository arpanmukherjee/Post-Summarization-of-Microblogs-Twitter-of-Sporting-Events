####################################################################
# IR PROJECT --- POST SUMMARIZATION FOR SPORTING EVENTS FROM MICROBLOGS - TWITTER
#--------------------------------------------------------------------
#tweet Vectors - Create vectors out of tweets
#---------------------------------------------------------------------
#CREATED BY : Shubhi
#DATE : Mar 9,2018
#---------------------------------------------------------------------
import csv
from collections import Counter

csv_path = "/media/adalove/WorkDrive/M.Tech/Sem2/IR/project/project_IR/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/TW_INDSA_13feb_Cleaned_subsampled.csv"

vocab = set()
tweets = {}
id=1

tweet_to_id = {}
with open(csv_path,'r') as f:
    reader = csv.reader(f)

    for row in reader:
        #print row[1]
        tw = row[1][1:]
        tw = tw[:-1]
        curTweet = tw.split(",")

        for w in curTweet:
            vocab.add(w)
        freq = Counter(curTweet)
        tweets[id] = freq
        id+=1
        tweet_to_id[row[1]] = id

vocab = sorted(vocab)

tweetVectors = {}
#create vector for each tweet

for k,v in tweets.iteritems():
    vec = [0]*len(vocab)
    i=0
    for word in vocab:
        if word in v.keys():
            vec[i] = v[word]
        i=i+1

    tweetVectors[k] = vec


print tweet_to_id
print  tweetVectors