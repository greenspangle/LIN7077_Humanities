# LIN6209 Files (#4 assessed)

import string  # module contains various collections of ASCII characters
import csv  # module for precessing comma seperated files

# define some constants for collections of characters
VOWELS_UC = 'AEIOU'
VOWELS_LC = VOWELS_UC.lower()
VOWELS = VOWELS_LC + VOWELS_UC

CONSONANTS_UC = 'BCDFGHJKLMNPQRSTVWXYZ'
CONSONANTS_LC = CONSONANTS_UC.lower()
CONSONANTS = CONSONANTS_LC + CONSONANTS_UC


def temperature_FtoC(temperature):
    """The parameter temperature represents a temperature on the
    Fahrenheit scale. Return the equivalent temperature on the Celsius scale.
    To convert a temperature from Fahrenheit to Centigrade
    first subtract thirty-two from the temperature,
    then divide that result by nine,
    then multiply by five."""
    # apply the formula given in question
    temperature_centigrade = (temperature - 32) / 9 * 5
    return temperature_centigrade


def thermostat(temperature):
    """If the temperature is less that 19 turn the heat on,
    if it's more than 24 turn the heat off,
    and if it's neither, leave the heat setting as it is.
    Return the string `'heat on'`, `'heat off'` or `'stet'` respectively."""
    # the three clauses in this compound if statement include all possible
    # values of temperature therefore one of them must return a value
    if temperature < 19:
        return 'heat on'
    if temperature > 24:
        return 'heat off'
    else:
        return 'stet'


#  from q04 import read_alternate_chars:
def read_alternate_chars(filename):
    """ Open the file `filename` and return two **sets** of characters:
        * set_1 : the set of the first, third, fifth, and so on,
                  characters from the file
        * set_2 : the set of the second, fourth, sixth, and so on,
                  characters from the file """
    # read the file into a string
    with open(filename, 'rt', encoding='utf-8') as f:
        file_string = f.read()
    # slice the string into two sub-strings of alternate characters
    # and add each slice to a set
    set_even = set(file_string[0::2])  # start at [0] and step 2
    set_odd = set(file_string[1::2])  # start at [1] and step 2
    # and return the two sets
    return set_even, set_odd


def write_ints(filename, an_int):
    """The parameters are guaranteed to be a legal filename and an integer
    greater than or equal to zero.
    Create the file and write `an_int` lines to the file.
    The successive lines of the file each start with the `next integer`
    in the ascending sequence from 1 to `an_int`
    followed by the sequence of integer multiples of `next_integer`
    up to and including `next_integer * next_integer`.
    All the integers in the same line are separated by a single space.
    No space is added at the beginning or the end of the line."""
    # open the named file for writing
    with open(filename, mode='wt', encoding='utf-8') as f:
        # the file has been opened for write hence exists and is empty
        # which satisfies the condition when an_int is zero
        # loop through the integers from 1 to an_int to create each line
        for i in range(1, an_int + 1):
            # start each line with the current integer
            line = str(an_int) + ' -'
            # and a loop for every following integer on that line
            for j in range(1, i + 1):
                line = line + ' ' + str(i * j)
            f.write(line + '\n')
    return  # no return value


def read_ints_csv(filename):
    """The file `filename` is guaranteed to be a CSV file  (comma seperated
    variables) with variable length records and integer valued fields.

    Every record should comply with the constraints that:
    * Every record has either zero fields or at least two fields
    * The value in the last field of a record must equal the sum of all the
      preceding fields in that record

    Open the file, read it, and return `True` if it complies with these
    constraints and `False` otherwise."""

    with open(filename) as csvfile:
        # read file as a CSV file
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            len_row = len(row)
            # record cannot have one field
            if len_row == 1:
                return False
            # all the fields are text so cast to integer
            row = list(map(int, row))
            # LAST field must equal sum of all other fields
            if not row[len_row-1] == sum(row[:-1]):
                return False
    # file read and all tests passed!
    return True


