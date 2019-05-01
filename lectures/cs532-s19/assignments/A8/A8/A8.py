import docclass as dcl
from subprocess import check_output

cl = dcl.naivebayes(dcl.getwords)

check_output(['rm', 'test.db'])

cl.setdb('test.db')
training = []
testing = []

with open("Training.txt") as inf:
    for line in inf:
        temp = line.rstrip("\n").split(' == ')
        training.append(tuple(temp))

with open("Testing.txt") as inf:
    for line in inf:
        testing.append(tuple(line.rstrip("\n")))

for item in training:
    cl.train(item[0], item[1])
    print(item[1])

for item in testing:
    #    print(item[0], item[1])
    print(cl.classify(item[0], item[1]))
