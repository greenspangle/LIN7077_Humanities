# LIN6209 Files (#4 assessed)

# Useful to create these global constants?
ALPHA_LC = 'abcdefghijklmnopqrstuvwxyz'
ALPHA_UC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS_09 = '0123456789'
import string  # this module contains the collection of whitespace characters


def thermostat(temperature):
    """If the temperature is less that 19 turn the heat on, if it's more than 24 turn the heat off, and if it's
    neither, leave the heat setting as it is.
    Return the string `'heat on'`, `'heat off'` or `'stet'` respectively."""
    # the three clauses in this compound if statement include all possible values of temperature
    # therefore one of them must return a value
    if temperature < 19:
        return 'heat on'
    elif temperature > 24:
        return 'heat off'
    else:
        return 'stet'


def score_2(dice_1, dice_2):
    """The parameters are guaranteed to be integers between 1 and 6 inclusive and represent the face values on the
    throw of two six-sided dice. Calculate the score according to this rule:
        1 The score is the sum of both dice
        2 unless it is a 'double' (both dice the same) in which case add one of the dice to the score again
        3 unless it is 'double six' (both dice six) in which case add both dice to the score again
        4 unless the sum of the two dice is seven in which case double it"""
    # a sequence of if statements covers all possibilities
    score = dice_1 + dice_2  # rule 1
    if score == 7:  # rule 4 = sum is seven
        score = 14
    if dice_1 == dice_2:  # rule 2 = it's a double
        score = dice_1 + dice_2 + dice_1
    if dice_1 == 6 and dice_2 == 6:  # rule 3 = double six!
        score = dice_1 + dice_2 + dice_1 + dice_2
    # all options considered, return the score
    return score


def score_4(red_1, red_2, blue_1, blue_2):
    """The parameters are guaranteed to be integers between 1 and 6 inclusive. They represent the face values on
        the throw of four six-sided dice, two coloured red and two coloured blue. Calculate the score according to
        the rule:
            1 The score is the face value of the lowest of all four dice
            2 Unless the sum of any one red dice and any one blue dice is seven in which case score 7
            3 Unless the sum of any one red dice and any one blue dice is seven, and the sum of the remaining red and
              blue dice is also seven, in which case score 14
            4 Unless the four dice are any permutation of (3,3,4,4), in which case score 21 """

    # a couple of ways to do this
    def score_4_v1(red1, red2, blue1, blue2):
        # as successive independent if statements, from the least restrictive to the most
        # rule 1 - use the built-in function min(). This also ensures that score always has a value
        score = min((red1, red2, blue1, blue2))
        # rule 2 - if the sum of any one red dice and any one blue dice is seven
        if red1 + blue1 == 7 or red1 + blue2 == 7 or red2 + blue1 == 7 or red2 + blue2 == 7:
            score = 7
        # rule 3 - if the sum of any one red dice and any one blue dice is seven,
        #          and the sum of the remaining red and blue dice is also seven
        if (red1 + blue1 == 7 and red2 + blue2 == 7) or (red1 + blue2 == 7 and red2 + blue1 == 7):
            score = 14
        # rule 4 - the four dice are any permutation of (3,3,4,4),
        if (red1 == 3 and red2 == 3 and blue1 == 4 and blue2 == 4) or \
                (red1 == 3 and red2 == 4 and blue1 == 3 and blue2 == 4) or \
                (red1 == 3 and red2 == 4 and blue1 == 4 and blue2 == 3) or \
                (red1 == 4 and red2 == 3 and blue1 == 3 and blue2 == 4) or \
                (red1 == 4 and red2 == 3 and blue1 == 4 and blue2 == 3) or \
                (red1 == 4 and red2 == 4 and blue1 == 3 and blue2 == 3):
            score = 21
        return score

    def score_4_v2(red1, red2, blue1, blue2):
        # as a single if-elif-else cascade, from the most restrictive to the least
        if sorted([red1, red2, blue1, blue2]) == [3, 3, 4, 4]:
            score = 21
        elif (red1 + blue1 == 7 and red2 + blue2 == 7) or \
                (red1 + blue2 == 7 and red2 + blue1 == 7):
            score = 14
        elif red1 + blue1 == 7 or \
                red1 + blue2 == 7 or \
                red2 + blue1 == 7 or \
                red2 + blue2 == 7:
            score = 7
        else:
            score = min((red1, red2, blue1, blue2))
        return score

    # why not test them for equivalence
    assert score_4_v1(red_1, red_2, blue_1, blue_2) == score_4_v2(red_1, red_2, blue_1, blue_2)
    # I like v2 best
    return score_4_v2(red_1, red_2, blue_1, blue_2)


