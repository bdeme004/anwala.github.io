import recommendations as recs
import BJDfunctions as fn
PROXY = 477  #712

PEOPLE = [471, 280, 373, 642, 330, 450, 541, 577, 864, 43, 805, 313, 504, 254, 94, 399,
          5, 92, 381, 716, 49, 1, 843, 222]


def topAndBottom(dataset):
    for item in fn.topValues(dataset):
        fn.printFail(item)
    print("\n")
    for item in fn.bottomValues(dataset):
        fn.printFail(item)
    print("\n")


ratings = fn.load_data()

item_mode = recs.transformPrefs(ratings)

fn.printFail(recs.sim_pearson(item_mode, 'Aristocats, The (1970)', '101 Dalmatians (1996)'))
fn.printFail(recs.sim_pearson(item_mode, 'Aristocats, The (1970)', 'Wild Bill (1995)'))
fn.printFail(recs.sim_pearson(item_mode, '101 Dalmatians (1996)', 'Wild Bill (1995)'))

cats = item_mode['Aristocats, The (1970)']
street = item_mode['Wild Bill (1995)']
dogs = item_mode['101 Dalmatians (1996)']

cats_dogs = list()
cats_street = list()
corr = 0

print("\n")
for item in cats:
    if item in dogs:
        cats_dogs.append((item, cats[item], dogs[item]))
    if item in street:
        cats_street.append((item, cats[item], street[item]))


for item in cats_dogs:
    print(item)
print("\n")
for item in cats_street:
    print(item)


print("\n")
print(corr)
print(len(cats))
print(len(cats_dogs))
print(len(dogs))
print(len(cats_street))
print(len(street))
