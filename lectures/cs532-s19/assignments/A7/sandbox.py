words = []
with open("stopwords.txt") as inf:
    for line in inf:
        words.append(line.rstrip("\n"))

with open("stopwords.txt", 'w') as of:
    for word in words:
        of.write(word + "\n")
