import unittest

from count_lib import *

class TestCount(unittest.TestCase):

	#DEFINE and INITIALIZE the variables.
	contents = collect_contents('how am i suppose to get out of this hell!! damn these fools\nidoits\tlosers')
	
	
	#pass the url that isn't even exists and check whether the url_responce function handles that.
	def test_url_responce(self):
		self.assertRaises('exception thrown', url_responce('http://grepcode.com/repo1.maven.org/maven2/org.apache.bigtop.itest/hadoop-smoke/0.2.0-incubating/examples/text/pg11.txt/?v=source'))
	
	#pass the file that doesn't exist and check whether it handles that.
	def test_stop_words(self):
		self.assertRaises('exception thrown',read_stop_words('C:\Users\mukilan\Desktop\stop_word.txt'))	
	
	#pass the string to collect_contents function that contains special characters and symbols. 
	#And check whether it avoids those special characters and symbols .
	#And produce the word character that matches (Letter|Number).
	def test_collect_contents(self):
		self.assertEqual(['how', 'am', 'i', 'suppose', 'to', 'get', 'out', 'of', 'this', 'hell', 'damn', 'these', 'fools', 'idoits', 'losers'], contents)
	
	#pass list of words and list of stop words. And check whether the function avoids the stop words and counts the frequency of other words. 
	def test_count_frequeny(self):
		str= 'he is the hero of the movie called Egypt,and he is born in egypt'
		frequency_list = count_frequeny(collect_contents(str.lower()), ['a', 'the', 'he', 'of', 'and', 'in', 'is'])
		self.assertEqual([('hero', 1),('egypt', 2),('born', 1),('movie', 1),('called', 1)], frequency_list)
	
	#pass the list of tuples in sort desc function 
	#check whether it sorts the list descending order based on the frequency of the words
	def test_sort_desc(self):
		self.assertEqual([('egypt',2),('hero',1),('born',1),('movie',1),('called',1)],sort_desc([('hero',1),('egypt',2),('born',1),('movie',1),('called',1)]))
		
if __name__ == '__main__':
    unittest.main()