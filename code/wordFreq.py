from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import csv
import math


csv_path = "/media/adalove/WorkDrive/M.Tech/Sem2/IR/project/project_IR/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/TW_INDSA_13feb_Cleaned2.csv"
#word_list = ['A', 'A', 'B', 'B', 'A', 'C', 'C', 'C', 'C']

n =100
word_list = []
#read file
with open(csv_path,'r') as f:
    reader = csv.reader(f)

    for row in reader:
        #print row[1]
        tw = row[1][1:]
        tw = tw[:-1]
        curTweet = tw.split(",")
        for w in curTweet:
            word_list.append(w)



print "words done"


#counts = Counter(word_list)
counts = dict(Counter(word_list).most_common(n))
print len(word_list)
print counts
for k,v in counts.iteritems():
    counts[k] = math.log10(v)

print "counter done"
labels, values = zip(*counts.items())

# sort your values in descending order
indSort = np.argsort(values)[::-1]
print "sorted"

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

bar_width = 0.35

print "plotting"
plt.bar(indexes, values)

# add labels
plt.xticks(indexes + bar_width, labels)
plt.ylabel("log10(Word Freqency)")
plt.xlabel("Top 100 words")
plt.show()