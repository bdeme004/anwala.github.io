mylist = list()

with open("words.txt") as inf:
    for line in inf:
        mylist.append(line)
    
mylist = list(dict.fromkeys(mylist))

with open("result_urls_limited.txt", 'w') as of:
    for item in mylist:
        of.write(item)
