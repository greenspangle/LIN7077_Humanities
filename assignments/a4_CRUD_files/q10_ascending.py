import string
from typing import List, Tuple, Union


def ascending(filename: str, alphabet: str = string.ascii_lowercase):
    """
    The parameters are:

    * 'filename' - the name of the file containing the text to be examined
    * `alphabet` - a string of characters with no duplicates
      and a default value of `[a-z]`.

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
      all in `alphabet` AND in non-decreasing order as defined by `alphabet`

    If there are multiple such substrings, report the first. If the file is empty
    return zeros"""

    # I have seperated this into multiple functions for two reasons:
    #   1. it breaks the problem at hand in smaller, simpler parts
    #   2. the sub functions seem potentially useful in themselves

    # read the file contents to a string
    file_as_str = readfile_to_str(filename)
    # break the string into words
    words_in_file = get_words(file_as_str, alphabet)
    # find the longest word
    longest_word = find_longest_word(words_in_file)
    # find the longest non-decreasing sequence within a word
    longest_ascending = find_longest_nondecreasing(words_in_file)
    # and return the result
    return longest_word, longest_ascending


# First: read the file and return a string
def readfile_to_str(f_name: str) -> str:
    """Open f_name  as text and return its contents as a string"""
    with open(f_name, 'rt', encoding='utf-8') as f:
        f_contents = f.read()
    return f_contents


# break the string into words
def get_words(a_str: str,
              alphabet: str = string.ascii_lowercase
              ) -> List[Tuple[int, int]]:
    """Split a_str into words and return a list of tuples.
    Each tuple contains the start and end indices of the word in a_str
    as defined by normal string slicing.

    * `word = a_str[start_index, end_index]`"""
    len_a_str = len(a_str)
    index = 0
    list_word_tuples = []  # [(start_index, end_index), ... ]

    while index < len_a_str:
        # find beginning of next word
        while index < len_a_str and a_str[index] not in alphabet:
            index += 1
        # found beginning of next word
        word_start_index = index
        #  capture the word into a string
        while index < len_a_str and a_str[index] in alphabet:
            index += 1
        word_end_index = index
        # append indices as a tuple to the list of word tuples
        list_word_tuples.append((word_start_index, word_end_index))
    # end of string
    return list_word_tuples


# find the longest word
def find_longest_word(list_of_word_tuples: List[Tuple[int, int]]
                      ) -> Tuple[int, int]:
    # find the longest word and return its start and end indices
    len_longest_word = 0
    longest_word = 0, 0
    for this_tuple in list_of_word_tuples:
        len_word = this_tuple[1] - this_tuple[0]
        if len_word > len_longest_word: # we only need the first longest word
            len_longest_word = len_word
            longest_word = this_tuple
    return longest_word


# find the longest non-decreasing sequence within a word
def find_longest_nondecreasing(
        list_of_word_tuples: List[Tuple[int, int]],
        alphabet: str = string.ascii_lowercase) -> Tuple[int, int]:
    """Get the start and end indexes of the longest non-decreasing
    sequence of characters in a_str.
    """
    # couple of variables to hold longest non-decreasing sequence
    # found so far
    len_longest_seq = 0
    longest_seq = 0,0
    # iterate through tuples of words
    for this_tuple in list_of_word_tuples:
        word_length = this_tuple[1] - this_tuple[0]
        if len_longest_seq < word_length: # if not then cannot be in this word
            longest_start = this_tuple[0]
            longest_end = this_tuple[0]
            longest_found = word_length
        # iterate through word comparing adjacent characters
        for i in range(this_tuple[0], this_tuple[1]):
            pass
    return 0, 0


#
#
#
if __name__ == "__main__":
    assert get_words('abc def') == [(0, 3), (4, 7)]

    words = get_words('abc defg hij')
    print(words)
    print(find_longest_word(words))  # == (4, 8)
