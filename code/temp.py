from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score

def pca_plot_data(dataX, dataY):
    #PCA
    pca = PCA(n_components=2)
    dataX_r = pca.fit(dataX).transform(dataX)
    colours = []
    for i in range(len(dataY)):
        colours.append(dataY[i])

    plt.title('Data distribution for different genre')
    temp_x = []
    temp_y = []
    for i in range(len(dataX_r)):
        temp_x.append(dataX_r[i][0])
        temp_y.append(dataX_r[i][1])
    plt.scatter(temp_x, temp_y, c=colours, cmap=plt.cm.get_cmap("jet", 10))
    plt.colorbar(ticks=range(10), label='Genres')
    plt.clim(-0.5, 9.5)
    plt.show()

documents = ["This little kitty came to play when I was eating at a restaurant.",
             "Merley has the best squooshy kitten belly.",
             "Google Translate app is incredible.",
             "If you open 100 tab in google you get a smiley face.",
             "Best cat photo I've ever taken.",
             "Climbing ninja cat.",
             "Impressed with google map feedback.",
             "Key promoter extension for Google Chrome."]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

print("\n")
print("Prediction")

Y = vectorizer.transform(["chrome browser to open."])
prediction = model.predict(Y)
print(prediction)

Y = vectorizer.transform(["My cat is hungry."])
prediction = model.predict(Y)
print(prediction)
pca_plot_data(X.toarray(), model.labels_)