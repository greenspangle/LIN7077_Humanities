from typing import Tuple


def read_alternate_chars(filename: str) -> Tuple[set[str], set[str]]:
    """
    Open the file `filename` and return two **sets** of characters:
        * set_1 : the set of the first, third, fifth, and so on,
                  characters from the file
        * set_2 : the set of the second, fourth, sixth, and so on,
                  characters from the file
    """
    # open the file as text and iread it into a string
    with open(filename, 'rt', encoding='utf-8') as f:
        file_string = f.read()
    # slice the string into two sub-strings of alternate characters
    # and add each slice to a set
    set_even = set(file_string[0::2])  # start at [0] and step 2
    set_odd = set(file_string[1::2])  # start at [1] and step 2
    # and return the two sets
    return set_even, set_odd
