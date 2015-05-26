import unittest
import urllib2

from count_lib import *


class TestCount(unittest.TestCase):

    # DEFINE and INITIALIZE the variables.
    global str
    str = '''he is the hero of the movie called *Egypt*!!!,
        \n and he is born in \t egypt'''

    # CALL the url_responce function with the url that isn't even exists
    # CHECK whether the url_responce function handles that.
    def test_url_responce_pass_not_exists(self):
        self.assertRaises(type(urllib2.URLError),
                          url_responce(('http://grepcode.com/repo1.maven.' +
                                        'org/maven2/org.apache.bigtop.itest/' +
                                        'hadoop-smoke/0.2.0-incubating/' +
                                        'examples/text/pg11.txt/?v=source')))

    # CALL the url_responce function with out passing any url.
    # CHECK whether the url_responce function take the default url.
    def test_url_responce_pass_null(self):
        self.assertTrue(url_responce())

    # CALL the url_responce function with forbidden webpage.
    # CHECK whether the function handles it.
    def test_url_responce_forbidden(self):
        self.assertRaises(type(urllib2.HTTPError),
                          url_responce(('http://www.gutenberg.org/' +
                                        'cache/epub/11/pg11.txt')))

    # CALL the read_stop_words function with the file that doesn't exists
    # CHECK it handles it.
    def test_stop_words_pass_invalid(self):
        self.assertRaises(type(IOError),
                          read_stop_words(('C:\Users\mukilan\Desktop\'' +
                                           'stop_word.txt')))

    # CALL the read_stop_words with out passing any filepath
    # CHECK whether it returns contents of local stop words file.
    def test_stop_words_pass_null(self):
        with open('C:\Users\mukilan\Desktop\stop_words.txt', 'r') as file:
                    self.assertEqual(file.read(), read_stop_words())

    # CALL the collect_contents function
    # WITH string that contains special characters and symbols.
    # CHECK whether it *avoids* those *special characters* and *symbols*.
    def test_collect_contents(self):
        self.assertEqual(['he', 'is', 'the', 'hero', 'of',
                          'the', 'movie', 'called', 'egypt', 'and',
                          'he', 'is', 'born', 'in', 'egypt'],
                         collect_contents(str.lower()))

    # CHECK whether the collect_contents function returns any non word.
    def test_collect_contents_non_word(self):
        self.assertFalse(True in
                         (map(lambda non_word: non_word in
                              [words for words in
                               collect_contents(str.lower())],
                              re.findall(r'\W+', str))))

    # PASS list of words and list of stop words in count_frequeny function.
    # CHECK whether the function avoids the stop words
    # COUNTS the frequency of other words.
    def test_count_frequeny(self):
        frequency_list = count_frequeny(collect_contents(str.lower()),
                                        ['a', 'the', 'he',
                                         'of', 'and', 'in', 'is'])
        self.assertFalse(True in
                         (map(lambda stop_word:
                              stop_word in [words for words, count
                                            in frequency_list],
                              ['a', 'the', 'he', 'of',
                               'and', 'in', 'is'])))

    # CHECK whether it counts correctly.
    def test_count_frequeny_cardinalilty(self):
        frequency_list = count_frequeny(collect_contents(str.lower()),
                                        ['a', 'the', 'he',
                                         'of', 'and', 'in', 'is'])
        self.assertEqual([('hero', 1), ('egypt', 2), ('born', 1),
                          ('movie', 1), ('called', 1)],
                         frequency_list)

    # PASS the list of tuples in sort_desc function
    # CHECK whether it sorts the list in desc based on frequency of words.
    # CROSS-CHECK by reversing the list.
    def test_sort_desc(self):
        frequency_list = count_frequeny(collect_contents(str.lower()),
                                        ['a', 'the', 'he',
                                         'of', 'and', 'in', 'is'])
        self.assertEqual([('egypt', 2), ('hero', 1), ('born', 1),
                          ('movie', 1), ('called', 1)],
                         sort_desc(frequency_list))
        self.assertEqual(sorted([('egypt', 2), ('hero', 1), ('born', 1),
                                 ('movie', 1), ('called', 1)],
                                reverse=True),
                         sorted(sort_desc(frequency_list), reverse=True))

if __name__ == '__main__':
    unittest.main()
