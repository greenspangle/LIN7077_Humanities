# LIN6209 Test 2nd Assignment

# updated Saturday 23 November 2024
# Place this in the same folder as your python script
# replace 'a2_answers' with the name of your answer script
# then run this python program script from IDLE
# from a2_answers import *

from assignment_student_submissions.a2_submissions.marked.a2_220478810_test_a2 import *
# from a2_answers import *

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

    @unittest.skipIf('signum' not in implemented,
                     'signum() not implemented')
    def test_signum(self):
        self.assertIsInstance(signum, types.FunctionType)
        self.assertEqual(signum(11), 1, 'signum(11) failed')
        self.assertEqual(signum(11 / 3), 1, 'signum(11/3) failed')
        self.assertEqual(signum(0.000702), 1, 'signum(0.000702) failed')

        self.assertEqual(signum(0), 0, 'signum(0) failed')
        self.assertEqual(signum(-0), 0, 'signum(-0) failed')
        self.assertEqual(signum(1 - 1), 0, 'signum(1-1) failed')
        self.assertEqual(signum(10 * (1 - 1)), 0, 'signum(10*(1-1)) failed')

        self.assertEqual(signum(-1 / 2), -1, 'signum(-1/2) failed')
        self.assertEqual(signum(-11), -1, 'signum(-11) failed')
        self.assertEqual(signum(-1.123), -1, 'signum(-1.123) failed')

    @unittest.skipIf('contains_vowel' not in implemented,
                     'contains_vowel() not implemented')
    def test_contains_vowel(self):
        self.assertIsInstance(contains_vowel, types.FunctionType)
        self.assertIs(contains_vowel('aeiou'), True)
        self.assertIs(contains_vowel('AEIOU'), True)
        self.assertIs(contains_vowel('UOIEA'), True)
        self.assertIs(contains_vowel(' a  e  i  o  u '), True)
        self.assertIs(contains_vowel(' a   '), True)
        self.assertIs(contains_vowel('  e   '), True)
        self.assertIs(contains_vowel('   i    '), True)
        self.assertIs(contains_vowel('    o    '), True)
        self.assertIs(contains_vowel('     u    '), True)
        self.assertIs(contains_vowel(' a  e  i  o  u '), True)
        self.assertIs(contains_vowel(' a  e  i  o  u '), True)

        self.assertIs(contains_vowel('sky'), False)
        self.assertIs(contains_vowel('rhythm'), False)
        self.assertIs(contains_vowel('yacht'), True)
        self.assertIs(contains_vowel('vowel'), True)

        self.assertIs(contains_vowel('SKY'), False)
        self.assertIs(contains_vowel('RHYTHM'), False)
        self.assertIs(contains_vowel('YACHT'), True)
        self.assertIs(contains_vowel('VOWEL'), True)

        self.assertIs(contains_vowel(''), False)
        self.assertIs(contains_vowel('                   '), False)

    @unittest.skipIf('len_longest_2' not in implemented,
                     'len_longest_2() not implemented')
    def test_len_longest_2(self):
        self.assertIsInstance(len_longest_2, types.FunctionType)
        self.assertEqual(len_longest_2('', ''), 0)
        self.assertEqual(len_longest_2('a', 'b'), 1)
        self.assertEqual(len_longest_2('aa', 'b'), 2)
        self.assertEqual(len_longest_2('a', 'bb'), 2)

        self.assertEqual(len_longest_2('short', 'long'), 5)
        self.assertEqual(len_longest_2('long', 'short'), 5)
        self.assertEqual(len_longest_2('shorter', 'longer'), 7)
        self.assertEqual(len_longest_2('ORANGE', 'DAMSON'), 6)
        self.assertEqual(len_longest_2('a-ORANGE-a', 'b-PEaCH-b'), 10)

    @unittest.skipIf('len_longest_3' not in implemented,
                     'len_longest_3 not implemented')
    def test_len_longest_3(self):
        self.assertIsInstance(len_longest_3, types.FunctionType)

        self.assertEqual(len_longest_3('', '', ''), 0)

        self.assertEqual(len_longest_3('a', '', ''), 1)
        self.assertEqual(len_longest_3('', 'a', ''), 1)
        self.assertEqual(len_longest_3('', '', 'a'), 1)

        self.assertEqual(len_longest_3('a', 'a', ''), 1)
        self.assertEqual(len_longest_3('', 'a', 'a'), 1)
        self.assertEqual(len_longest_3('a', '', 'a'), 1)

        self.assertEqual(len_longest_3('a', 'a', 'a'), 1)

        self.assertEqual(len_longest_3('a', 'bb', 'ccc'), 3)
        self.assertEqual(len_longest_3('a', 'ccc', 'bb'), 3)
        self.assertEqual(len_longest_3('bb', 'a', 'ccc'), 3)
        self.assertEqual(len_longest_3('bb', 'ccc', 'a'), 3)
        self.assertEqual(len_longest_3('ccc', 'a', 'bb'), 3)
        self.assertEqual(len_longest_3('ccc', 'bb', 'a'), 3)
        self.assertEqual(len_longest_3('a', 'bb', 'ccc'), 3)

        self.assertEqual(len_longest_3('Peter', 'Piper', 'picked'), 6)

    @unittest.skipIf('len_middle_3' not in implemented,
                     'len_middle_3() not implemented')
    def test_len_middle_3(self):
        self.assertIsInstance(len_middle_3, types.FunctionType)

        self.assertEqual(len_middle_3('', '', ''), 0)

        self.assertEqual(len_middle_3('a', '', ''), 0)
        self.assertEqual(len_middle_3('', 'a', ''), 0)
        self.assertEqual(len_middle_3('', '', 'a'), 0)

        self.assertEqual(len_middle_3('a', 'a', ''), 1)
        self.assertEqual(len_middle_3('', 'a', 'a'), 1)
        self.assertEqual(len_middle_3('a', '', 'a'), 1)

        self.assertEqual(len_middle_3('a', 'a', 'a'), 1)

        self.assertEqual(len_middle_3('bb', 'a', 'a'), 1)
        self.assertEqual(len_middle_3('a', 'bb', 'a'), 1)
        self.assertEqual(len_middle_3('a', 'a', 'bb'), 1)

        self.assertEqual(len_middle_3('bb', 'bb', 'a'), 2)
        self.assertEqual(len_middle_3('a', 'bb', 'bb'), 2)
        self.assertEqual(len_middle_3('bb', 'a', 'bb'), 2)

        self.assertEqual(len_middle_3('a', 'bb', 'ccc'), 2)
        self.assertEqual(len_middle_3('a', 'cc', 'bb'), 2)
        self.assertEqual(len_middle_3('ccc', 'bb', 'a'), 2)
        self.assertEqual(len_middle_3('ccc', 'a', 'bb'), 2)
        self.assertEqual(len_middle_3('a', 'bb', 'ccc'), 2)
        self.assertEqual(len_middle_3('a', 'bb', 'ccc'), 2)
        self.assertEqual(len_middle_3('a', 'bb', 'ccc'), 2)

        self.assertEqual(len_middle_3('Peter', 'Piper', 'picked'), 5)

    @unittest.skipIf('isa_triangle' not in implemented,
                     'isa_triangle() not implemented')
    def test_isa_triangle(self):
        self.assertIsInstance(isa_triangle, types.FunctionType)

        # not a triangle
        self.assertEqual(isa_triangle(1, 2, 4), 0)
        self.assertEqual(isa_triangle(3, 7, 1), 0)
        self.assertEqual(isa_triangle(3, 3, 7), 0)
        self.assertEqual(isa_triangle(3, 7, 3), 0)
        self.assertEqual(isa_triangle(7, 3, 3), 0)

        # scalene
        self.assertEqual(isa_triangle(3, 4, 5), 1)
        self.assertEqual(isa_triangle(.3, .4, .5), 1)
        self.assertEqual(isa_triangle(0.0003, .0004, .0005), 1)

        # isosceles
        self.assertEqual(isa_triangle(3, 3, 2), 2)
        self.assertEqual(isa_triangle(3, 2, 3), 2)
        self.assertEqual(isa_triangle(2, 3, 3), 2)

        # equilateral
        self.assertEqual(isa_triangle(1, 1, 1), 3)
        self.assertEqual(isa_triangle(11, 11, 11), 3)
        self.assertEqual(isa_triangle(1.1, 1.1, 1.1), 3)

    @unittest.skipIf('score_2' not in implemented,
                     'score_2 not implemented')
    def test_score_2(self):
        self.assertIsInstance(score_2, types.FunctionType)
        # rule 1
        self.assertEqual(score_2(1, 2), 3)
        self.assertEqual(score_2(1, 5), 6)
        self.assertEqual(score_2(5, 1), 6)
        self.assertEqual(score_2(6, 5), 11)
        self.assertEqual(score_2(5, 6), 11)
        # rule 2
        self.assertEqual(score_2(1, 1), 3)
        self.assertEqual(score_2(2, 2), 6)
        self.assertEqual(score_2(3, 3), 9)
        self.assertEqual(score_2(4, 4), 12)
        self.assertEqual(score_2(5, 5), 15)
        # rule 3
        self.assertEqual(score_2(6, 6), 24)
        # rule 4
        self.assertEqual(score_2(1, 6), 14)
        self.assertEqual(score_2(2, 5), 14)
        self.assertEqual(score_2(3, 4), 14)
        self.assertEqual(score_2(4, 3), 14)
        self.assertEqual(score_2(5, 2), 14)
        self.assertEqual(score_2(6, 1), 14)

    @unittest.skipIf('score_4' not in implemented,
                     'score_4() not implemented')
    def test_score_4(self):
        self.assertIsInstance(score_4, types.FunctionType)
        # rule 1
        self.assertEqual(score_4(3, 2, 3, 3), 2)
        self.assertEqual(score_4(1, 1, 1, 1), 1)
        self.assertEqual(score_4(5, 5, 5, 1), 1)
        self.assertEqual(score_4(1, 2, 3, 4), 1)
        self.assertEqual(score_4(1, 6, 2, 5), 1)
        # rule 2
        self.assertEqual(score_4(1, 5, 6, 6), 7)
        self.assertEqual(score_4(1, 1, 2, 6), 7)
        self.assertEqual(score_4(3, 3, 3, 4), 7)
        #  rule 3
        self.assertEqual(score_4(2, 6, 1, 5), 14)
        self.assertEqual(score_4(2, 5, 2, 5), 14)
        self.assertEqual(score_4(2, 5, 5, 2), 14)
        self.assertEqual(score_4(6, 1, 1, 6), 14)
        # rule 4
        self.assertEqual(score_4(3, 3, 4, 4), 21)
        self.assertEqual(score_4(3, 4, 3, 4), 21)
        self.assertEqual(score_4(3, 4, 4, 3), 21)
        self.assertEqual(score_4(4, 3, 3, 4), 21)
        self.assertEqual(score_4(4, 3, 4, 3), 21)
        self.assertEqual(score_4(4, 4, 3, 3), 21)

    @unittest.skipIf('isa_leap_year' not in implemented,
                     'isa_leap_year() not implemented')
    def test_isa_leap_year(self):
        self.assertIsInstance(isa_leap_year, types.FunctionType)
        self.assertIs(isa_leap_year(1999), False)
        self.assertIs(isa_leap_year(75), False)
        self.assertIs(isa_leap_year(1000), False)
        self.assertIs(isa_leap_year(1900), False)
        self.assertIs(isa_leap_year(2000), True)
        self.assertIs(isa_leap_year(2024), True)

    @unittest.skipIf('true_date' not in implemented,
                     'true_date() not implemented')
    def test_true_date(self):
        self.assertIsInstance(true_date, types.FunctionType)
        # ordinary days
        self.assertIs(true_date(1, 1, 1), True)
        self.assertIs(true_date(2022, 10, 14), True)
        self.assertIs(true_date(2022, 10, 31), True)
        # leap year days
        self.assertIs(true_date(4, 2, 29), True)
        self.assertIs(true_date(8, 2, 29), True)
        self.assertIs(true_date(200, 2, 29), False)
        self.assertIs(true_date(400, 2, 29), True)
        self.assertIs(true_date(800, 2, 29), True)
        self.assertIs(true_date(2000, 2, 29), True)
        self.assertIs(true_date(2000, 2, 29), True)
        self.assertIs(true_date(2024, 2, 29), True)
        # leap year days - NOT
        self.assertIs(true_date(100, 2, 29), False)
        self.assertIs(true_date(1000, 2, 29), False)
        self.assertIs(true_date(3000, 2, 29), False)
        # bonkers dates
        self.assertIs(true_date(2022, 9, 31), False)
        self.assertIs(true_date(2022, 13, 1), False)
        self.assertIs(true_date(2024, 1, 32), False)
        self.assertIs(true_date(1, 1, 1111), False)


if __name__ == '__main__':
    unittest.main()
