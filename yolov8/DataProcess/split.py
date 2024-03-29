import os
import random

trainval_percent = 0.9
train_percent = 0.9
xmlfilepath = 'data2/Annotations'
txtsavepath = 'data2/ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('data2/ImageSets/trainval.txt', 'w')
ftest = open('data2/ImageSets/test.txt', 'w')
ftrain = open('data2/ImageSets/train.txt', 'w')
fval = open('data2/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

