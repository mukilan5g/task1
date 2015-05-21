import argparse
from sys import argv

from count_lib import *

#GETS the respsonce from url 
#COLLECTS the contents
#COUNT the frequency of the words
#SORT the words in *descending* based on their frequency 
def main(n):
	words = collect_contents(url_responce().read().lower())
	stop_words = read_stop_words()
	countwords = count_frequeny(words,stop_words)
	sorted_list =  sort_desc(countwords)
	for content in sorted_list[0:n]:
		print '%s : %d'%content

#DEFINING the named_argument *n* as an integer with default value 10
parser = argparse.ArgumentParser()
parser.add_argument('-n',dest='n',default=10,type=int)
args = parser.parse_args()

#CALL the main function with command_line_arguments
main(args.n)