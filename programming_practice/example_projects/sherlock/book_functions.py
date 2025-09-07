"""Functions extracted from various notebooks in this project."""

"""
               Functions from Iteration 1
"""


def read_book_to_str(book_file_name):
    """Read a text file into a string"""
    with open(book_file_name, mode='r', encoding='utf-8') as book_file_handle:
        book_as_str = book_file_handle.read()
        return book_as_str


def book_char_counts(book_str):
    """Classify the characters in the book into a dictionary.

    The keys of the dictionary are: all_char, lowercase, uppercase, digits,
    punctuation, space, whitespace, other"""
    # the code is deliberately 'simple' in approach to aid understandability

    # Define what counts as lowercase, uppercase, etc.
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    space = ' '
    whitespace = '\t\n\r'

    # set counts to zero
    count_chars = 0
    count_uppercase = 0
    count_lowercase = 0
    count_digits = 0
    count_punctuation = 0
    count_space = 0
    count_whitespace = 0
    count_other = 0

    # iterate through the book classifying each character in turn
    for char in book_str:
        count_chars += 1
        if char in lowercase:
            count_lowercase += 1
        elif char in uppercase:
            count_uppercase += 1
        elif char in digits:
            count_digits += 1
        elif char in punctuation:
            count_punctuation += 1
        elif char in space:
            count_space += 1
        elif char in whitespace:
            count_whitespace += 1
        else:
            count_other += 1
    # put the results in a dictionary
    char_counts = {'all_char': count_chars,
                   'lowercase': count_lowercase,
                   'uppercase': count_uppercase,
                   'digits': count_digits,
                   'punctuation': count_punctuation,
                   'space': count_space,
                   'whitespace': count_whitespace,
                   'other': count_other}
    # and return the dictionary
    return char_counts



"""
               Functions from Iteration 1
"""
