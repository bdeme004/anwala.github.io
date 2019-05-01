import numpredict as npre

kset = [1, 2, 5, 10, 20]
matrix = list()
with open("titles.txt") as inf:
    blogs = [line.rstrip("\n") for line in inf]

with open("blogdata.txt") as inf:
    for line in inf:
        temp = line.rstrip("\n").split()
        matrix.append([int(val) for val in temp])

fmeasure = matrix[len(matrix) - 2]
wsdl = matrix[len(matrix) - 1]

print("Nearest Neighbors to F-Measure:")
for k in kset:
    print("k=%d" % k)
    for val, i in npre.knnestimate(matrix, fmeasure, k):
        print(blogs[i], " -  dist= %.3f" % val)
    print("\n")

print("Nearest Neighbors to WS-DL:")
for k in kset:
    print("k=%d" % k)
    for val, i in npre.knnestimate(matrix, wsdl, k):
        print(blogs[i], " -  dist= %.3f" % val)
    print("\n")
