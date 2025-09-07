def get_words(a_str, alphabet='abcd'):
    """break a string into words.
    Words are contiguous sequences of characters in 'alphabet'.
    Return a list of tuples.
    Each tuple contains the start and end indices of a word"""

    str_len = len(a_str)
    # special cases for lengths 0 and 1#
    if str_len == 0:
        return []
    if str_len == 1:
        if a_str[0] in alphabet:
            return [(0, 1)]
        else:
            return []

    # string longer than 1
    curr_char_alpha = None  # will be assigned in while loop
    word_start_index = 0
    prev_char_alpha = a_str[0] in alphabet
    str_index = 1
    words = []

    # now iterate through the rest of the string
    while str_index < str_len:
        curr_char_alpha = a_str[str_index] in alphabet
        if prev_char_alpha and curr_char_alpha:
            pass  # do nothing, inside a word, move to next character
        elif not prev_char_alpha and not curr_char_alpha:
            pass  # do nothing, inside space, move to next character
        elif not prev_char_alpha and curr_char_alpha:
            # word start boundary
            word_start_index = str_index
        else: # prev_char_alpha and not curr_char_alpha:
            # word end boundary
            word_end_index = str_index
            words.append((word_start_index, word_end_index))

        # prepare for iteration of while loop
        str_index += 1
        prev_char_alpha = curr_char_alpha
    # at end of string. Check if it is also a word end
    if curr_char_alpha:  # yes, ends with a word
        word_end_index = str_index
        words.append((word_start_index, word_end_index))
    # all done
    return words


def get_longest_words(list_of_tuples):
    longest_words = []
    longest_word_length = 0
    for a_tuple in list_of_tuples:
        word_length = a_tuple[1] - a_tuple[0]
        if word_length > longest_word_length:
            # new longest word length
            longest_word_length = word_length
            longest_words.clear()
            longest_words.append(a_tuple)
        elif word_length == longest_word_length:
            # another longest word, so add to list
            longest_words.append(a_tuple)
    return longest_words


def get_longest_word(list_of_tuples):
    return list_of_tuples[0]


# break a string into words
# Words are contiguous sequences of characters in 'alphabet'
# return a list of tuples each containing the start and end indices of a word

def get_words(a_str, alphabet='abcd'):
    # variables
    # str_len
    # str_index
    # word_start_index
    # word_end_index
    # prev_char_alpha
    # curr_char_alpha
    # result

    str_len = len(a_str)
    # special cases for lengths 0 and 1#
    if str_len == 0:
        return []
    if str_len == 1:
        if a_str[0] in alphabet:
            return [(0, 1)]
        else:
            return []

    # string longer than 1
    word_start_index = 0
    prev_char_alpha = a_str[0] in alphabet
    str_index = 1
    result = []

    # now iterate through the rest of the string
    while str_index < str_len:
        curr_char_alpha = a_str[str_index] in alphabet
        if prev_char_alpha and curr_char_alpha:
            pass  # do nothing, inside a word
        if not prev_char_alpha and not curr_char_alpha:
            pass  # do nothing, inside space
        if prev_char_alpha and not curr_char_alpha:
            # word end boundary
            word_end_index = str_index
            result.append((word_start_index, word_end_index))
        if not prev_char_alpha and curr_char_alpha:
            # word start boundary
            word_start_index = str_index
        # prepare for next loop
        str_index += 1
        prev_char_alpha = curr_char_alpha
    # at end of string. Check if it is also a word end
    if curr_char_alpha:  # yes, end with a word
        word_end_index = str_index
        result.append((word_start_index, word_end_index))

    # all done
    return result











