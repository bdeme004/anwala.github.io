from boilerpipe.extract import Extractor

file_list = list()

with open("results-curl.txt") as inf:
    for line in inf:
        file_list.append(line.rstrip("\n"))

for url in file_list:
    output = "results/new/" + url
    input = "results/curl/" + url
    with open(input) as inp:
        content = inp.read()
    try:
        extractor = Extractor(extractor='ArticleExtractor', html=content)
        extracted_text = extractor.getText()
        with open(output, 'w') as of:
            of.write(str(extracted_text.encode(errors='replace')))
    except:
        pass
