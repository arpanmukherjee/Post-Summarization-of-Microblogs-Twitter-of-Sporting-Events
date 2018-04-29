import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from sklearn.metrics import mean_squared_error
from sklearn.feature_extraction.text import TfidfVectorizer

data_dict = {}
tweets = []
csv_path = "/home/iiitd/Desktop/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/threshold_data.csv"



def pca_plot_data(dataX, dataY):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #PCA
    pca = PCA(n_components=3)
    dataX_r = pca.fit(dataX).transform(dataX)
    colours = []
    for i in range(len(dataY)):
        colours.append(dataY[i])

    plt.title('Data distribution for different clusters in 3D')
    temp_x = []
    temp_y = []
    temp_z = []
    for i in range(len(dataX_r)):
        temp_x.append(dataX_r[i][0])
        temp_y.append(dataX_r[i][1])
        temp_z.append(dataX_r[i][2])
    ax.scatter(temp_x, temp_y, temp_z, c=dataY, s=40)
    plt.show()
    # plt.scatter(temp_x, temp_y, c=colours, cmap=plt.cm.get_cmap("jet", 10))
    # plt.colorbar(ticks=range(10), label='Clusters')
    # plt.clim(-0.5, 9.5)
    # plt.show()


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
min_dist_centroid = [1e9]*k_value
closest_ind = [0]*k_value
model = KMeans(n_clusters=k_value, init='k-means++', max_iter=500)
model.fit(X)

order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
data_x = X.toarray()
data_y = model.labels_
for i in range(len(data_x)):
    id = data_y[i]
    temp_dist = mean_squared_error(data_x[i], model.cluster_centers_[id])
    if min_dist_centroid[id] > temp_dist:
        min_dist_centroid[id] = temp_dist
        closest_ind[id] = i
for i in range(k_value):
    print tweets[i]
    # print(str(min_dist_centroid[i])+" "+str(closest_ind[i]))

# data = []
# with open(csv_path, "rb") as file_obj:
#     reader = csv.reader(file_obj)
#     for row in reader:
#         data.append(row[1])
# with open('/home/iiitd/Desktop/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/clustered_data.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     for j in range(len(Y)):
#         writer.writerow([Y[j], data[j]])
# pca_plot_data(X.toarray(), model.labels_)
