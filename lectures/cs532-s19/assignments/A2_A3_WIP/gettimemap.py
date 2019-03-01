import argparse
import requests
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(description='''Checks links for link''')
parser.add_argument('infile', metavar='F',  nargs='?', default="result_urls_mem.txt",
                    help='.txt list of links')
parser.add_argument('output', metavar='O',  nargs='?',
                    default="result_urls_mem.txt",
                    help=""".txt name for output file.
                     (default: "result_urls_limited.txt")""")
args = parser.parse_args()

infile = args.infile
outfile = args.output

mem_count_list = list()
mem_count_dict = dict()

with open(infile) as inf:
    for line in inf:
        r = requests.get(line)
        timemap = r.text
        mem_num =(timemap.count('rel="first memento"')
                              + timemap.count('rel="memento"')
                              + timemap.count('rel="last memento"'))
        mem_count_list.append(mem_num)



plt.hist(mem_count_list, 50, density=1)
plt.show()