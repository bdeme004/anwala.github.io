spam = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9"]
notspam = ["n0", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9"]

results = []

for item in spam:
    with open("Testing/" + item + ".txt") as inf:
        results.append(((inf.read()), "spam"))

for item in notspam:
    with open("Testing/" + item + ".txt") as inf:
        results.append(((inf.read()), "not spam"))

with open("Testing.txt", 'w') as of:
    for item in results:
        of.write(str(item) + "\n")

results.clear()

for item in spam:
    with open("Training/" + item + ".txt") as inf:
        results.append(((inf.read()), "spam"))

for item in notspam:
    with open("Training/" + item + ".txt") as inf:
        results.append(((inf.read()), "not spam"))

with open("Training.txt", 'w') as of:
    for item in results:
        of.write(str(item) + "\n")
