import re
import urllib2
from collections import *
from operator import itemgetter


# GETS the response from the url
def url_response(url_path=('http://grepcode.com/file/' +
                           'repo1.maven.org/maven2/org.apache.bigtop.itest/' +
                           'hadoop-smoke/0.2.0-incubating/examples' +
                           '/text/pg11.txt')):
    try:
        return urllib2.urlopen(url_path)
    except urllib2.HTTPError as e:        # Thrown: forbidden
        print e
    except urllib2.URLError as e:        # Thrown: no network, server not found
        print e


# COLLECTS the word characters from a string
def collect_contents(str, format=r'\w+'):
    return re.findall(format, str)


# READS the stop words from the file
def read_stop_words(filepath=('C:\Users\mukilan\Desktop\stop_words.txt'),
                    mode='r'):
    try:
        with open(filepath, mode) as file:
            return file.read()
    except IOError as e:        # Exception thrown when the file not exists
        print e


# COUNTS the frequency of the words, except the stop words
def count_frequency(list_str, stop_words):
    return [(word, count)
            for word, count in Counter(list_str).items()
            if word not in stop_words]


# SORTS the list in descending order based on the frequency of the word
def sort_desc(sort_list):
    return sorted(sort_list, key=itemgetter(1), reverse=True)
