# https: /  / github.com / arthur - e / Programming - Collective - Intelligence / blob / master / chapter8 / numpredict.py

from random import random, randint
import math
from pylab import *


def wineprice(rating, age):
    peak_age = rating - 50

    # Calculate price based on rating
    price = rating / 2
    if age > peak_age:
        # Past its peak, goes bad in 10 years
        price = price * (5 - (age - peak_age) / 2)
    else:
        # Increases to 5x original value as it
        # approaches its peak
        price = price * (5 * ((age + 1) / peak_age))
    if price < 0:
        price = 0
    return price


def wineset1():
    rows = []
    for i in range(300):
      # Create a random age and rating
      rating = random() * 50 + 50
      age = random() * 50

      # Get reference price
      price = wineprice(rating, age)

      # Add some noise
      price *= (random() * 0.2 + 0.9)

      # Add to the dataset
      rows.append({'input': (rating, age),
                   'result': price})
    return rows


def euclidean(v1, v2):
    d = 0.0
    for i in range(len(v1)):
      d += (v1[i] - v2[i]) ** 2
    return math.sqrt(d)


def cosine(v1, v2):
    d = 0.0
    num = (vdot(v1, v2))
    den = ((sqrt(vdot(v1, v1))) * (sqrt(vdot(v2, v2))))
    if den == 0:
        # cue that something has gone very wrong
        # for some reason, some of the blogs have 0 of the terms checked?
        # Which makes me question that data, but it's a little late for that
        #  ¯\_(ツ)_/¯
        return 803

    d = num / den
    return d


def getdistances(data, vec1, distance=euclidean):
    distancelist = []

    # Loop over every item in the dataset
    for i in range(len(data)):
      vec2 = data[i]#['input']

      # Add the distance and the index
      if vec2 != vec1:
        distancelist.append((distance(vec1, vec2), i))

    # Sort by distance
    distancelist.sort()
    return distancelist


def knnestimate(data, vec1, k=5):
    # Get sorted distances
    dlist = getdistances(data, vec1, cosine)
   # avg = 0.0

    # Take the average of the top k results
#    for i in range(k):
#      idx = dlist[i][1]
#      avg += data[idx]['result']
#    avg = avg / k
    return dlist[0:k] #avg


def inverseweight(dist, num=1.0, const=0.1):
    return num / (dist + const)


def subtractweight(dist, const=1.0):
    if dist > const:
      return 0
    else:
      return const - dist


def gaussian(dist, sigma=5.0):
    return math.e ** (-dist ** 2 / (2 * sigma ** 2))


def weightedknn(data, vec1, k=5, weightf=gaussian):
    # Get distances
    dlist = getdistances(data, vec1)
    avg = 0.0
    totalweight = 0.0

    # Get weighted average
    for i in range(k):
      dist = dlist[i][0]
      idx = dlist[i][1]
      weight = weightf(dist)
      avg += weight * data[idx]['result']
      totalweight += weight
    if totalweight == 0:
       return 0
    avg = avg / totalweight
    return avg


def dividedata(data, test=0.05):
    trainset = []
    testset = []
    for row in data:
      if random() < test:
        testset.append(row)
      else:
        trainset.append(row)
    return trainset, testset


def testalgorithm(algf, trainset, testset):
    error = 0.0
    for row in testset:
      guess = algf(trainset, row['input'])
      error += (row['result'] - guess) ** 2
      #print row['result'], guess
    #print error / len(testset)
    return error / len(testset)


def crossvalidate(algf, data, trials=100, test=0.1):
    error = 0.0
    for i in range(trials):
      trainset, testset = dividedata(data, test)
      error += testalgorithm(algf, trainset, testset)
    return error / trials


def wineset2():
    rows = []
    for i in range(300):
      rating = random() * 50 + 50
      age = random() * 50
      aisle = float(randint(1, 20))
      bottlesize = [375.0, 750.0, 1500.0][randint(0, 2)]
      price = wineprice(rating, age)
      price *= (bottlesize / 750)
      price *= (random() * 0.2 + 0.9)
      rows.append({'input': (rating, age, aisle, bottlesize),
                   'result': price})
    return rows


def rescale(data, scale):
    scaleddata = []
    for row in data:
      scaled = [scale[i] * row['input'][i] for i in range(len(scale))]
      scaleddata.append({'input': scaled, 'result': row['result']})
    return scaleddata


def createcostfunction(algf, data):
    def costf(scale):
      sdata = rescale(data, scale)
      return crossvalidate(algf, sdata, trials=20)
    return costf


# weightdomain = [(0, 10)] * 4


def wineset3():
    rows = wineset1()
    for row in rows:
      if random() < 0.5:
        # Wine was bought at a discount store
        row['result'] *= 0.6
    return rows


def probguess(data, vec1, low, high, k=5, weightf=gaussian):
    dlist = getdistances(data, vec1)
    nweight = 0.0
    tweight = 0.0

    for i in range(k):
      dist = dlist[i][0]
      idx = dlist[i][1]
      weight = weightf(dist)
      v = data[idx]['result']

      # Is this point in the range?
      if v >= low and v <= high:
        nweight += weight
      tweight += weight
    if tweight == 0:
       return 0

    # The probability is the weights in the range
    # divided by all the weights
    return nweight / tweight


def cumulativegraph(data, vec1, high, k=5, weightf=gaussian):
    t1 = arange(0.0, high, 0.1)
    cprob = array([probguess(data, vec1, 0, v, k, weightf) for v in t1])
    plot(t1, cprob)
    show()


def probabilitygraph(data, vec1, high, k=5, weightf=gaussian, ss=5.0):
    # Make a range for the prices
    t1 = arange(0.0, high, 0.1)

    # Get the probabilities for the entire range
    probs = [probguess(data, vec1, v, v + 0.1, k, weightf) for v in t1]

    # Smooth them by adding the gaussian of the nearby probabilites
    smoothed = []
    for i in range(len(probs)):
      sv = 0.0
      for j in range(0, len(probs)):
        dist = abs(i - j) * 0.1
        weight = gaussian(dist, sigma=ss)
        sv += weight * probs[j]
      smoothed.append(sv)
    smoothed = array(smoothed)

    plot(t1, smoothed)
    show()