def write_random(filename='random_chars.txt',
                 size=6209,
                 alphabet=string.digits):
    """The parameters are:
        * filename: a legal file name with a default value of
          `'random_chars.txt'`
        * size: a positive integer with a default value of `6209`
        * alphabet: a string of characters with a default value of
          `'0123456789'`
    Write `size` random characters from `alphabet` to a file named `filename`.
    """
    import random

    with open(filename, mode='wt', encoding='utf-8') as out_file:
        counter = 0
        while counter < size:
            random_char = random.choice(alphabet)
            out_file.write(random_char)
            counter += 1
        pass
    return  # no return value specified


def is_alphabetical(a_str=''):
    """Do not use the built-in function `sorted()` or `reversed()` or any other
    Python sorting feature in your answer to this question.

    The parameter `a_str` is a string consisting of only the lower case letters
    `[a..z]`with a default value of `''` (the empty string) which is deemed
    to be in alphabetical order.

    If the characters in `a_str` are all in normal alphabetical order then
    return `True`, else return `false`."""
    # if the string has length zero or one then it is sorted
    if len(a_str) < 2:
        return True
    # now iterate through the rest of a_str, testing that every character
    # is not less than the preceding character.
    preceding_character = a_str[0]
    for current_character in a_str[1:]:
        if current_character < preceding_character:
            return False
        preceding_character = current_character
    # all done, all in order
    return True


def deal(an_int):
    """This function simulates dealing `an_int` number of cards from a shuffled
    deck of playing cards. The parameter `an_int` is guaranteed to be an
    integer between 0 and 52 inclusive with a default value of one.

    A set of playing cards consists of 52 individual cards each marked as
    belonging to one of four suits (clubs, diamonds, hearts, spades) and one of
    thirteen face values (ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, knave, queen, king).
    The pack contains no duplicates so every card is unique with its deck.

    When called, this function should return a list of `an_int` playing cards
    with each card being a tuple containing two strings. The first for its face
    value and the second for its suit.

    Just like a real deck of cards, the same card cannot be dealt twice on a
    single call of `deal()`."""
    # import the random library
    import random
    # create the deck of cards
    suits = 'clubs diamonds hearts spades'.split(' ')
    faces = ('ace 2 3 4 5 6 7 8 9 10'
             ' knave queen king').split(' ')
    deck_as_tuples = []
    for s in suits:
        for f in faces:
            deck_as_tuples.append((f, s))
    # deck created as tuple for each card

    # now deal the hand
    hand_as_tuples = random.sample(deck_as_tuples, an_int)
    return hand_as_tuples


def write_html(a_str='LIN6209 - Coding for Linguists',
               filename='webpage.html'):
    """This function writes `a_str` into a well-formed HTML file named `filename`.

    The default value of `a_str` is `'LIN2609 - Coding for Linguists'`.\
    The default value of `filename` is `'webpage.html'`."""

    html_string_template = '<!DOCTYPE html>' \
        '<html lang="en">' \
        '<head>' \
        '    <title>Page Title</title>' \
        '</head>' \
        '<body>' \
 \
        '<h1>This is a Heading</h1>' \
        '<p>This is a paragraph.</p>' \
 \
        '</body>' \
        '</html>'

    html_string_start = \
        '<!DOCTYPE html>' \
        '<html lang="en">' \
        '<head>' \
        '    <title>Page Title</title>' \
        '</head>' \
        '<body>' \
        '<h1>This is a Heading</h1>'

    html_string_middle = '<p>' + a_str + '</p>'

    html_string_end = \
        '</body>' \
        '</html>'

    html_string_new = html_string_start + html_string_middle + html_string_end
    with open(filename, mode='wt', encoding='utf-8') as out_file:
        out_file.write(html_string_new)
    return html_string_new


