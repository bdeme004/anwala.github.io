from boilerpipe.extract import Extractor
import argparse

parser = argparse.ArgumentParser(description='''Extract text from files''')
parser.add_argument('-s', '--silent', action='store_true', help='suppress status reports')
args = parser.parse_args()

silent = args.silent
file_list = list()

with open("results_curl.txt") as inf:
    for line in inf:
        file_list.append(line.rstrip("\n"))
    if not silent:
        print("filenames loaded.", flush=True)

for url in file_list:
    output = "results/text/" + url
    input = "results/curl/" + url
    try:
        with open(input) as inp:
            content = inp.read()
    except Exception as e:
        print(e)
    try:
        extractor = Extractor(extractor='ArticleExtractor', html=content)
        extracted_text = extractor.getText()
        with open(output, 'w') as of:
            of.write(str(extracted_text.encode(errors='replace')))
            if not silent:
                print("extracted-" + str(file_list.index(url)), flush=True)
    except Exception as e:
        print(e, flush=True)
