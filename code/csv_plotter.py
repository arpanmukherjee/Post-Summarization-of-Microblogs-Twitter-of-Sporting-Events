import csv
import matplotlib.pyplot as plt;plt.rcdefaults()
import numpy as np

csv_path = "/Users/arpn/Google Drive/Semester2/Information Retrieval/Post-Summarization-of-Microblogs-" \
           "Twitter-of-Sporting-Events/Dataset/Dataset collected/TW_RMPSGUCL_15feb.csv"
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
            data_dict[key] = set()
        data_dict[key].add(row[1])


def build_data_graph():
    temp = []
    for i in range(len(data_dict.keys())):
        temp.append(data_dict.keys()[i])
    objects = tuple(temp)
    y_pos = np.arange(len(objects))
    performance = []
    for i in temp:
        performance.append(len(data_dict[i]))

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('No of tweetes')
    plt.title('Comparison of no of tweets with time')

    plt.show()


with open(csv_path, "rb") as file_obj:
    try:
        csv_reader(file_obj)
    except:
        print("Ignore")

build_data_graph()