def get_all_chars(filename):
    """The parameter is guaranteed to be the name of a text file encoded as utf-8.
    Open the file read-only and return the set of all characters present in the file."""
    # read the file into a string
    with open(filename, 'rt', encoding='utf-8') as f:
        file_string = f.read()
    # create a set with every character in the file in it
    file_set = set(file_string)
    # and that's the answer, so return it
    return file_set


# to maintain compatability with a previous version create get_chars_set()
# get_chars_set = get_all_chars


def count_chars(filename):
    """Read the file and return number of characters in the file. There is no need to be concerned
    as to what constitutes a 'character', count everything."""
    # read the file into a string
    with open(filename, 'rt', encoding='utf-8') as f:
        file_string = f.read()
    # everything in a string is, by definition, a character
    # so the total number of characters is just the length of the string
    return len(file_string)


def count_and(filename):
    """Read the file and count the number of occurrences of each of the character strings
     'and', ' and ', and ' and, ' (the string 'and'; same but with spaces both sides;
     same again but with a space before and a comma and a space after).
     Ignore the case of the text. Return the respective counts as a tuple of integers."""
    # read the file into a string
    with open(filename, 'rt', encoding='utf-8') as f:
        file_string = f.read()
    # question says to ignore case, so convert everything to lower case
    file_string = file_string.lower()
    # use the count() method from the string library
    num_and = file_string.count('and')
    num_sp_and_sp = file_string.count(' and ')
    num_sp_and_comma_sp = file_string.count(' and, ')
    # and that's all that's required so return result
    return num_and, num_sp_and_sp, num_sp_and_comma_sp


def count_words(filename):
    """The parameter is the name of a text file containing only the characters [a-z][A-Z], spaces `' '`,
    and the escape sequences `'\n'` and `'\t'`. Read the file and return number of words in the file.
    A word is any sequence of characters from [a-z][A-Z] seperated by one or more spaces or escape sequences."""

    # a couple of ways to do this
    def count_words_v1(f_name):
        # read the file into a string
        with open(f_name, 'rt', encoding='utf-8') as f:
            file_string = f.read()
        # replace '\n' and '\t' with ' '
        file_string = file_string.replace('\n', ' ').replace('\t', ' ')
        # split into words wherever there is a space
        words = file_string.split(' ')
        # but words potentially contains elements that are empty strings
        # remove them
        words = [word for word in words if word != '']
        # and that's the list of words so return the number of elements
        return len(words)

    def count_words_v2(f_name):
        with open(f_name, 'r', encoding='utf_8') as f:
            # assume the file is not too big to chomp in a single mouthful ....
            f_contents = f.read()
        # file read and closed, contents now in f_contents.
        # replace all whitespace by true whitespace ' '
        for char in string.whitespace:
            f_contents.replace(char, ' ')
        # split on spaces (default behaviour of split() method)
        f_contents = f_contents.split()
        # every word is an element in that list  so number of words is length of that list
        return len(f_contents)

    # v2 is incorrect!
    assert count_words_v1(filename) == count_words_v2(filename)
    return count_words_v2(filename)


def char_frequency(filename):
    """Return a dictionary with every character in the file `filename` as a key
    with a value equal to the number of its occurrences in the file."""

    def v1(f_name):
        # read the file into a string
        with open(f_name, mode='rt', encoding='utf-8') as f:
            file_string = f.read()
        # create the dictionary with the key entries associated with a value of 0
        letter_dict = dict.fromkeys(file_string, 0)
        # now iterate through string, incrementing the respective entry for every character encountered
        for each_char in file_string:
            letter_dict[each_char] += 1
        # all letters done, return the resulting dictionary
        return letter_dict

    def v2(f_name):
        # read the file into a string
        with open(f_name, mode='rt', encoding='utf-8') as f:
            file_string = f.read()
        # create the dictionary
        char_counts = dict()
        # and count the words into it
        for char in file_string:
            if char in char_counts:
                # get its count and increment by 1
                char_counts[char] = char_counts[char] + 1
            else:
                # add char to dictionary with a value of one
                char_counts[char] = 1
        # all words counted so return the dictionary
        return char_counts

    assert v1(filename) == v2(filename)
    # prefer v2
    return v2(filename)


