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

fn.printFail(recs.sim_pearson(item_mode, 'Star Wars (1977)', 'Grease (1978)'))
fn.printFail(recs.sim_pearson(item_mode, 'Star Wars (1977)', 'While You Were Sleeping (1995)'))
fn.printFail(recs.sim_pearson(item_mode, 'Star Wars (1977)', 'Sleepless in Seattle (1993)'))

cats = item_mode['Wallace & Gromit: The Best of Aardman Animation (1996)']
gun = item_mode['Grease (1978)']
dogs = item_mode['While You Were Sleeping (1995)']

cats_dogs = list()
cats_gun = list()
corr = 0

print("\n")
for item in dogs:
    if item in cats:
        cats_dogs.append((item, cats[item], dogs[item]))
    if item in gun:
        cats_gun.append((item, dogs[item], gun[item]))


for item in cats_dogs:
    print(item)
print("\n")
for item in cats_gun:
    print(item)


print("\n")
print(corr)
print("len cats:")
print(len(cats))
print("len dogs:")
print(len(dogs))
print("len gun:")
print(len(gun))
print("len dogs/cats:")
print(len(cats_dogs))
print("len dogs/gun:")
print(len(cats_gun))
