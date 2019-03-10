import numpy as np

list0 = np.linspace(0, 100)
list1 = list()
for item in np.linspace(1, 100, 11):
    list1.append("F" + str(int(item)))
print(list1)
