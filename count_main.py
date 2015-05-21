import argparse
from sys import argv
from count_lib import *

def main(n):
	words = collect_contents(url_responce().read().lower())
	stop_words = read_stop_words()
	countwords = count_frequeny(words,stop_words)
	sorted_list =  sort_desc(countwords)
	for content in sorted_list[0:n]:
		print '%s : %d'%content


parser = argparse.ArgumentParser()
parser.add_argument('-n',dest='n',default=10,type=int)
args = parser.parse_args()
main(args.n)