def ascending_v2(filename, alphabet=string.ascii_lowercase):
    # Open file  as text and return its contents as a string"""
    with open(filename, 'rt', encoding='utf-8') as f:
        file_contents = f.read()
    # get the number of characters in the file_contents
    len_file_contents = len(file_contents)

    # if file contains just zero or one characters treat as special cases
    if len_file_contents == 0:
        return (0, 0), (0, 0)
    if len_file_contents == 1:
        if file_contents[0] in alphabet:
            return (0, 1), (0, 1)
        else:
            return (0, 0), (0, 0)

    # iterate through file_contents and find the longest contiguous sequence of
    # characters all in alphabet
    longest_word_start = 0
    longest_word_end = 0
    # current_word_start = 0  # is reassigned when 1st character in alphabet found
    # current_word_end = 0 # is reassigned when end of word is found
    longest_asc_seq_start = 0
    longest_asc_seq_end = 0
    current_asc_seq_start = 0
    current_asc_seq_end = 0

    index = 1  # start at 2nd character
    while index < len_file_contents:
        # absorb successive non-alphabetic characters
        while (file_contents[index] not in alphabet and
               index < len_file_contents):
            index += 1
            # check not at end of file contents
            # if index == len_file_contents:
            #     # at end of file contents therefore done, return results
            #    return longest_word_start, longest_word_end
        # have found beginning of next word
        current_word_start = index
        # search for end of word
        while (file_contents[index] in alphabet and
               index < len_file_contents):
            index += 1
        # have found end of word
        current_word_end = index
        #
        # check if current word is the longest
        if ((current_word_end - current_word_start) >
                (longest_word_end - longest_word_start)):
            # new longest
            longest_word_start = current_word_start
            longest_word_end = current_word_end
        #
        # check if current word contains the longest non-decreasing subsequence
        # start by checking it is longer than last sequence found
        if (longest_asc_seq_end - longest_asc_seq_start >
                current_word_end - current_word_start):
            # it is long enough to contain a candidate
            # set up variable to find ascending sequences
            current_asc_seq_start = current_word_start
            asc_index = current_word_start + 1
            while asc_index < current_word_end:
                if file_contents[asc_index] < file_contents[asc_index - 1]:
                    # ascending sequence has ended
                    current_asc_seq_end = asc_index
                    # check if it is longest
                    if (current_asc_seq_end - current_asc_seq_start >
                            longest_asc_seq_end - longest_asc_seq_start):
                        longest_word_start = current_asc_seq_start
                        longest_asc_seq_end = current_asc_seq_end
                    # reset variables
                    current_asc_seq_start = current_asc_seq_end
                # increment asc_index
                asc_index += 1
                # and done so return some values
    return (longest_word_start, longest_word_end), (
            longest_asc_seq_start, longest_asc_seq_end)


