mylist = list()

with open("result_urls_limited.txt") as infile:
    for line in infile:
        mylist.append(line)

myList = list(dict.fromkeys(mylist))

with open("new1.txt", 'w') as of:
    for item in myList:
        of.write(item + "\n")
