# LIN6209 Files (#4 assessed)

import string  # module contains various collections of ASCII characters
import csv  # module for precessing comma seperated files

# define some constants for collections of characters
# VOWELS_UC = 'AEIOU'
# VOWELS_LC = VOWELS_UC.lower()
# VOWELS = VOWELS_LC + VOWELS_UC
#
# CONSONANTS_UC = 'BCDFGHJKLMNPQRSTVWXYZ'
# CONSONANTS_LC = CONSONANTS_UC.lower()
# CONSONANTS = CONSONANTS_LC + CONSONANTS_UC


def ascending_v2(filename, alphabet=string.ascii_lowercase):
    # Open file and return contents as a string"""
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


ascending = ascending_v2
