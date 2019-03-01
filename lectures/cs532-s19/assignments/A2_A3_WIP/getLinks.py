import tweepy
import json
import argparse
# consumer key, consumer secret, access token, access secret.


ckey = "g9QwxyzRoMI2YVNgWIi0lTzlV"
csecret = "tRrBSizC15gLS0Kyco6E5Hl1B6a1jDrPSjcXVGbvq6hV3uaLqd"
atoken = "2592291038-HIOrJ8CY48iy0qeaOvSvKEZRllL03A31vSMNcc9"
asecret = "BpQkp51FF0z9MPWyK44OyYKmFEXR7ScLp1oxsmOawK6LM"
result_urls = set()

parser = argparse.ArgumentParser(description='''Collects 1300 links
                                                from Twitter''')
parser.add_argument('infile', metavar='F',  nargs='?',
                    help='.txt partial list of links')
parser.add_argument('output', metavar='O',  nargs='?',
                    default="result_urls.txt",
                    help=""".txt name for output file.
                     (default: "result_urls.txt")""")
args = parser.parse_args()

partial_list = args.infile
outfile = args.output

print("Outputting to '" +outfile +"'.")

if(partial_list):
    print("Found file '" + partial_list + "'...", flush=True)
    with open(partial_list) as f:
        for url in f:
            result_urls.add(url)
    print("URLs loaded from file.", flush=True)

of = open(outfile, "a")
for url in result_urls:
    of.write(url+ '\n')


class listener(tweepy.StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        if "entities" in all_data:
            urls = all_data["entities"]["urls"]
            if (len(urls) > 0):
                new_url = str(urls[0]["expanded_url"])
                if (new_url.find("twitter.com/") < 0):
                    try:
                        of.write(new_url + '\n')
                        result_urls.add(new_url)
                    except UnicodeEncodeError:
                        pass                        
                    if (len(result_urls) > 200):
                        of.close()
                        return(False)
        return(True)

    def on_error(self, status):
        print("status")


auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = tweepy.Stream(auth, listener())
twitterStream.filter(track="now")
