import csv
import nltk

input = '/media/adalove/WorkDrive/M.Tech/Sem2/IR/project/project_IR/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/threshold_data.csv'

dict = []
tweets = []
#read file
with open(input,'r') as f:
    reader = csv.reader(f)

    for row in reader:

        #print "reading"

        rt = row[1][1:]
        rt = rt[:-1]
        rt = rt.split(',')
        tweets.append(row[1])
        for k in rt:
            dict.append(k)


freq = nltk.FreqDist(dict)

for k,v in freq.iteritems():
    print k
    print v


#score each sentence ...
score = {}
i=0
for t in tweets:
    sc = 0
    for k in t:
        sc += freq[k]
    score[i] =sc
    i+=1

sen = sorted(score, key=score.get)

#remove ""


for k in range(20):
    print tweets[k]
    # temp = tweets[k]
    # temp2= []
    # for t in temp:
    #     x = t[1:]
    #     x = x[:-1]
    #     #print x
    #     temp2.append(x)
    # print temp2

#
# print type(freq)
# print freq
# for word, frequency in freq.most_common(50):
#     print(u'{};{}'.format(word, frequency))

