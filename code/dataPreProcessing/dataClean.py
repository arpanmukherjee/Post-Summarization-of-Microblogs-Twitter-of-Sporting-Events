####################################################################
# IR PROJECT --- POST SUMMARIZATION FOR SPORTING EVENTS FROM MICROBLOGS - TWITTER
#--------------------------------------------------------------------
#dataClean - Data preprocessing
#---------------------------------------------------------------------
#CREATED BY : Shubhi
#DATE : Mar 9,2018
#---------------------------------------------------------------------

import csv
import nltk
import string

#stopWords
stopWords = nltk.corpus.stopwords.words('english') + list(string.punctuation)

#porterStemmer
portStem = nltk.stem.PorterStemmer();

tweet = ""
dat = []
duplicate =0
input = '/media/adalove/WorkDrive/M.Tech/Sem2/IR/project/project_IR/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/originalData/TW_INDSA_13feb.csv'
output = '/media/adalove/WorkDrive/M.Tech/Sem2/IR/project/project_IR/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/TW_INDSA_13feb_Cleaned2.csv'
outputMap = '/media/adalove/WorkDrive/M.Tech/Sem2/IR/project/project_IR/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/TW_INDSA_13feb_Mapper.csv'



mapper = {} #map original tweets to tokenized tweets

#read file
with open(input,'r') as f:
    reader = csv.reader(f)

    for row in reader:

        list = []
        if len(row) != 2:
            continue

        # remove seconds
        #t =str(row[0])[0:16]
        t= row[0]

        tweet = row[1]
        # remove url
        urlIndex = row[1].find("https")
        if urlIndex!=-1:
            nextSpace = row[1].find(" ",urlIndex)
            if nextSpace ==-1:
                #end of string
                tweet = row[1][:urlIndex]
            else:
                tweet = row[1][:urlIndex] + row[1][nextSpace+1:len(row[1])]
        #print tweet

        #remove retweets
        if tweet.find("RT @")==0:
           continue

        #remove duplicate tweets
        #accumulated due to twitter API network error
        for pair in dat:
            #print "here"
            if t == pair[0] and tweet == pair[1]:
                print t
                print tweet
                duplicate =1
                break

        if duplicate==1:
            duplicate=0
            continue

        #tokenization and stemming...
        ft = [i for i in nltk.word_tokenize(tweet.lower().decode('utf-8').strip()) if i not in stopWords]
        final_tweet = []
        for word in ft:
            final_tweet.append(portStem.stem(word))


        list.append(t)
        list.append(final_tweet)
        dat.append(list)
        mapper[row[1]] = final_tweet


#writing to csv
with open(output,'w+') as f1:
    writer = csv.writer(f1)
    writer.writerows(dat)


#writing mapper to csv
with open(outputMap,'w+') as f1:
    writer = csv.writer(f1)
    writer.writerows(mapper)




