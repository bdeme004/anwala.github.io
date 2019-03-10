import tweepy
import argparse
import time

# consumer key, consumer secret, access token, access secret.
ckey = "g9QwxyzRoMI2YVNgWIi0lTzlV"
csecret = "tRrBSizC15gLS0Kyco6E5Hl1B6a1jDrPSjcXVGbvq6hV3uaLqd"
atoken = "2592291038-HIOrJ8CY48iy0qeaOvSvKEZRllL03A31vSMNcc9"
asecret = "BpQkp51FF0z9MPWyK44OyYKmFEXR7ScLp1oxsmOawK6LM"

parser = argparse.ArgumentParser(description='''insert description here''')
parser.add_argument('follows', metavar='F', nargs='?',
                    help='.txt list of followers')
parser.add_argument('friends', metavar='N', nargs='?',
                    help='.txt list of friends')
parser.add_argument('-s', '--silent', action='store_true', help='suppress status reports')
args = parser.parse_args()

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

follows_file = args.follows
friends_file = args.friends
TARGET_NAME = 'acnwala'

# need better naming for this ><
# friends_list = list()
# followers_list_2 = list()


# In this example, the handler is time.sleep(15 * 60),
# but you can of course handle it in any way you want.
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print("Rate Limit reached-- waiting...", flush=True)
            time.sleep(15 * 60)
        except StopIteration:
            break


def friends_from_twitter(target_name):
    friends_list = list()
    flist = limit_handled(tweepy.Cursor(api.friends, screen_name=target_name).items())
    for friend in flist:
        try:
            friends_list.append(friend.screen_name)
        except tweepy.RateLimitError:
            print("Rate Limit reached-- waiting...", flush=True)
            time.sleep(15 * 60)
    friends_list.append(target_name)
    return friends_list


def follows_from_twitter(target_name):
    friends_list = list()
    flist = limit_handled(tweepy.Cursor(api.followers, screen_name=target_name).items())
    for friend in flist:
        try:
            friends_list.append(friend.screen_name)
        except tweepy.RateLimitError:
            print("Rate Limit reached-- waiting...", flush=True)
            time.sleep(15 * 60)
    friends_list.append(target_name)
    return friends_list


# get a list of the people following target_name
def get_friends(target_name):
    if friends_file is not None:
        friends_list = list()
        try:
            with open(friends_file) as inf:
                for line in inf:
                    friends_list.append(line.rstrip("\n"))
            print("Friend list collected.", flush=True)
        except FileNotFoundError as e:
            print(e, flush=True)
            # decide what to do here
            # or more like, I may as well just decide for myself:
            return None
    else:
        friends_list = friends_from_twitter(target_name)
        print("Friend list collected.", flush=True)
    return friends_list


def get_follows(target_name):
    if follows_file is not None:
        friends_list = list()
        try:
            with open(follows_file) as inf:
                for line in inf:
                    friends_list.append(line.rstrip("\n"))
            print("Follower list collected.", flush=True)
        except FileNotFoundError as e:
            print(e, flush=True)
            # decide what to do here
            # or more like, I may as well just decide for myself:
            return None
    else:
        friends_list = follows_from_twitter(target_name)
        print("Follower list collected.", flush=True)
    return friends_list


# do stuff with the list you just got
def get_friends_of_friends(friends_list):
    foff_list = list()
    try:
        for friend in friends_list:
            try:
                user = api.get_user(friend)
                foff_list.append((user.screen_name, user.friends_count))
            #    print(str(len(foff_list)), flush=True)
            except tweepy.RateLimitError:
                print("Rate Limit reached-- waiting...", flush=True)
                time.sleep(15 * 60)
            except tweepy.TweepError:
                pass
    except NameError:
        pass
    return foff_list


def get_follows_of_follows(friends_list):
    foff_list = list()
    try:
        for friend in friends_list:
            try:
                user = api.get_user(friend)
                foff_list.append((user.screen_name, user.followers_count))
            #    print(str(len(foff_list)), flush=True)
            except tweepy.RateLimitError:
                print("Rate Limit reached-- waiting...", flush=True)
                time.sleep(15 * 60)
            except tweepy.TweepError:
                pass
    except NameError:
        pass
    return foff_list


friend_list = get_friends_of_friends(get_friends(TARGET_NAME))
follower_list = get_follows_of_follows(get_follows(TARGET_NAME))

try:
    with open("tw_friends.txt", 'w') as of:
        for line in friend_list:
            of.write(str(line) + "\n")
    with open("tw_follows.txt", 'w') as of:
        for line in follower_list:
            of.write(str(line) + "\n")
except Exception as e:
    print(e)
