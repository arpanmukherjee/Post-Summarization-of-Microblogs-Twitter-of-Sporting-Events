####################################################################
# IR PROJECT --- POST SUMMARIZATION FOR SPORTING EVENTS FROM MICROBLOGS - TWITTER
#--------------------------------------------------------------------
#dataClean - Data preprocessing
#---------------------------------------------------------------------
#CREATED BY : Shubhi
#DATE : Mar 9,2018
#---------------------------------------------------------------------

import csv


dat = []
#read file
with open('/media/adalove/WorkDrive/M.Tech/Sem2/IR/project/project_IR/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/Dataset collected/TW_RMPSGUCL_15feb.csv','r') as f:
    reader = csv.reader(f)

    for row in reader:
        #remove seconds
        list = []
        if len(row) != 2:
            continue
        t =str(row[0])[0:16]
        #print t
        list.append(t)
        list.append(row[1])
        dat.append(list)

#writing to csv
with open('/media/adalove/WorkDrive/M.Tech/Sem2/IR/project/project_IR/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/Dataset collected/TW_RMPSGUCL_15feb_SecRemoved.csv','w+') as f1:
    writer = csv.writer(f1)
    writer.writerows(dat)





