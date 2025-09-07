# Functions to perform basic textual analysis on the text of a book

def get_chars(a_str, char_filter=None) -> [str]:
    """Return a list of all the individual characters in a_str for which char_filter(char) is True.

    :param a_str: The string that is to be seperated into individual characters.
    :param char_filter: only include characters for which char_filter() returns True.
    :return: a list of the individual characters in a)str
    """
    if char_filter is None:
        return list(a_str)
    else:
        return [char for char in a_str if char_filter(char)]


def get_words(a_str:str, sep=' ', word_filter=None) -> [str]:
    """Return a list of all the words in a_str separated by sep and for which word_filter(word) is True.

    :param a_str: The string that is to be seperated into individual words.
    :param sep: The character that demarks the boundary between words.
    :param word_filter: only include words for which word_filter() returns True.
    :return: A list of the words in a_str
    """
    # get list of all characters
    chars = list(a_str)
    # only keep alphanumerics
    for char in chars:
        if not char.isalnum():
            chars.remove(char)
    # split the string on spaces
    words = a_str.split(' ')
    # remove full stops, exclamation marks and question marks

    # [char for char in a if char.isalnum() or char == ' ']


def get_paragraphs(a_str, sep='\n', para_filter=filter) -> [str]:
    pass


def get_chapters(a_str, sep='chapter', chap_filter=filter) -> [str]:
    pass


def get_char_freq():
    pass


def get_word_freq():
    pass
