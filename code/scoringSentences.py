from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import csv

stopWords = set(stopwords.words("english"))
words = word_tokenize(text)


with open(input,'r') as f:
    reader = csv.reader(f)

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()


for sentence in sentences:
    for wordValue in freqTable:
        if wordValue[0] in sentence.lower():
            if sentence[:12] in sentenceValue:
                sentenceValue[sentence[:12]] += wordValue[1]
            else:
                sentenceValue[sentence[:12]] = wordValue[1]

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues/ len(sentenceValue))

summary = ''
for sentence in sentences:
        if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (1.5 * average):
            summary +=  " " + sentence