# LIN7077 Test 4th Assignment
#############################################################################
# Place this in the same folder as your python script
# replace 'a4_answers' with the name of your answer script
# then run this python program script from IDLE
from a4_answers import *
#############################################################################

# import the following libraries from the Python standard library
import unittest
import types
import sys

# check this is Python 3
if not sys.version[0] == '3':
    print("Must be version 3")
    exit(-1)  # exit with error code

##############################################################################
#      Define some HELPER functions and default values for testing         ###
##############################################################################

# get a list of what's been implemented
implemented = dir()

test_filename = 'test_data.txt'


def str_to_file(a_str, f_name=test_filename):
    """Create a file from a string and return the file name."""
    with open(f_name, mode='wt', encoding='utf-8') as tf:  # open the file
        tf.write(a_str)  # write content
    # file automatically closed at end of indentation block
    return f_name  # return the name of the file


def file_to_str(f_name=test_filename):
    """Read the file and return its contents as a string."""
    with open(f_name, mode='rt', encoding='utf-8') as tf:  # open the file
        f_content = tf.read()  # read entire contents
        # return contents as a string
        return f_content


##############################################################################
# Now start testing
##############################################################################
# unittest pattern
#       self.assertCondition(thing_being_tested, expected_result, error_msg)
##############################################################################

class TestStringMethods(unittest.TestCase):

    @unittest.skipIf('temperature_FtoC' not in implemented,
                     'temperature_FtoC() not implemented')
    def test_temperature_FtoC(self):
        self.assertIsInstance(temperature_FtoC, types.FunctionType)
        self.assertAlmostEqual(temperature_FtoC(212), 100, places=8)
        self.assertAlmostEqual(temperature_FtoC(32), 0, places=8)
        self.assertAlmostEqual(temperature_FtoC(-40), -40, places=8)

    @unittest.skipIf('thermostat' not in implemented,
                     'thermostat() not implemented')
    def test_thermostat(self):
        self.assertIsInstance(thermostat, types.FunctionType)
        self.assertIn(thermostat(19), ('stet', 'stat'))
        self.assertIn(thermostat(21), ('stet', 'stat'))
        self.assertIn(thermostat(24), ('stet', 'stat'))

        self.assertIn(thermostat(18), ('heat on', 'on'))
        self.assertIn(thermostat(24.0001), ('heat off', 'off'))

        self.assertIn(thermostat(-999), ('heat on', 'on'))
        self.assertIn(thermostat(+999), ('heat off', 'off'))

    @unittest.skipIf('read_alternate_chars' not in implemented,
                     'read_alternate_chars() not implemented')
    def test_read_alternate_chars(self):
        self.assertIsInstance(read_alternate_chars, types.FunctionType)
        self.assertEqual(read_alternate_chars(str_to_file('1234567')),
                         (set('1357'), set('246')))
        self.assertEqual(read_alternate_chars(str_to_file('abc123')),
                         (set('ac2'), set('b13')))
        self.assertEqual(read_alternate_chars(str_to_file('')),
                         (set(''), set('')))
        self.assertEqual(read_alternate_chars(str_to_file('1')),
                         (set('1'), set('')))
        self.assertEqual(read_alternate_chars(str_to_file('12')),
                         (set('1'), set('2')))

    @unittest.skipIf('write_ints' not in implemented,
                     'write_ints() not implemented')
    def test_write_ints(self):
        self.assertIsInstance(read_alternate_chars, types.FunctionType)

        write_ints(test_filename, 0)
        result = ''
        self.assertIn(file_to_str(), (result, result + '\n'))

        write_ints(test_filename, 1)
        result = '1 - 1'
        self.assertIn(file_to_str(), (result, result + '\n'))

        write_ints(test_filename, 2)
        result = '2 - 1\n2 - 2 4'
        self.assertIn(file_to_str(), (result, result + '\n'))

        write_ints(test_filename, 5)
        result = '5 - 1\n5 - 2 4\n5 - 3 6 9\n5 - 4 8 12 16\n5 - 5 10 15 20 25'
        self.assertIn(file_to_str(), (result, result + '\n'))

    @unittest.skipIf('read_ints_csv' not in implemented,
                     'read_ints_csv() not implemented')
    def test_read_ints_csv(self):
        self.assertIsInstance(read_ints_csv, types.FunctionType)

        # refine the assignment to cope with fields with
        # leading and trailing spaces
        str_to_file('', test_filename)
        self.assertTrue(read_ints_csv(test_filename))

        str_to_file('1,1', test_filename)
        self.assertTrue(read_ints_csv(test_filename))

        str_to_file('1,2,3,4,5,15', test_filename)
        self.assertTrue(read_ints_csv(test_filename))

        str_to_file('1,2,3,4,5,15', test_filename)
        self.assertTrue(read_ints_csv(test_filename))

        str_to_file('9,9,9,9,9,9,9,9,9,9,9,99', test_filename)
        self.assertTrue(read_ints_csv(test_filename))

        str_to_file('1', test_filename)
        self.assertFalse(read_ints_csv(test_filename))

        str_to_file('3,2,1,5', test_filename)
        self.assertFalse(read_ints_csv(test_filename))

        str_to_file('9,1,8,2,10', test_filename)
        self.assertFalse(read_ints_csv(test_filename))

        str_to_file('3,2,1', test_filename)
        self.assertFalse(read_ints_csv(test_filename))

    @unittest.skipIf('write_random' not in implemented,
                     'write_random() not implemented')
    def test_write_random(self):
        self.assertIsInstance(write_random, types.FunctionType)

        # only test two things:
        #     file length is correct
        #     all characters in file are in alphabet
        # =======
        # this is because different ways of selecting the characters
        # results in different sequences

        import random  # set random.seed before every test
        seed_test_value = 1234
        default_filename = 'random_chars.txt'
        default_len = 7077
        default_alphabet = '0123456789'

        # define two helper functions
        def correct_answer(size=default_len, alphabet=default_alphabet):
            random.seed(seed_test_value)
            return ''.join(random.choices(alphabet, k=size))

        def student_answer(filename=default_filename,
                           size=default_len,
                           alphabet=default_alphabet):
            random.seed(seed_test_value)
            write_random(filename, size, alphabet)
            return file_to_str(default_filename)

        # test default values are correct
        st_str = student_answer()
        self.assertEqual(len(st_str), default_len)
        self.assertEqual(all([i in default_alphabet for i in st_str]), True)

        # test size is correct
        test_size = 27
        st_str = student_answer(size=test_size)
        self.assertEqual(len(st_str), test_size)
        self.assertEqual(all([i in default_alphabet for i in st_str]), True)

        # test alphabet is correct
        test_alphabet = '!£$%^&*'
        st_str = student_answer(alphabet=test_alphabet)
        self.assertEqual(len(st_str), default_len)
        self.assertEqual(all([i in test_alphabet for i in st_str]), True)

        # test both work together
        test_size = 1234
        test_alphabet = 'abc678!£$%^&*'
        st_str = student_answer(size=test_size, alphabet=test_alphabet)
        self.assertEqual(len(st_str), test_size)
        self.assertEqual(all([i in test_alphabet for i in st_str]), True)
        #
        #
        #
        #
        #
        #
        #

    @unittest.skipIf('is_alphabetical' not in implemented,
                     'is_alphabetical() not implemented')
    def test_is_alphabetical(self):
        self.assertIsInstance(is_alphabetical, types.FunctionType)
        # TESTS
        self.assertTrue(is_alphabetical(''))
        self.assertTrue(is_alphabetical('a'))
        self.assertTrue(is_alphabetical('ab'))
        self.assertTrue(is_alphabetical('aa'))
        self.assertTrue(is_alphabetical('aaaaaaaaaaaaaaaaaaaaaaaaaa'))
        self.assertTrue(is_alphabetical('ace'))

        self.assertFalse(is_alphabetical('abbab'))
        self.assertFalse(is_alphabetical('aazaa'))
        self.assertFalse(is_alphabetical('zzaa'))
        self.assertFalse(is_alphabetical('xb'))

    @unittest.skipIf('deal' not in implemented,
                     'deal() not implemented')
    def test_deal(self):
        self.assertIsInstance(deal, types.FunctionType)
        # setup
        suits = 'clubs diamonds hearts spades'.split(' ')
        faces = ('ace 2 3 4 5 6 7 8 9 10'
                 ' knave queen king').split(' ')
        deck_as_tuples = []
        for s in suits:
            for f in faces:
                deck_as_tuples.append((f, s))
        # deck created as tuple for each card

        # WRITE TESTS
        # visually inspect code and output
        # test output length and that all tuples are in a deck

        cards = deal(1)
        self.assertEqual(len(set(cards)), 1)
        for card in cards:
            self.assertTrue(card in deck_as_tuples)

        cards = deal(2)
        self.assertEqual(len(set(cards)), 2)
        for card in cards:
            self.assertTrue(card in deck_as_tuples)

        cards = deal(51)
        self.assertEqual(len(set(cards)), 51)
        for card in cards:
            self.assertTrue(card in deck_as_tuples)

    @unittest.skipIf('write_html' not in implemented,
                     'write_html() not implemented')
    def test_write_html(self):
        self.assertIsInstance(write_html, types.FunctionType)
        # TEST SETUP

        default_filename = 'webpage.html'
        default_a_str = 'LIN7077 - Programming for the Humanities'
        a_str = default_a_str
        default_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>{a_str}</p>

