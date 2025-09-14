"""LIN7077 Test script for Assignment 1

1. Place this script in the same folder as your python script for assignment 1
2. Replace 'a1_answers' with the name of your answer script.
3. Run this python program script from IDLE
"""

from assignment_student_submissions.a1_submissions.marked.a1_240408877_v1 import *
# import the following libraries from the Python standard library
import unittest
import types
import sys

# check this is Python 3
if not sys.version[0] == '3':
    print("Must be version 3")
    exit(-1)  # exit with error code

# get a list of everything in the local python environment
# this will include all the functions implemented in the imported script
implemented = dir()


class TestStringMethods(unittest.TestCase):

    @unittest.skipIf('all_ops_part1' not in implemented,
                     'all_ops_part1() not implemented')
    def test_all_ops_part1(self):  # + - * / // %
        self.assertIsInstance(all_ops_part1, types.FunctionType)
        self.assertEqual(all_ops_part1(4, 2), (6, 2, 8, 2.0, 2, 0),
                         'an error message for this test can be placed here')
        self.assertEqual(all_ops_part1(5, 4), (9, 1, 20, 1.25, 1, 1))
        self.assertEqual(all_ops_part1(9, 3), (12, 6, 27, 3.0, 3, 0))
        self.assertEqual(all_ops_part1(-4, -2), (-6, -2, 8, 2.0, 2, 0))

    @unittest.skipIf('all_ops_part2' not in implemented,
                     'all_ops_part2() not implemented')
    def test_all_ops_part2(self):  # < <= == != >=
        self.assertIsInstance(all_ops_part2, types.FunctionType)
        self.assertEqual(all_ops_part2(7, 6),
                         (False, False, False, True, True, True))
        self.assertEqual(all_ops_part2(6, 7),
                         (True, True, False, True, False, False))
        self.assertEqual(all_ops_part2(0, 0),
                         (False, True, True, False, True, False))
        self.assertEqual(all_ops_part2(4, 4),
                         (False, True, True, False, True, False))
        self.assertEqual(all_ops_part2(-4, -2),
                         (True, True, False, True, False, False))

    @unittest.skipIf('magic_number' not in implemented,
                     'magic_number() not implemented')
    def test_magic_number(self):
        self.assertIsInstance(magic_number, types.FunctionType)
        self.assertTrue(magic_number(7))
        self.assertTrue(magic_number(11171171))
        self.assertTrue(magic_number(-7))
        self.assertTrue(magic_number(0.123456789))
        self.assertFalse(magic_number(0))
        self.assertFalse(magic_number(0123.456))
        self.assertTrue(magic_number(3 + 4))
        self.assertFalse(magic_number(7 * 7))

    @unittest.skipIf('hms_to_s' not in implemented,
                     'hms_to_s() not implemented')
    def test_hms_to_s(self):
        self.assertIsInstance(hms_to_s, types.FunctionType)
        self.assertEqual(hms_to_s(0, 0, 0), 0)
        self.assertEqual(hms_to_s(0, 0, 1), 1)
        self.assertEqual(hms_to_s(0, 2, 0), 120)
        self.assertEqual(hms_to_s(3, 0, 0), 10800)
        self.assertEqual(hms_to_s(3, 2, 1), 10921)
        self.assertEqual(hms_to_s(1, 1, 1), 3661)
        self.assertEqual(hms_to_s(1, 2, 3), 3723)
        self.assertEqual(hms_to_s(100, 100, 100), 366100)

    @unittest.skipIf('s_to_hms' not in implemented,
                     's_to_hms() not implemented')
    def test_s_to_hms(self):
        self.assertIsInstance(s_to_hms, types.FunctionType)
        self.assertEqual(s_to_hms(0), (0, 0, 0))
        self.assertEqual(s_to_hms(1), (0, 0, 1))
        self.assertEqual(s_to_hms(59), (0, 0, 59))
        self.assertEqual(s_to_hms(60), (0, 1, 0))
        self.assertEqual(s_to_hms(601), (0, 10, 1))
        self.assertEqual(s_to_hms(3661), (1, 1, 1))
        self.assertEqual(s_to_hms(10921), (3, 2, 1))
        self.assertEqual(s_to_hms(366100), (101, 41, 40))

    @unittest.skipIf('add_hms' not in implemented,
                     'add_hms() not implemented')
    def test_add_hms(self):
        self.assertIsInstance(add_hms, types.FunctionType)
        self.assertEqual(add_hms(0, 0, 0, 0, 0, 0), (0, 0, 0))
        self.assertEqual(add_hms(1, 1, 1, 0, 0, 0), (1, 1, 1))
        self.assertEqual(add_hms(0, 0, 0, 1, 1, 1), (1, 1, 1))
        self.assertEqual(add_hms(1, 1, 1, 2, 2, 2), (3, 3, 3))
        self.assertEqual(add_hms(0, 0, 50, 0, 0, 40), (0, 1, 30))
        self.assertEqual(add_hms(3, 2, 59, 4, 9, 2), (7, 12, 1))
        self.assertEqual(add_hms(25, 50, 50, 145, 40, 20), (171, 31, 10))
        self.assertEqual(add_hms(101, 101, 101, 99, 99, 99), (203, 23, 20))
        self.assertEqual(add_hms(300, 400, 500, 600, 700, 800), (918, 41, 40))

    @unittest.skipIf('add_old_uk' not in implemented,
                     'add_old_uk() not implemented')
    def test_add_old_uk(self):
        self.assertIsInstance(add_old_uk, types.FunctionType)
        self.assertEqual(add_old_uk(0, 0, 0, 0, 0, 0), (0, 0, 0))
        self.assertEqual(add_old_uk(0, 0, 1, 0, 0, 0), (0, 0, 1))
        self.assertEqual(add_old_uk(0, 1, 0, 0, 0, 0), (0, 1, 0))
        self.assertEqual(add_old_uk(1, 0, 0, 0, 0, 0), (1, 0, 0))
        self.assertEqual(add_old_uk(0, 0, 11, 0, 0, 7), (0, 1, 6))
        self.assertEqual(add_old_uk(1, 19, 11, 0, 0, 1), (2, 0, 0))
        self.assertEqual(add_old_uk(4, 19, 11, 5, 10, 10), (10, 10, 9))
        self.assertEqual(add_old_uk(0, 0, 10001, 0, 0, 1001), (45, 16, 10))
        self.assertEqual(add_old_uk(0, 19, 11, 1, 10, 6), (2, 10, 5))

    @unittest.skipIf('is_palindrome' not in implemented,
                     'is_palindrome() not implemented')
    def test_is_palindrome(self):
        self.assertIsInstance(is_palindrome, types.FunctionType)
        self.assertTrue(is_palindrome('Kayak'))
        self.assertTrue(is_palindrome('Akasaka'))
        self.assertTrue(is_palindrome('Madam'))
        self.assertTrue(is_palindrome('Racecar'))
        self.assertTrue(is_palindrome(
            'saippuakivikauppias'))  # swedish for soapstone seller ??
        self.assertTrue(is_palindrome('Now sir a war is won'))
        self.assertTrue(is_palindrome('never odd or even'))
        self.assertTrue(is_palindrome('  NeV  ER Od D or EveN  '))
        self.assertFalse(is_palindrome('backwards'))

    @unittest.skipIf('is_anagram' not in implemented,
                     'is_anagram() not implemented')
    def test_is_anagram(self):
        self.assertIsInstance(is_anagram, types.FunctionType)
        self.assertTrue(is_anagram('', ''))
        self.assertTrue(is_anagram(' ', ' '))
        self.assertTrue(is_anagram('   ', '                 '))
        self.assertTrue(is_anagram('A', 'a'))
        self.assertTrue(is_anagram('2', str(2)))
        self.assertTrue(is_anagram('-', '-'))
        self.assertTrue(is_anagram('abc', 'abc'))
        self.assertTrue(is_anagram(' abc ', ' a  b  c '))
        self.assertTrue(is_anagram(' a  b   c    ', '   a   b  c '))
        self.assertTrue(is_anagram('Debit card', 'Bad credit'))
        self.assertTrue(is_anagram('Sugared ambulances', 'Cumberland Sausage'))
        self.assertTrue(is_anagram('A legal title', 'Tagliatelle'))
        self.assertFalse(is_anagram('this phrase', 'that phrase'))

    @unittest.skipIf('lucky_fun' not in implemented,
                     'lucky_fun() not implemented')
    def test_lucky_fun(self):
        self.assertIsInstance(lucky_fun, types.FunctionType)  # added 8/Oct/23
        lucky_1 = lucky_fun(7)  # assign the returned function lucky_1
        self.assertIsInstance(lucky_1, types.FunctionType)  # added 5/Oct/23
        self.assertTrue(lucky_1(11711))  # returns True
        self.assertFalse(lucky_1(11511))  # returns False
        self.assertTrue(
            lucky_1('James Bond 007, licenced to kill'))  # returns True
        self.assertFalse(lucky_1(5 * 10 - 1))  # returns False as 5*10-1 = 49
        self.assertFalse(lucky_1(7 * 7))  # returns False as 7*7 is 49

        lucky_2 = lucky_fun(
            'ms')  # returns a function and assigns it to lucky_2
        self.assertIsInstance(lucky_2, types.FunctionType)  # added 5/Oct/23
        self.assertFalse(lucky_2(
            'spam'))  # returns False as 'ms' is not in the string 'spam'
        self.assertTrue(lucky_2(
            'spam' * 5))  # returns True as 'ms' is in 'spamspamspamspamspam'


if __name__ == '__main__':
    unittest.main()
