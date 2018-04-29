import csv
import matplotlib.pyplot as plt;plt.rcdefaults()
import numpy as np

csv_path = "/home/iiitd/Desktop/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/TW_INDSA_13feb_Cleaned2.csv"

data_dict = {}


def remove_sec(temp):
    ans = ""
    for i in temp:
        ans += i


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        key = row[0][:-3]
        if key not in data_dict.keys():
            data_dict[key] = []
        data_dict[key].append(row[1])


def build_data_graph():
    temp = []
    for i in range(len(data_dict.keys())):
        temp.append(data_dict.keys()[i])
    objects = tuple(temp)
    y_pos = np.arange(len(objects))
    performance = []
    for i in temp:
        performance.append(len(data_dict[i]))
    mean = np.mean(performance)
    std_dev = np.std(performance)
    threshold = mean+2*std_dev
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('No of tweetes')
    plt.title('Comparison of no of tweets with time')

    plt.show()
    return performance, threshold



with open(csv_path, "rb") as file_obj:
    try:
        csv_reader(file_obj)
    except:
        print("Ignore")

performance, threshold = build_data_graph()
imp_moments = 0
for i in range(len(performance)):
    if performance[i] >= threshold:
        imp_moments += 1
print("Important Moments: " + str(imp_moments))
# print("Maximum tweets in a minute: "+str(max([len(data_dict[i]) for i in data_dict.keys()])))

threshold_tweets = {}
for key in sorted(data_dict.keys()):
    if len(data_dict[key]) > threshold:
        threshold_tweets[key] = data_dict[key]
with open('/home/iiitd/Desktop/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/threshold_data.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key in threshold_tweets.keys():
        for j in range(len(threshold_tweets[key])):
            writer.writerow([key, threshold_tweets[key][j]])
build_data_graph()
