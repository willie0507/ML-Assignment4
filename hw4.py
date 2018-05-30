import sys
# import pandas as pd
if (sys.argv[1] == '--train'):
    bias = 3
    fp = open(r'upload_full2/training_data/Training freq 1D, OW 16, PW 2.csv', 'r')
elif (sys.argv[1] == '--test'):
    bias = 4
    fp = open(r'upload_full2/test_feature/Verification freq 1D, OW 16, PW 2_feature.csv', 'r')
for i in range(4):
    line = fp.readline()

data = []
label= []
while line:
    tmp = []
    for i in range(1, 85):
        idx = line.find(',')
        if(i < bias):
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

if(bias == 3):
    output = 'train_1D_OW16_PW2.txt'
else:
    output = 'test_1D_OW16_PW2.txt'  
with open(output, 'w') as fp:
    pass
with open(output, 'a') as fp:
    for i, v in enumerate(data):
        if(label[i] == 'True'):
            fp.write(str(1) + ' ')
        elif(label[i] == 'False'):
            fp.write(str(0) + ' ')
        elif(bias == 4):
            fp.write(str(9) + ' ')
        else:
            continue
        for j in v:
            fp.write(j + ' ')
        fp.write('\n')