def ascending_v1(filename, alphabet=string.ascii_lowercase):
    """The parameter `alphabet` is a string of characters with no duplicates
    and has a default value of `[a-z]`.

    The characters in `filename` are NOT all guaranteed to be in `alphabet`.
    Any character in `filename` that is not in `alphabet` is a word separator.
    Uninterrupted consecutive sequences of characters from `alphabet`
    in `filename` are words.

    The order of the characters in `alphabet` defines ascending alphabetical
    order for this function. For instance, if `alphabet = 'azbrdvkge'` then
    the strings `'aardvark', 'badger', 'zebra'` arranged in `alphabet` order
    are `'aardvark', 'zebra', 'badger'`.

    Answer two tuples containing the starting position and length of:

    * the longest consecutive sequence of characters within `filename` that are
    all in `alphabet`
    * the longest consecutive sequence of characters within `filename` that are
    in all in `alphabet` AND in non-decreasing order as defined by `alphabet`

    If there are multiple such substrings, report the first. If the file is empty
    return zeros"""

    # I have seperated this into multiple inner functions as it seems a handy
    # capability to have available for strings
    # First: Just read the file and return a string
    def readfile_to_str(f_name):
        """Open f_name  as text and return its contents as a string"""
        with open(f_name, 'rt', encoding='utf-8') as f:
            f_contents = f.read()
        return f_contents

    def get_words(a_str):
        """Split a_str into words and return a list of tuples.
        Each tuple contains the start and end indices of the word in a_str
        as defined by normal string slicing.

        * `word = a_str[start_index, end_index]`"""
        len_a_str = len(a_str)
        index = 0
        list_word_tuples = []  # [(start_index, end_index), ... ]

        while index < len_a_str:
            # find beginning of word
            while a_str[index] not in alphabet and index < len_a_str:
                index += 1
            # found beginning of next word
            word_start_index = index
            #  capture the word into a string
            while a_str[index] in alphabet and index < len_a_str:
                index += 1
            word_end_index = index
            # append indices as a tuple to the list of word tuples
            list_word_tuples.append((word_start_index, word_end_index))
        # end of string
        return list_word_tuples

    def get_longest_word(list_of_word_tuples):
        # find the longest word and return its start and end indices
        len_longest_word = 0
        longest_word_start = 0
        longest_word_end = 0
        for each_tuple in list_of_word_tuples:
            len_word = each_tuple[1] - each_tuple[0]
            if len_word > len_longest_word:
                longest_word_start = each_tuple[0]
                longest_word_end = each_tuple[1]
        return longest_word_start, longest_word_end

    def get_longest_ascending_v2(a_str='',
                                 list_of_word_tuples=(0, 0),
                                 alphabet=string.ascii_lowercase):
        """Get the start and end indexes of the longest non-decreasing
        sequence of characters in a_str.

        """
        # couple of variables to hold longest non-decreasing sequence
        # found so far
        longest_start = 0
        longest_end = 0
        longest_found = 0
        # iterate through tuples
        for a_tuple in list_of_word_tuples:
            word_length = a_tuple[1] - a_tuple[0]
            if word_length < 2:
                # only zero or one character so it MUST be in order
                if longest_found < word_length:
                    longest_start = a_tuple[0]
                    longest_end = a_tuple[0]
                    longest_found = word_length
            # iterate through word comparing adjacent characters
            for i in range(a_tuple[0], a_tuple[1]):
                pass

        # check special case of a 0 or 1 length word
        # word_length = len(a_word)
        # if word_length < 2:
        #     return 0, word_length
        # word has at least two characters so set up some pointers and counters
        longest_start = 0  # start index of longest non-decreasing sequence
        longest_length = 0  # length of longest sequence found so far
        current_start = 0  # start index of current substring
        current_length = 0  # length of current substring

        #####################################

    def get_longest_ascending(a_word, inner_alphabet=alphabet):
        """Get the start and end indexes of the longest non-decreasing
        sequence of characters in a_str.
        Ordering is as defined by alphabet parameter.
        All characters in a_str are guaranteed to be in alphabet"""
        # check special case of a 0 or 1 length word
        word_length = len(a_word)
        if word_length < 2:
            return 0, word_length
        # word has at least two characters so set up some pointers and counters
        longest_start = 0  # start index of longest non-decreasing sequence
        longest_length = 0  # length of longest sequence found so far
        current_start = 0  # start index of current substring
        current_length = 0  # length of current substring
        # search for non-decreasing sequences
        current_index = 2
        while current_index < word_length:
            if alphabet.find(a_word[current_index]) < \
                    alphabet.find(a_word[current_index - 1]):
                # current character is less than preceding character
                # hence end of non-decreasing sequence
                # check if it is the longest
                if (current_index - current_start) > longest_length:
                    longest_start = current_start
                    longest_length = current_index - current_start
                # update current start and length
                current_start = current_index
            # update
            current_length += 1
            # go round loop again
            current_index += 1


ascending = ascending_v2