def word_frequency(filename):
    """Return a dictionary with every word in filename as a key and the associated value
    the number of its occurrences with filename."""
    # read the file into a string
    with open(filename, mode='rt', encoding='utf-8') as f:
        file_string = f.read()
    # replace every whitespace character by ' ', an actual space
    for char in string.whitespace:
        file_string = file_string.replace(char, ' ')
    # split into words wherever there is a space. This is the default behaviour of str.split()
    words = file_string.split()
    # create the dictionary to contain the words and their counts
    word_counts = dict()
    # count the words and update the dictionary
    for word in words:
        if word in word_counts:
            # get its count and increment by 1
            word_counts[word] = word_counts[word] + 1
        else:
            # add word to dictionary with a value of one
            word_counts[word] = 1
    # all words counted so return the dictionary
    return word_counts


def write_Q(filename, an_int):
    """The parameters are guaranteed to be a legal filename and an integer greater than or equal to zero.
    Create the file and write `an_int` lines to the file.
    The structure of the successive lines of the file is:
        the next integer in the sequence from `1` to `an_int` inclusive,
        followed by a `space character`,
        followed by `an_int` number of successive `'?'` characters,
        followed by a `newline`."""
    # open the named file for writing
    with open(filename, mode='wt', encoding='utf-8') as f:
        for i in range(an_int):
            j = i + 1
            f.write(str(j) + ' ' + '?' * j + '\n')
    return


def write_ints(filename, an_int):
    """The parameters are guaranteed to be a legal filename and an integer greater than or equal to zero.
    Create the file and write `an_int` lines to the file.
    The successive lines of the file each start with the `next integer` in the ascending sequence from 1 to `an_int`
    followed by the sequence of integer multiples of `next_integer` up to and including `next_integer * next_integer`.
    All the integers in the same line are separated by a single space.
    No space is added at the beginning or the end of the line."""
    # open the named file for writing
    with open(filename, mode='wt', encoding='utf-8') as f:
        # loop for the first integer on every line
        for i in range(1, an_int + 1):
            line = str(i)
            # and a loop for every following integer on that line
            for j in range(2, i + 1):
                line = line + ' ' + str(i * j)
            f.write(line + '\n')


def runup(filename):
    """The file is guaranteed to consist only of the lowercase characters [a-z].
    Answer a tuple containing the starting position and length of the longest sequence
     of characters within `filename` that is in alphabetical order.
     Alphabetical order means `'a'` then `'b'` and so on all the way to `'z'`.
     If there are multiple such substrings, report the first. If the file is empty return (0, 0)."""

    # I have seperated this into two inner functions as it seems a handy capability to have available for strings
    # First: Just read the file and return a string
    def readfile(f_name):
        with open(f_name, 'rt', encoding='utf-8') as f:
            f_contents = f.read()
        return f_contents

    # Second: now find the longest non-decreasing sub-sequence
    def runup_str(a_str):
        # deal with special cases
        len_a_str = len(a_str)
        if len_a_str == 0 or len_a_str == 1:
            return 0, len_a_str
        # set up some pointers and counters
        longest_start = 0
        longest_length = 0
        current_start = 0
        current_length = 1  # because we know string is not empty
        # iterate through a_str
        for i in range(1, len_a_str):
            # compare adjacent elements
            if a_str[i] < a_str[i - 1]:  # end of current sequence
                # current_length = i - current_start
                if current_length > longest_length:
                    longest_start = current_start
                    longest_length = current_length
                # reset current sequence
                current_start = i
                current_length = 1
            else:  # still non-decreasing
                current_length += 1
        # the string is exhausted, check if current sequence is longest
        if current_length > longest_length:
            longest_start = current_start
            longest_length = current_length
        # all done, return the result
        return longest_start, longest_length

    # Solve the original problem by composing the two functions
    return runup_str(readfile(filename))
