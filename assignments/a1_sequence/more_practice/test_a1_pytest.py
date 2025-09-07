# from StudentAssignmentSubmissions.a1_submissions.a2_180080960 import *

from assignments.a1_sequence.a1_answers import *
import types


def test_all_ops_pt1():
    assert isinstance(all_ops_part1, types.FunctionType)
    assert all_ops_part1(4, 2) == (6, 2, 8, 2.0, 2, 0)
    assert isinstance(all_ops_part1(4, 2)[3], float)
    assert all_ops_part1(5, 4) == (9, 1, 20, 1.25, 1, 1)
    assert all_ops_part1(9, 3) == (12, 6, 27, 3.0, 3, 0)


def test_all_ops_pt2():
    assert isinstance(all_ops_part2, types.FunctionType)
    assert all_ops_part2(1, 2) == (True, True, False, True, False, False)
    assert all_ops_part2(2, 1) == (False, False, False, True, True, True)
    assert all_ops_part2(0, 0) == (False, True, True, False, True, False)
    assert all_ops_part2(1, 1) == (False, True, True, False, True, False)


def test_magic_number():
    assert isinstance(magic_number, types.FunctionType)
    assert magic_number(7)
    assert magic_number(11171171)
    assert magic_number(-7)
    assert magic_number(0.123456789)
    assert not magic_number(0)
    assert not magic_number(0123.456)


def test_hms_to_s():
    assert isinstance(hms_to_s, types.FunctionType)
    assert hms_to_s(0, 0, 0) == 0
    assert hms_to_s(0, 0, 1) == 1
    assert hms_to_s(0, 1, 0) == 60
    assert hms_to_s(1, 0, 0) == 3600
    assert hms_to_s(1, 1, 1) == 3661
    assert hms_to_s(1, 2, 3) == 3723
    assert hms_to_s(100, 100, 100) == 366100


def test_s_to_hms():
    assert isinstance(s_to_hms, types.FunctionType)
    assert s_to_hms(0) == (0, 0, 0)
    assert s_to_hms(1) == (0, 0, 1)
    assert s_to_hms(60) == (0, 1, 0)
    assert s_to_hms(3600) == (1, 0, 0)
    assert s_to_hms(10921) == (3, 2, 1)
    assert s_to_hms(366100) == (101, 41, 40)


def test_add_hms():
    assert isinstance(add_hms, types.FunctionType)
    assert add_hms(0, 0, 0, 0, 0, 0) == (0, 0, 0)
    assert add_hms(1, 1, 1, 0, 0, 0) == (1, 1, 1)
    assert add_hms(0, 0, 0, 1, 1, 1) == (1, 1, 1)
    assert add_hms(1, 1, 1, 1, 1, 1) == (2, 2, 2)
    assert add_hms(0, 0, 50, 0, 0, 40) == (0, 1, 30)
    assert add_hms(25, 50, 50, 145, 40, 20) == (171, 31, 10)


def test_add_old_uk():
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


# def test_is_palindrome():
#    assert isinstance(is_palindrome('Kayak'), bool)
#    assert is_palindrome('Kayak')
#    assert is_palindrome('Akasaka')
#    assert is_palindrome('never odd or even')
#    assert is_palindrome('NeVER OdD or EveN')
#    assert not is_palindrome('backwards')


def test_is_palindrome():
   assert isinstance(is_palindrome('Kayak'), bool)
   assert is_palindrome('Kayak')
   assert is_palindrome('Akasaka')
   assert is_palindrome('never odd or even')
   assert is_palindrome('NeVER OdD or EveN')
   assert not is_palindrome('backwards')


def test_is_anagram():
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

# def test_lucky_fun():
#     assert isinstance(lucky_fun, types.FunctionType)
#     a = lucky_fun(7)
#     assert isinstance(a, types.FunctionType)
#     assert isinstance(a(11711), bool)
#     assert a(11711)
#     assert not a(11511)
#     assert not a(0)
#     b = lucky_fun(11)
#     assert isinstance(b, types.FunctionType)
#     assert isinstance(a(11711), bool)
#     assert b(11711)
#     assert not b(15151)
#     assert b(1.102)
#     assert not b(1010)
#     assert b(11711)
#     assert b(11711)
