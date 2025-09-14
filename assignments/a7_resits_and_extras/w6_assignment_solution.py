# W6 LIN 7077 Assignment.
# Design, build and test the following functions.
# Submit your python student_script with the filename 'w6_yourID.py'.
# This is one version of the answers."""

import string  # this module contains the whitespace() method


def num_seq_str_v1(an_int):
    """The parameter is guaranteed to be a positive integer greater than zero. Return a string containing the
    integers 1 to an_int inclusive. Successive integers are separated by a comma and a space. Note that there is
    no trailing comma or space at the end of the string. """
    result = ''  # will build return value as a string
    for i in range(1, an_int + 1):
        result += str(i) + ', '  # append next integer with trailing comma+space
    # result contains required return value - PLUS a trailing comma+space
    result = result[:-2]  # drop the trailing comma+space
    return result


def num_seq_str_v2(an_int):
    """Same pattern as v1, but entirely with lists"""
    result = []  # will build return value as a list of strings
    for i in range(1, an_int + 1):
        result.append(str(i) + ', ')  # each element is an integer followed by a comma+space
    # all component parts of result are now assembled in list
    # use str.join() method to assemble list elements into a string
    result = ' '.join(result)
    return result[:-2]  # and return result minus the trailing comma+space


def num_seq_str_v3(an_int):
    """Same pattern as v1, but entirely with lists"""
    int_list = []  # first build the list of integers
    for i in range(1, an_int + 1):
        int_list.append(str(i))  # each element is an integer
    # all component parts of result are now assembled in list
    # use str.join() method to assemble list elements into a string separated by comma+space
    result_str = ", ".join(int_list)
    return result_str  # and return result


def num_seq_str_v4(an_int):
    """Same pattern as v3, but with a list comprehension"""
    int_list = [str(i) for i in range(1, an_int + 1)]
    # assemble list of integers into a string separated by comma-space and done
    return ', '.join(int_list)


# I like v4 best as it's concise but perhaps v1 is the easiest to understand?
# best use v1 as that's the most 'obvious'
num_seq_str = num_seq_str_v1


def num_seq_list(an_int):
    """The parameter is guaranteed to be a positive integer greater than zero. Return a list containing the
    integers 1 to an_int inclusive."""
    return [i for i in range(1, an_int + 1)]


def num_seq_set(an_int):
    """The parameter is guaranteed to be a positive integer greater than zero. Return a set containing the integers
    1 to an_int."""
    return {i for i in range(1, an_int + 1)}  # create set using a comprehension


def num_seq_dict_v1(an_int):
    """The parameter is guaranteed to be a positive integer greater than zero. Return a dictionary containing the
    integers 1 to an_int as the keys of the dictionary. The value associated with each key should be the string
    returned by fizzbuzz(key)."""
    return {i: fizzbuzz(i) for i in range(1, an_int + 1)}


def num_seq_dict_v2(an_int):
    """Make the assembly of the dictionary explicit"""
    result_dictionary = {}  # an empty dictionary
    for i in range(1, an_int + 1):
        result_dictionary[i] = fizzbuzz(i)  # add the integer keys and set value to fizzbuzz
    # all done so just return the assembled dictionary
    return result_dictionary


# the list comprehension is especially neat :-) but stick with the simpler v2
num_seq_dict_ = num_seq_dict_v2



def char_frequency(filename):
    """Return a dictionary with every character in filename as a key with a value equal to
    the number of its occurrences with filename."""
    # Read the file
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        contents = f.read()
    # file contents are now in 'content'. Iterate through it counting character occurrences into a dictionary
    # create an empty dictionary
    char_freq = dict()  # an empty dictionary
    # for every character, increment its entry in dictionary, creating an entry if it is not already present
    for char in contents:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
            # all done, just return the dictionary containing the frequency information
    return char_freq


def word_frequency(filename):
    """Return a dictionary with every word in filename as a key and the associated value the number
     of its occurrences within filename."""
    # open the file and read it's contents
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        contents = f.read()
    # file contents are now in 'content'.
    # replace all whitespace by true whitespace ' '
    for char in string.whitespace:
        contents.replace(char, ' ')
    words = contents.split()  # split content on spaces (default behaviour of split() method)
    w_freq = {}  # create an empty dictionary to hold results
    # for every character, increment its entry in dictionary, creating an entry if it is not already present
    for word in words:
        if word in w_freq:  # if this word is in dictionary
            w_freq[word] += 1  # increase its count by one
        else:  # if it's not in dictionary
            w_freq[word] = 1  # add an entry to dictionary with a count of 1
    # all done, just return the dictionary containing the frequency information
    return w_freq


def average_word_length(filename):
    """Return average length of the 'words' in the file"""
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        f_contents = f.read()
        # file read and closed, contents now in f_contents.
        # replace all whitespace by true whitespace ' '
        for char in string.whitespace:
            f_contents.replace(char, ' ')
        # split on spaces (default behaviour of split() method)
        f_words = f_contents.split()
        # iterate through that list of words counting instances and their lengths
        sum_words = 0
        sum_lengths = 0
        for word in f_words:
            sum_words += 1
            sum_lengths += len(word)
        # calculate the average length
        if sum_words == 0:  # check for division by zero
            result = 0
        else:
            result = sum_lengths / sum_words
        return result





def write_q(an_int, filename):
    """The parameters are guaranteed to be a positive integer **greater than zero** and a legal filename.
    Write the sequence of integers from 1 to an_int inclusive to a text file, with each integer separated
    from the next by the string ' ? ' (space, question mark, space). The return value should be the count
    of the total number of characters written to the file."""
    # open file for write
    with open(filename, 'wt', encoding='utf-8') as f:
        # iterate through the integers from 1 to an_int inclusive, counting the characters written
        # an_int must be one or greater, so write '1' to file
        f.write('1')
        c_count = 1  # and set count of characters to one
        # now write successive integers preceded by ' ? '
        for i in range(2, an_int + 1):
            a_str = ' ? ' + str(i)  # assemble string to be written,
            c_count += len(a_str)  # update the count of characters,
            f.write(' ? ' + str(i))  # and write to file
        # and return the count of characters written
        return c_count


def write_ints(an_int, filename):
    """The parameters are guaranteed to be a positive integer **or zero** and a legal filename.
    Create the file if it does not already exist and write `an_int` lines to the file.
    The successive lines of the file each start with the `next integer` in the ascending sequence from 1
    to `an_int` followed by the sequence of integer multiples of `next_integer` up to and including
    `next_integer * next_integer`.
    All the integers in the same line are separated by a single space.
    No space is added at the beginning or the end of the line."""
    # open file for write
    with open(filename, 'w', encoding='utf-8') as f:
        # iterate through the integers from 0 up to an_int inclusive
        for i in range(1, an_int + 1):
            # for each successive i write a line to the file
            # each line is the sequence of multiples of i from 1*i to i*i separated by spaces
            for j in range(1, i):
                # up to the last multiple write the value followed by space
                f.write(str(i * j) + ' ')
            # at the end of the line write i*i followed by newline
            f.write(str(i * i) + '\n')
        # and that's it done (leave the trailing newline in the file)
    # no return value is specified so return None
    return None
