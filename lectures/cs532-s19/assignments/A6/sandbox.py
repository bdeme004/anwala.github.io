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

