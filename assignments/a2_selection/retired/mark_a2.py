# test a2 scripts for correctness

# needs PyTest library

from a2_answers import *


def test_signum():
    assert signum(11) == 1
    assert signum(0.000702) == 1
    assert signum(0) == 0
    assert signum(-0) == 0
    assert signum(-1 / 2) == -1
    assert signum(-11) == -1


def test_longest():
    assert longest('', '') == 'same'
    assert longest('short', 'longer') == 'longer'
    assert longest('shorter', 'longer') == 'shorter'
    assert longest('orange', 'damson') == 'same'


def test_max_2():
    assert max_2(0, 0) == 0
    assert max_2(1, 1) == 1
    assert max_2(-1, -1) == -1
    assert max_2(1, 2) == 2
    assert max_2(2, 1) == 2
    assert max_2(2, 2) == 2
    assert max_2(3, 3) == 3
    assert max_2(3, 2) == 3
    assert max_2(2, 3) == 3
    assert max_2('a', 'x', ) == 'x'
    assert max_2('abra', 'cad') == 'cad'


def test_max_3():
    assert max_3(0, 0, 0) == 0
    assert max_3(1, 1, 1) == 1
    assert max_3(3, 3, 3) == 3
    assert max_3(-0, -0, -0) == 0
    assert max_3(-1, -1, -1) == -1
    assert max_3(-3, -3, -3) == -3
    assert max_3(3, 3, 2) == 3
    assert max_3(3, 2, 3) == 3
    assert max_3(2, 3, 3) == 3
    assert max_3(1, 2, 3) == 3
    assert max_3(2, 3, 1) == 3
    assert max_3(1, 3, 2) == 3
    assert max_3(0, 2, 3) == 3
    assert max_3(1, 0, 3) == 3
    assert max_3(1, 2, 0) == 2
    assert max_3('a', 'x', 'c') == 'x'
    assert max_3('abra', 'cad', 'abra') == 'cad'


def test_middle_3():
    """In theory should also test for negative numbers - but not now"""
    assert middle_3(0, 0, 0) == 0
    assert middle_3(1, 1, 1) == 1
    assert middle_3(3, 3, 3) == 3
    assert middle_3(3, 3, 2) == 3
    assert middle_3(3, 2, 3) == 3
    assert middle_3(2, 3, 3) == 3
    assert middle_3(1, 2, 3) == 2
    assert middle_3(2, 3, 1) == 2
    assert middle_3(1, 3, 2) == 2
    assert middle_3('a', 'x', 'c') == 'c'
    assert middle_3('abra', 'cad', 'abra') == 'abra'


def test_isa_triangle():
    # equilateral triangles
    assert isa_triangle(1, 1, 1) == 3
    assert isa_triangle(55, 55, 55) == 3
    # isosceles triangles
    assert isa_triangle(2, 2, 1) == 2
    assert isa_triangle(2, 1, 2) == 2
    assert isa_triangle(1, 2, 2) == 2
    # scalene triangles
    assert isa_triangle(3, 4, 5) == 1
    # impossible triangles
    assert isa_triangle(2, 17, 2) == 0
    # assert isa_triangle(0, 0, 0) == 0
    # assert isa_triangle(1, 2, 3) == 0


def test_fizzbuzz():
    assert fizzbuzz(1).lower() == '1'
    assert fizzbuzz(5).lower() == 'buzz'
    assert fizzbuzz(33).lower() == 'fizz'
    assert fizzbuzz(45).lower() == 'fizzbuzz'
    assert fizzbuzz(13).lower() == '13'


def test_grade():
    # should test for decimal scores
    assert grade(1001) == 'A'
    assert grade(101) == 'A'
    assert grade(81) == 'A'
    assert grade(80) == 'A'
    assert grade(79) == 'B'
    assert grade(71) == 'B'
    assert grade(70) == 'B'
    assert grade(69) == 'C'
    assert grade(61) == 'C'
    assert grade(60) == 'C'
    assert grade(59) == 'D'
    assert grade(51) == 'D'
    assert grade(50) == 'D'
    assert grade(49) == 'E'
    assert grade(41) == 'E'
    assert grade(40) == 'E'
    assert grade(39) == 'F'
    assert grade(1) == 'F'
    assert grade(00) == 'F'
    assert grade(-1) == 'F'


def test_isa_leap_year():
    assert isa_leap_year(1) == False
    assert isa_leap_year(4) == True
    assert isa_leap_year(6) == False
    assert isa_leap_year(100) == False
    assert isa_leap_year(1000) == False
    assert isa_leap_year(1200) == True
    assert isa_leap_year(1900) == False
    assert isa_leap_year(2000) == True
    assert isa_leap_year(2020) == True
    assert isa_leap_year(2022) == False
    assert isa_leap_year(18766) == False
    assert isa_leap_year(18768) == True


def test_true_date():
    # assert true_date(1, 0, 1) == False
    assert true_date(1, 1, 1) == True
    assert true_date(1, 2, 1) == True
    assert true_date(1, 3, 1) == True
    assert true_date(1, 4, 1) == True
    assert true_date(1, 5, 1) == True
    assert true_date(1, 6, 1) == True
    assert true_date(1, 7, 1) == True
    assert true_date(1, 8, 1) == True
    assert true_date(1, 9, 1) == True
    assert true_date(1, 10, 1) == True
    assert true_date(1, 11, 1) == True
    assert true_date(1, 12, 1) == True
    assert true_date(1, 13, 1) == False

    assert true_date(2022, 10, 14) == True
    assert true_date(2022, 13, 14) == False
    assert true_date(2022, 10, 31) == True
    assert true_date(2022, 9, 31) == False
    assert true_date(12022, 2, 29) == False
