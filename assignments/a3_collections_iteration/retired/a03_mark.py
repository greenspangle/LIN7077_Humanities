# from StudentAssignmentSubmissions.a1_submissions.a2_180080960 import *

from assignment_student_submissions.a3_submissions.attempt_20221027.a4_200059095_PMcG import *
# from assignments.a03_collections_iteration.a030_answers import *
import types


def test_count_a():
    assert isinstance(count_a, types.FunctionType)
    assert count_a('1') == 0
    assert count_a('a') == 1
    assert count_a('abracadabra') == 5


def test_count_digits():
    assert isinstance(count_digits, types.FunctionType)
    assert count_digits('1') == 1
    assert count_digits('a') == 0
    assert count_digits('a1b2r3a123cadabra') == 6


def test_count_vowels():
    assert isinstance(count_vowels, types.FunctionType)
    assert count_vowels('1') == 0
    assert count_vowels('a') == 1
    assert count_vowels('aaxee') == 4
    assert count_vowels('rhythm') == 0
    assert count_vowels('abracadabra') == 5
    assert count_vowels('ABRACADABRA') == 5
    assert count_vowels('aebrecodeibra') == 7


def test_count_consonants():
    assert isinstance(count_consonants, types.FunctionType)
    assert count_consonants('J') == 1
    assert count_consonants('k') == 1
    assert count_consonants('rhythm') == 6
    assert count_consonants('aebrecodeibra') == 6
    assert count_consonants('ABRACADABRA') == 6


def test_contains_substr():
    assert isinstance(contains_substr, types.FunctionType)
    assert contains_substr('1', '1') == True
    assert contains_substr('1', '9') == False
    assert contains_substr('Hocus-Pocus', 's-P') == True
    assert contains_substr('Hocus-Pocus', 's-p') == False
    assert contains_substr('abracadabra', 'abraxas') == False
    assert contains_substr('a', '') == True


def test_count_substr():
    assert isinstance(count_substr, types.FunctionType)
    assert count_substr('a', 'a') == 1
    assert count_substr('aaa', 'a') == 3
    assert count_substr('Hocus-Pocus', 'ocu') == 2
    assert count_substr('Hocus-Pocus', 'us') == 2
    assert count_substr('Hocus-Pocus', 'b') == 0


def test_get_sequence_list():
    assert isinstance(get_sequence_list, types.FunctionType)
    assert get_sequence_list(1) == [1]
    assert get_sequence_list(2) == [1, 2]
    assert get_sequence_list(5) == [1, 2, 3, 4, 5]
    assert get_sequence_list(11) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def test_get_sequence_as_set():
    assert isinstance(get_sequence_as_set, types.FunctionType)
    assert get_sequence_as_set(1) == {1}
    assert get_sequence_as_set(2) == {1, 2}
    assert get_sequence_as_set(5) == {1, 2, 3, 4, 5}
    assert get_sequence_as_set(11) == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}


def test_get_sequence_str():
    assert isinstance(get_sequence_str, types.FunctionType)
    assert get_sequence_str(1) == '1'
    assert get_sequence_str(2) == '1 2'
    assert get_sequence_str(5) == '1 2 3 4 5'


def test_times2_dict():
    assert isinstance(times2_dict, types.FunctionType)
    assert times2_dict(1) == {1: 2}
    assert times2_dict(2) == {1: 2, 2: 4}
    assert times2_dict(5) == {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}


def test_fizzbuzz_dict():
    assert isinstance(fizzbuzz_dict, types.FunctionType)
    assert fizzbuzz_dict(1) == {1: '1'}
    assert fizzbuzz_dict(2) == {1: '1', 2: '2'}
    assert fizzbuzz_dict(3) == {1: '1', 2: '2', 3: 'Fizz'}
    assert fizzbuzz_dict(5) == {1: '1', 2: '2', 3: 'Fizz', 4: '4', 5: 'Buzz'}


def test_robber_lingo():
    assert isinstance(robber_lingo, types.FunctionType)
    assert robber_lingo("this is fun") == "tothohisos isos fofunon"


def test_isa_pangram():
    assert isa_pangram('the quick brown fox jumps over the lazy dog') == True
    assert isa_pangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG') == True
    assert isa_pangram('the quick brown fox ?<!>? jumps over the lazy dog') == True
    assert isa_pangram('the quick brown fox jumped over the lazy dog') == False


def test_merge2():
    assert merge2('', '') == ''
    assert merge2('a', 'x') == 'ax'
    assert merge2('ab', 'xy') == 'axby'
    assert merge2('abc', 'def') == 'adbecf'


def test_merge3():
    assert merge3('', '', '') == ''
    assert merge3('a', 'b', 'c') == 'abc'
    assert merge3('ab', 'xy', 'wz') == 'axwbyz'
    assert merge3('abc', 'def', 'ghj') == 'adgbehcfj'


def test_merge3_short():
    assert merge3_short('', '', '') == ''
    assert merge3_short('a', 'b', 'c') == 'abc'
    assert merge3_short('abc', 'de', 'g') == 'adg'
    assert merge3_short('abc', 'de', 'gh') == 'adgbeh'
    assert merge3_short('abc', 'de', 'ghij') == 'adgbeh'
    assert merge3_short('ghij', 'de', 'abc') == 'gdaheb'
    assert merge3_short('agh', 'bcd', 'ef') == 'abegcf'


def test_merge3_long():
    assert merge3_long('', '', '') == ''
    assert merge3_long('a', 'b', 'c') == 'abc'
    assert merge3_long('abc', 'de', 'g') == 'adgbec'
    assert merge3_long('abc', 'de', 'gh') == 'adgbehc'
    assert merge3_long('abc', 'de', 'ghij') == 'adgbehcij'
    assert merge3_long('ghij', 'de', 'abc') == 'gdahebicj'
    assert merge3_long('de', 'ghij', 'abc') == 'dgaehbicj'


def test_letter_count():
    assert letter_count('') == {}
    assert letter_count('a') == {'a': 1}
    assert letter_count('aaa') == {'a': 3}
    assert letter_count('abbabab') == {'a': 3, 'b': 4}
    assert letter_count('abracadabra') == {'a': 5, 'b': 2, 'c': 1, 'd': 1, 'r': 2}
