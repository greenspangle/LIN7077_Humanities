
from a040answers import *

def test_robberlingo():
    assert robberlingo('') == ''
    assert robberlingo('this is fun') == 'tothohisos isos fofunon'
    assert robberlingo('here is some robberlingo') == \
           'hoherore isos sosomome rorobobboberorlolinongogo'


def test_pangram():
    assert pangram('the quick brown fox jumps over the lazy dog') == True
    assert pangram('The quick brown Fox jumps over the lazy Dog') == True  # ignore capitalisation
    assert pangram('the quick brown fox, jumps over the lazy dog.') == True  # ignore punctuation
    assert pangram('The quick brown Fox jumps over the lazy Dog!') == True  # ignore both caps and punctuation
    assert pangram('the quick brown fox jumped over the lazy dog') == False


def test_merge2():
    assert merge2('', '') == ''
    assert merge2('a', 'x') == 'ax'
    assert merge2('abc', 'def') == 'adbecf'


def test_merge3():
    assert merge3('', '', '') == ''
    assert merge3('a', 'b', 'c') == 'abc'
    assert merge3('abc', 'def', 'ghj') == 'adgbehcfj'


def test_letter_count():
    assert letter_count('') == {}
    assert letter_count('a') == {'a': 1}
    assert letter_count('aaa') == {'a': 3}
    assert letter_count('abbabab') == {'a': 3, 'b': 4}
    assert letter_count('abracadabra') == {
        'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

