# LIN7077 Test 5th Assignment

from assignment_student_submissions.a4_submissions.attempt_20221207.a5_200411868_ import *

# Define some HELPER functions and default values for testing #################################################
default_file_name = 'test_data.txt'


def str_to_file(a_str, f_name=default_file_name):
    """Create a file from a string and return the file name."""
    with open(f_name, mode='wt', encoding='utf-8') as tf:  # open the file
        tf.write(a_str)  # write content
    # file automatically closed at end of indentation block
    return f_name  # return the name of the file


def file_to_str(f_name=default_file_name):
    """Read the file and return its contents as a string."""
    with open(f_name, mode='rt', encoding='utf-8') as tf:  # open the file
        f_content = tf.read()  # read entire contents
        # return contents as a string
        return f_content


##############################################################################
# Now start testing
##############################################################################

def test_thermostat():
    # given examples
    assert thermostat(21) == 'stet' or thermostat(21) == 'stat'
    assert thermostat(16) == 'heat on' or thermostat(16) == 'on'
    assert thermostat(34) == 'heat off' or thermostat(34) == 'off'
    assert thermostat(19) == 'stet' or thermostat(19) == 'stat'
    assert thermostat(24) == 'stet' or thermostat(24) == 'stat'
    # a few extreme values
    assert thermostat(-999) == 'heat on' or thermostat(-999) == 'on'
    assert thermostat((19 + 24) / 2) == 'stet' or thermostat((19 + 24) / 2) == 'stat'
    assert thermostat(+999) == 'heat off' or thermostat(+999) == 'off'


def test_score_2():
    assert score_2(1, 5) == 6
    assert score_2(5, 1) == 6
    assert score_2(3, 4) == 14
    assert score_2(5, 2) == 14
    assert score_2(2, 2) == 6
    assert score_2(6, 6) == 24


def test_score_4():
    assert score_4(1, 5, 6, 6) == 7
    assert score_4(3, 2, 3, 3) == 2
    assert score_4(2, 6, 1, 5) == 14
    assert score_4(1, 1, 2, 6) == 7
    assert score_4(1, 2, 3, 4) == 1
    assert score_4(3, 3, 3, 4) == 7
    assert score_4(3, 3, 4, 4) == 21
    assert score_4(4, 3, 3, 4) == 21


def test_get_all_chars():
    # no examples given so just try these
    assert get_all_chars(str_to_file('')) == set()
    assert get_all_chars(str_to_file('abracadabra')) == set('abcdr')
    assert get_all_chars(str_to_file('abcdefghijklABCDEFGHIJKL')) == set('abcdefghijklABCDEFGHIJKL')
    assert get_all_chars(str_to_file('The quick brown fox jumped over the lazy dog')) == \
           set('The quick brown fx jmped v t lazy dg')


def test_count_chars():
    # examples
    assert count_chars(str_to_file('')) == 0
    assert count_chars(str_to_file('abc 123')) == 7
    assert count_chars(str_to_file('-abc-123-')) == 9
    # and a few more
    assert count_chars(str_to_file('\n')) == 1
    assert count_chars(str_to_file('7777777 7777777 7777777 7777777')) == 31
    assert count_chars(str_to_file('~abc+cab~')) == 9
    assert count_chars(str_to_file('\t\n\n')) == 3


def test_count_and():
    # test examples
    assert count_and(str_to_file('')) == (0, 0, 0)
    assert count_and(str_to_file('and and and, ')) == (3, 1, 1)
    assert count_and(str_to_file('Andover and shandy')) == (3, 1, 0)
    # and more

    assert count_and(str_to_file(' a n d ')) == (0, 0, 0)
    assert count_and(str_to_file('and and and')) == (3, 1, 0)
    assert count_and(str_to_file(' and and and ')) == (3, 2, 0)
    assert count_and(str_to_file(' and  and  and ')) == (3, 3, 0)
    assert count_and(str_to_file('Andover and, and shandy')) == (4, 1, 1)


def test_count_words():
    # examples
    assert count_words(str_to_file('')) == 0
    assert count_words(str_to_file('abc 123')) == 2
    assert count_words(str_to_file('abc     123\n \t    xyz')) == 3
    # more tests
    assert count_words(str_to_file('Launching pytest with arguments')) == 4
    assert count_words(str_to_file('a')) == 1
    assert count_words(str_to_file('aaa')) == 1
    assert count_words(str_to_file('\n\tabc')) == 1
    assert count_words(str_to_file('abc\n\t')) == 1
    assert count_words(str_to_file('\n\tabc\n\t')) == 1
    assert count_words(str_to_file('abc\nabc')) == 2
    assert count_words(str_to_file('abc\tabc')) == 2


def test_char_frequency():
    assert char_frequency(str_to_file('')) == {}
    assert char_frequency(str_to_file('abc')) == {'a': 1, 'b': 1, 'c': 1}
    assert char_frequency(str_to_file('abc ab a d')) == {'a': 3, 'b': 2, 'c': 1, 'd': 1, ' ': 3}
    assert char_frequency(str_to_file('abc     123    \n\t\n    23b')) == {
        'a': 1, 'b': 2, 'c': 1, ' ': 13, '1': 1, '2': 2, '3': 2, '\n': 2, '\t': 1}


def test_word_frequency():
    assert word_frequency(str_to_file('')) == {}  # empty dictionary
    assert word_frequency(str_to_file('abc 123')) == {'abc': 1, '123': 1}
    assert word_frequency(str_to_file('abc 123\n \t xyz')) == {'abc': 1, '123': 1, 'xyz': 1}
    assert word_frequency(str_to_file('        ')) == {}
    assert word_frequency(str_to_file('abc     123    \n\t    xyz')) == {'abc': 1, '123': 1, 'xyz': 1}
    assert word_frequency(str_to_file('abc     123    \n\t  123  abc xyz')) == {'abc': 2, '123': 2, 'xyz': 1}


def test_write_Q():
    write_Q(default_file_name, 0)
    assert file_to_str() == ''

    write_Q(default_file_name, 1)
    assert file_to_str() == '1 ?\n'

    write_Q(default_file_name, 2)
    assert file_to_str() == '1 ?\n2 ??\n'

    write_Q(default_file_name, 5)
    assert file_to_str() == '1 ?\n2 ??\n3 ???\n4 ????\n5 ?????\n'


def test_write_ints():
    write_ints(default_file_name, 0)
    assert file_to_str() == ''

    write_ints(default_file_name, 1)
    assert (file_to_str() == '1\n' or file_to_str() == '1')

    write_ints(default_file_name, 2)
    assert (file_to_str() == '1\n2 4\n' or file_to_str() == '1\n2 4')

    write_ints(default_file_name, 5)
    # assert file_to_str() == '1\n2 4\n3 6 9\n4 8 12 16\n5 10 15 20 25\n'
    expected = '1\n2 4\n3 6 9\n4 8 12 16\n5 10 15 20 25\n'
    actual = file_to_str()
    assert (actual==expected or actual==expected[:-1])

def test_runup():
    str_to_file('')
    assert runup(default_file_name) == (0, 0)

    str_to_file('z')
    assert runup(default_file_name) == (0, 1)

    str_to_file('ababcb')
    assert runup(default_file_name) == (2, 3)

    str_to_file('testresult')
    assert runup(default_file_name) == (1, 3)

    str_to_file('ababcccdab')
    assert runup(default_file_name) == (2, 6)

    str_to_file('abracadabra')
    assert runup(default_file_name) == (0, 3)

    str_to_file('spoonfeedbackwardsisdeefnoops')
    assert runup(default_file_name) == (20, 9)
