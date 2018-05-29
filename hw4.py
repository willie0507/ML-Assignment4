import pandas as pd

fp = open(r'full1_upload/full1_upload/training_data/Training freq 1D, OW 1, PW 1.csv', 'r')
line = fp.readline()
line = fp.readline()
line = fp.readline()
line = fp.readline()
data = []
label= []
while line:
    tmp = []
    for i in range(1, 85):
        idx = line.find(',')
        if(i < 3):
            line = line[idx+1:]
            continue
        if(i == 84):
            label.append(line[idx+1:-1])
            break
        value = line[:idx]
        if(value == ''):
            line = line[idx+1:]
            continue
        tmp.append(str(i - 2) + ':' + value)
        line = line[idx+1:]
    line = fp.readline()
    data.append(tmp)
    del tmp
fp.close()

with open('train.txt', 'a') as fp:
    for i, v in enumerate(data):
        if(label[i] == 'True'):
            fp.write(str(1) + ' ')
        elif(label[i] == 'False'):
            fp.write(str(0) + ' ')
        else:
            continue
        for j in v:
            fp.write(j + ' ')
        fp.write('\n')