</body>
</html>"""
        # TESTS
        import os
        write_html()
        self.assertTrue(os.path.isfile(default_filename))
        write_html(filename='some random filename.txt')
        self.assertTrue(os.path.isfile('some random filename.txt'))
        write_html('some random filename.txt', 'some random filename.txt')
        self.assertTrue(os.path.isfile('some random filename.txt'))

    @unittest.skipIf('ascending_SKIP' not in implemented,
                     'ascending() not implemented')
    def test_ascending(self):
        self.assertIsInstance(ascending, types.FunctionType)
        # WRITE TESTS
        self.assertEqual(ascending(str_to_file('')), ((0, 0), (0, 0)))
        self.assertEqual(ascending(str_to_file('z')), ((0, 1), (0, 1)))
        self.assertEqual(ascending(str_to_file('ababcb')), ((0, 6), (2, 3)))

        self.assertEqual(ascending(
            str_to_file('testedresult'), 'est'), ((0, 5), (1, 3)))
        self.assertEqual(
            ascending(str_to_file('testedresult'), 'tse'), ((0, 5), (1, 1)))
        self.assertEqual(
            ascending(str_to_file('ababcccdab'), 'abcccd'), ((0, 9), (2, 8)))
        self.assertEqual(
            ascending(str_to_file('abra cadabra'), 'abr'), ((5, 7), (0, 3)))
