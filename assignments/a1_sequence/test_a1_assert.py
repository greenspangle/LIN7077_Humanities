"""
Test that your functions work correctly

Place this in the same folder as your python script and replace 'a1_answers' in the import statement with the name of your answer script'
If you get any errors, check that you have not changed the function signatures.
If you get any runtime errors, check that you have not changed any of the function bodies.
"""

from a1_answers import *
import types

# get a list of all the objects in memory, including functions
object_space = dir()

assert (all_ops_part1(4, 2) == (6, 2, 8, 2.0, 2, 0))
assert isinstance(all_ops_part1, types.FunctionType)

assert isinstance(all_ops_part1(4, 2)[3], float)
assert all_ops_part1(5, 4) == (9, 1, 20, 1.25, 1, 1)
assert all_ops_part1(9, 3) == (12, 6, 27, 3.0, 3, 0)


def test_upper(self):
    self.assertEqual('foo'.upper(), 'FOO')


def test_isupper(self):
    self.assertTrue('FOO'.isupper())
    self.assertFalse('Foo'.isupper())


def test_split(self):
    s = 'hello world'
    self.assertEqual(s.split(), ['hello', 'world'])
    # check that s.split fails when the separator is not a string
    with self.assertRaises(TypeError):
        s.split(2)


if __name__ == '__main__':
    unittest.main()

# same again for all other functions
if 'all_ops_pt2' in object_space:
    assert isinstance(all_ops_part2, types.FunctionType)
    assert all_ops_part2(1, 2) ==      (True, True, False, True, False, False)
    assert all_ops_part2(2, 1) == (False, False, False, True, True, True)
    assert all_ops_part2(0, 0) == (False, True, True, False, True, False)
    assert all_ops_part2(1, 1) == (False, True, True, False, True, False)

if 'magic_number' in object_space:
    assert isinstance(magic_number, types.FunctionType)
    assert magic_number(7)
    assert magic_number(11171171)
    assert magic_number(-7)
    assert magic_number(0.123456789)
    assert not magic_number(0)
    assert not magic_number(0123.456)

if 'hms_to_s' in object_space:
    assert isinstance(hms_to_s, types.FunctionType)
    assert hms_to_s(0, 0, 0) == 0
    assert hms_to_s(0, 0, 1) == 1
    assert hms_to_s(0, 1, 0) == 60
    assert hms_to_s(1, 0, 0) == 3600
    assert hms_to_s(1, 1, 1) == 3661
    assert hms_to_s(1, 2, 3) == 3723
    assert hms_to_s(100, 100, 100) == 366100

if 's_to_hms' in object_space:
    assert isinstance(s_to_hms, types.FunctionType)
    assert s_to_hms(0) == (0, 0, 0)
    assert s_to_hms(1) == (0, 0, 1)
    assert s_to_hms(60) == (0, 1, 0)
    assert s_to_hms(3600) == (1, 0, 0)
    assert s_to_hms(10921) == (3, 2, 1)
    assert s_to_hms(366100) == (101, 41, 40)

if 'add_hms' in object_space:
    assert isinstance(add_hms, types.FunctionType)
    assert add_hms(0, 0, 0, 0, 0, 0) == (0, 0, 0)
    assert add_hms(1, 1, 1, 0, 0, 0) == (1, 1, 1)
    assert add_hms(0, 0, 0, 1, 1, 1) == (1, 1, 1)
    assert add_hms(1, 1, 1, 1, 1, 1) == (2, 2, 2)
    assert add_hms(0, 0, 50, 0, 0, 40) == (0, 1, 30)
    assert add_hms(25, 50, 50, 145, 40, 20) == (171, 31, 10)

if 'add_old_uk' in object_space:
    assert isinstance(add_old_uk, types.FunctionType)
    assert add_old_uk(0, 0, 0, 0, 0, 0) == (0, 0, 0)
    assert add_old_uk(0, 0, 1, 0, 0, 0) == (0, 0, 1)
    assert add_old_uk(0, 1, 0, 0, 0, 0) == (0, 1, 0)
    assert add_old_uk(1, 0, 0, 0, 0, 0) == (1, 0, 0)
    assert add_old_uk(100, 0, 0, 200, 0, 0) == (300, 0, 0)
    assert add_old_uk(0, 100, 0, 0, 200, 0) == (15, 0, 0)
    assert add_old_uk(0, 0, 100, 0, 0, 200) == (1, 5, 0)
    assert add_old_uk(0, 0, 11, 0, 0, 7) == (0, 1, 6)
    assert add_old_uk(0, 19, 11, 1, 10, 6) == (2, 10, 5)

if 'is_palindrome' in object_space:
    assert isinstance(is_palindrome('Kayak'), bool)
    assert is_palindrome('Kayak')
    assert is_palindrome('Akasaka')
    assert is_palindrome('never odd or even')
    assert is_palindrome('NeVER OdD or EveN')
    assert not is_palindrome('backwards')

if 'is_anagram' in object_space:
    assert isinstance(is_anagram, types.FunctionType)
    assert isinstance(is_anagram('Debit card', 'Bad credit'), bool)
    assert is_anagram('Debit card', 'Bad credit')
    assert is_anagram('Sugared ambulances', 'Cumberland Sausage')
    assert is_anagram('A legal title', 'Tagliatelle')
    assert not is_anagram('this phrase', 'that phrase')
    assert is_anagram('', '')
    assert is_anagram('A', 'a')
    assert is_anagram('2', str(2))
    assert is_anagram('-', '-')
    assert not is_anagram('a', 'b')
