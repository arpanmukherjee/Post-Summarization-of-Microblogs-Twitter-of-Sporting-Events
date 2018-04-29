import csv
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score
from sklearn.feature_extraction.text import TfidfVectorizer

data_dict = {}
tweets = []
csv_path = "/home/iiitd/Desktop/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/threshold_data.csv"


def get_tweet(row):
    tweet = ""
    for item in row:
        tweet += item
    return tweet
     

def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        key = row[0]
        if key not in data_dict.keys():
            data_dict[key] = []
        data_dict[key].append(get_tweet(row[1]))
        tweets.append(get_tweet(row[1]))


with open(csv_path, "rb") as file_obj:
    try:
        csv_reader(file_obj)
    except:
        print("Ignore")

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(tweets)
k_value = len(data_dict.keys())
model = KMeans(n_clusters=k_value, init='k-means++', max_iter=500)
model.fit(X)

order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()

Y = model.labels_
unique, counts = np.unique(Y, return_counts=True)
for i, j in zip(unique, counts):
    print(str(i)+" "+str(j))

data = []
with open(csv_path, "rb") as file_obj:
    reader = csv.reader(file_obj)
    for row in reader:
        data.append(row[1])
with open('/home/iiitd/Desktop/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/clustered_data.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for j in range(len(Y)):
        writer.writerow([Y[j], data[j]])
