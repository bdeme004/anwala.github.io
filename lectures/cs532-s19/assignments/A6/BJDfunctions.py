def load_data(path='ml-100k'):
    movie_titles = list()
    ratings = dict()

    with open(path + '/u.item', errors='replace') as inf:
        for line in inf:
            movie_titles.append(line.split("|")[1])

    with open(path + '/u.data', errors='replace') as inf:
        for line in inf:
            data = line.split("\t")
            user = int(data[0])
#            try:
            index = int(data[1]) - 1
            movie = movie_titles[index]
#            except Exception as e:
#                print(e)
#                for item in data:
#                    print(item)
            ratings.setdefault(user, dict())
            ratings[user][movie] = int(data[2])
#            try:
#                ratings[user][movie] = int(data[2])
#            except KeyError:
#                ratings[user] = dict()
#                ratings[user][movie] = int(data[2])
    return ratings


def loadDataIMBD(prefs, path='imbd'):
    ratings = dict()
    infile = path + '/title.basics.tsv/data.tsv'
    with open(infile, errors='replace') as inf:
        for line in inf:
            data = line.split("\t")
            try:
                tConst = data[0]
                title = data[2]
                year = int(data[5])
            except Exception:
                tConst = 0
                title = 0
                year = 2000
            if (year < 1999 and data[1] == 'movie' and data[4] == '0'):
                ratings[tConst] = (title, year)
    print("data loaded", flush=True)
    return ratings


def topValues(any_list):
    values = list()
    for i in range(5):
        values.append(any_list[i])

    return values


def bottomValues(any_list):
    values = list()
    end = len(any_list)
    for i in range(end - 5, end):
        values.append(any_list[i])
    return values


def printFail(string):
    try:
        print(string)
    except UnicodeEncodeError:
        print(str(string).encode(encoding="ascii", errors='replace')
                         .decode(encoding="ascii", errors='replace'))
