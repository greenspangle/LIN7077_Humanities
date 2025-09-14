# LIN7077 Test 3rd Assignment

# updated afternoon Tuesday 24 October 2023
# Place this in the same folder as your python script
# replace 'a1_answers' with the name of your answer script
# then run this python program script from IDLE

from assignment_student_submissions.a3_submissions.a3_220398932_v2 import *
#from a3_answers import *

# import the following libraries from the Python standard library
import unittest
import types
import sys

# check this is Python 3
if not sys.version[0] == '3':
    print("Must be version 3")
    exit(-1)  # exit with error code

# get a list of what's been implemented
implemented = dir()


class TestStringMethods(unittest.TestCase):

    @unittest.skipIf('robber_lingo' not in implemented,
                     'robber_lingo() not implemented')
    def test_robber_lingo(self):
        self.assertIsInstance(robber_lingo, types.FunctionType)
        self.assertEqual(robber_lingo("this is fun"), "tothohisos isos fofunon")

    @unittest.skipIf('char_counts' not in implemented,
                     'char_counts() not implemented')
    def test_char_counts(self):
        self.assertIsInstance(char_counts, types.FunctionType)
        self.assertEqual(char_counts(''), (0, 0, 0, 0))
        self.assertEqual(char_counts(' '), (0, 0, 0, 1))
        self.assertEqual(char_counts('a'), (1, 0, 0, 0))
        self.assertEqual(char_counts('z'), (0, 1, 0, 0))
        self.assertEqual(char_counts('1'), (0, 0, 1, 0))
        self.assertEqual(char_counts('?'), (0, 0, 0, 1))

        self.assertEqual(char_counts('aAa'), (3, 0, 0, 0))
        self.assertEqual(char_counts('rhythm'), (0, 6, 0, 0))
        self.assertEqual(char_counts('?'), (0, 0, 0, 1))
        self.assertEqual(char_counts('aebre? 535 code.3.ibra'), (7, 6, 4, 5))
        self.assertEqual(char_counts('abracadabra'), (5, 6, 0, 0))

    @unittest.skipIf('seq_collections' not in implemented,
                     'seq_collections() not implemented')
    def test_seq_collections(self):
        self.assertIsInstance(seq_collections, types.FunctionType)
        self.assertEqual(seq_collections(1), ('1', {1}, [[], [1]]))
        self.assertEqual(seq_collections(2), ('1 2', {1, 2}, [[2], [1]]))
        self.assertEqual(seq_collections(5),
                         ('1 2 3 4 5', {1, 2, 3, 4, 5}, [[2, 4], [5, 3, 1]]))
        self.assertEqual(seq_collections(11),
                         ('1 2 3 4 5 6 7 8 9 10 11',
                          {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},
                          [[2, 4, 6, 8, 10], [11, 9, 7, 5, 3, 1]])
                         )

    @unittest.skipIf('fiddledee_dict' not in implemented,
                     'fiddledee_dict() not implemented')
    def test_fiddledee_dict(self):
        self.assertIsInstance(fiddledee_dict, types.FunctionType)
        self.assertEqual(fiddledee_dict(1), {1: '1'})
        self.assertEqual(fiddledee_dict(2), {1: '1', 2: 'Dee'})
        self.assertEqual(fiddledee_dict(3), {1: '1', 2: 'Dee', 3: 'Fiddle'})
        self.assertEqual(fiddledee_dict(5),
                         {1: '1', 2: 'Dee', 3: 'Fiddle', 4: 'Dee',
                          5: '5'})
        self.assertEqual(fiddledee_dict(7),
                         {1: '1', 2: 'Dee', 3: 'Fiddle', 4: 'Dee',
                          5: '5', 6: 'FiddleDee', 7: '7'})

    @unittest.skipIf('char_count_dict' not in implemented,
                     'char_count_dict() not implemented')
    def test_char_count_dict(self):
        self.assertIsInstance(char_count_dict, types.FunctionType)
        self.assertEqual(char_count_dict(''), {})
        self.assertEqual(char_count_dict('1'), {'1': 1})
        self.assertEqual(char_count_dict('a'), {'a': 1})
        self.assertEqual(char_count_dict('aaa'), {'a': 3})
        self.assertEqual(char_count_dict('aAa'), {'a': 2, 'A': 1})
        self.assertEqual(char_count_dict('abb ab ab'), {'a': 3, 'b': 4, ' ': 2})
        self.assertEqual(char_count_dict('abracadabra'),
                         {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

    @unittest.skipIf('fiddledee_dict' not in implemented,
                     'fiddledee_dict() not implemented')
    def test_word_count_dict(self):
        self.assertEqual(word_count_dict(''), {})
        self.assertEqual(word_count_dict('a'), {'a': 1})
        self.assertEqual(word_count_dict('aaa'), {'aaa': 1})
        self.assertEqual(word_count_dict('aaa aaa'), {'aaa': 2})
        self.assertEqual(word_count_dict('  aaa  '), {'aaa': 1})
        self.assertEqual(word_count_dict('aaa bbb'), {'aaa': 1, 'bbb': 1})
        self.assertEqual(word_count_dict('  aaa  bbb  '), {'aaa': 1, 'bbb': 1})
        self.assertEqual(word_count_dict('ab a ab cde ab'),
                         {'ab': 3, 'a': 1, 'cde': 1})
        self.assertEqual(word_count_dict("jane's escapade"),
                         {'jane': 1, 's': 1, 'escapade': 1})

    @unittest.skipIf('isa_pangram' not in implemented,
                     'isa_pangram() not implemented')
    def test_isa_pangram(self):
        self.assertIsInstance(isa_pangram, types.FunctionType)
        self.assertTrue(
            isa_pangram('the quick brown fox jumps over the lazy dog'))
        self.assertTrue(
            isa_pangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'))
        self.assertTrue(isa_pangram(
            'the quick brown fox \n\t?<!>? jumps over the lazy dog'))
        self.assertFalse(
            isa_pangram('the quick brown fox jumped over the lazy dog'))

    @unittest.skipIf('zip_2' not in implemented,
                     'zip_2() not implemented')
    def test_zip_2(self):
        self.assertIsInstance(zip_2, types.FunctionType)
        self.assertEqual(zip_2('', ''), '')
        self.assertEqual(zip_2('@', ''), '@')
        self.assertEqual(zip_2('', '@'), '@')
        self.assertEqual(zip_2('a', 'x'), 'ax')
        self.assertEqual(zip_2('x', 'a'), 'ax')
        self.assertEqual(zip_2('ab', 'xy'), 'abxy')
        self.assertEqual(zip_2('xy', 'ab'), 'abxy')
        self.assertEqual(zip_2('abc', 'def'), 'abcdef')

    @unittest.skipIf('zip_n' not in implemented,
                     'zip_n() not implemented')
    def test_zip_n(self):
        self.assertIsInstance(zip_2, types.FunctionType)
        self.assertEqual(zip_n(), '')
        self.assertEqual(zip_n(''), '')
        self.assertEqual(zip_n('a'), 'a')
        self.assertEqual(zip_n('abc'), 'abc')
        self.assertEqual(zip_n('', ''), '')
        self.assertEqual(zip_n('a', ''), 'a')
        self.assertEqual(zip_n('', 'a'), 'a')
        self.assertEqual(zip_n('a', 'b'), 'ab')
        self.assertEqual(zip_n('b', 'a'), 'ab')
        self.assertEqual(zip_n('ade', 'cf'), 'acdef')
        self.assertEqual(zip_n('a', '', ''), 'a')
        self.assertEqual(zip_n('', 'a', ''), 'a')
        self.assertEqual(zip_n('', '', 'a'), 'a')
        self.assertEqual(zip_n('', 'b', 'a'), 'ab')
        self.assertEqual(zip_n('b', '', 'a'), 'ab')
        self.assertEqual(zip_n('b', 'a', ''), 'ab')
        self.assertEqual(zip_n('a', 'b', 'c'), 'abc')
        self.assertEqual(zip_n('ab', 'xy', 'wz'), 'abwxyz')
        self.assertEqual(zip_n('abc', 'def', 'ghj'), 'abcdefghj')
        self.assertEqual(zip_n('a', 'bu', 'ct', 'z', 'ds', 'er', 'f'),
                         'abcdefrstuz')

    @unittest.skipIf('caesar' not in implemented,
                     'caesar() not implemented')
    def test_caesar(self):
        self.assertIsInstance(caesar, types.FunctionType)

        self.assertEqual(caesar(''), '')
        self.assertEqual(caesar('a'), 'd')
        self.assertEqual(caesar('A'), 'D')
        self.assertEqual(caesar('x'), '0')
        self.assertEqual(caesar(' '), 'c')
        self.assertEqual(caesar(' ', 4), 'd')
        self.assertEqual(caesar('a', 5), 'f')
        self.assertEqual(caesar('A', 5), 'F')
        self.assertEqual(caesar('f', 5, False), 'a')
        self.assertEqual(caesar('a', 6, alphabet='abdef'), 'b')
        self.assertEqual(caesar('a', 6, alphabet='aBdEf'), 'B')
        self.assertEqual(caesar('B', 6, alphabet='aBdEf'), 'd')

        self.assertEqual(caesar('Caesar Cipher'), 'FdhvducFlskhu')
        self.assertEqual(caesar('secret msg', encode=False), 'pb obq,jpd')
        self.assertEqual(caesar('Caesar Cipher', shift=17), 'Trv9r8qTz6yv8')
        self.assertEqual(caesar('Trv9r8qTz6yv8', encode=False, shift=17),
                         'Caesar Cipher')
        self.assertEqual(
            caesar('eddcbad!', alphabet='fedc bma', encode=False, shift=17),
            'feed me!')


if __name__ == '__main__':
    unittest.main()
