import recommendations as recs
import BJDfunctions as fn

PROXY = 477


def topAndBottom(dataset):
    for item in fn.topValues(dataset):
        fn.printFail(item)
    print("\n")
    for item in fn.bottomValues(dataset):
        fn.printFail(item)
    print("\n")


ratings = fn.load_data()


users = recs.topMatches(ratings, PROXY)
item_recs = recs.getRecommendations(ratings, PROXY)
item_mode = recs.calculateSimilarItems(ratings)
grape = item_mode["What's Eating Gilbert Grape (1993)"]
cats = item_mode['Aristocats, The (1970)']

print("\n Similar Users:")
topAndBottom(users)
print("\n Recommended Items:")
topAndBottom(item_recs)
print("\n Like 'What's Eating Gilbert Grape (1993)'")
topAndBottom(grape)
print("\n Like 'Aristocats, The (1970)':")
topAndBottom(cats)
