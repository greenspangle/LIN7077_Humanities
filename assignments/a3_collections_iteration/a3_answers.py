# LIN7077 Assignment #3 - Collections & Iteration


# define some constants for collections of characters
A_TO_Z_UC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
A_TO_Z_LC = 'abcdefghijklmnopqrstuvwxyz'
A_TO_Z = A_TO_Z_LC + A_TO_Z_UC
VOWELS_UC = 'AEIOU'
VOWELS_LC = 'aeiou'
VOWELS = VOWELS_LC + VOWELS_UC
CONSONANTS_UC = 'BCDFGHJKLMNPQRSTVWXYZ'
CONSONANTS_LC = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS = CONSONANTS_LC + CONSONANTS_UC
DIGITS = '0123456789'


def robber_lingo(a_str):
    """Translate a_str text into 'rövarspråket'
    (Swedish for “robber’s language”).
    That is, double every consonant and place an occurrence of 'o' in between.
    For example, robber_lingo('this is fun') should return the string
    'tothohisos isos fofunon'.
    """
    # create a list to build result in
    robber_list = []
    # consonants are characters that are not vowels
    consonants = set('abcdefghijklmnopqrstuvwxyz') - set('aeiou')
    # iterate through a_str
    # testing for consonants and constructing result as we go.
    for char in a_str:
        # all characters in a_str are retained in translated text
        robber_list.append(char)
        # consonants are repeated with an 'o' between them
        if char in consonants:
            robber_list.append('o')
            robber_list.append(char)
    # All done. Assemble result and return it
    result = ''.join(robber_list)
    return result


def char_counts(a_str):
    """Return the number of vowels, the number of consonants,
    the number of digits, and the number of other characters in the
    parameter string `a_str`.
    """
    count_vowels = 0
    count_consonants = 0
    count_digits = 0
    count_other = 0

    for char in a_str:
        if char in VOWELS:
            count_vowels += 1
        elif char in CONSONANTS:
            count_consonants += 1
        elif char in DIGITS:
            count_digits += 1
        else:
            count_other += 1
    return count_vowels, count_consonants, count_digits, count_other


def seq_collections(an_int):
    """Return a tuple containing the integers 1 to an_int inclusive,
    as a string, a set, and a list."""
    ints_str = ''
    ints_set = set()
    ints_list = [[], []]
    for i in range(1, an_int + 1):
        ints_str += str(i) + ' '
        ints_set.add(i)
        if i % 2:
            # index i is odd, so add to second sublist
            ints_list[1].append(i)
        else:
            # index i is even, so add it to first sublist
            ints_list[0].append(i)
    #  remove the trailing space ' ' from the end of ints_str
    ints_str = ints_str[:-1]
    # reverse the second sublist
    ints_list[1].reverse()
    return ints_str, ints_set, ints_list


def fiddledee_dict(an_int):
    # first create the function fiddledee()
    def fiddledee(another_int):
        f_or_d_or_both = ''
        if another_int % 3 == 0:
            f_or_d_or_both += 'Fiddle'
        if another_int % 2 == 0:
            f_or_d_or_both += 'Dee'
        if f_or_d_or_both == '':
            return str(another_int)
        return f_or_d_or_both

    # create a dictionary
    result = {}
    # iterate across range adding integer as key and fiddledee as value
    for i in range(1, an_int + 1):
        result[i] = fiddledee(i)
    return result
    # return {i: fizzbuzz(i) for i in range(1, an_int + 1)}


def char_count_dict(a_str):
    """Return a dictionary with every character (including spaces and
    punctuation) in a_str as a key in the dictionary with a value equal
    to the number of occurrences of that character in a_str."""

    # create the dictionary with en entry for every character in a_str
    count = dict.fromkeys(a_str, 0)
    # Now iterate through `a_str`
    # and update the entry for each character as we go
    for char in a_str:
        count[char] += 1
    # when finished, return the dictionary of characters with counts
    return count


def word_count_dict_v1(a_str):
    """Return a dictionary with every word in a_str as a key with an associated
    value of the number of times that word occurs in a_str.
    A word is any unbroken sequence of characters in the
    collection [a-z] + [A-Z] + [0-9].
    All characters not in that collection are word separators."""
    # first build the alphabet as a single string
    alphabet = A_TO_Z_LC + A_TO_Z_UC + DIGITS
    # now iterate through a_str, replacing all word separators by spaces
    a_list = []
    for character in a_str:
        if character in alphabet:
            a_list.append(character)
        else:
            a_list.append(' ')
    # and join everything together into a string
    str_words = ''.join(a_list)
    # now split out the words which are all separated by one or more spaces
    list_words = str_words.split(' ')
    # create a dictionary to hold result
    word_dict = {}
    # iterate through list of words associating every word with its count
    for word in list_words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    # remove dictionary entry for empty word ''
    if '' in word_dict:
        del word_dict['']
    return word_dict


def word_count_dict_v2(a_str):
    """Return a dictionary with every word in a_str as a key with an associated
    value of the number of times that word occurs in a_str.
    A word is any unbroken sequence of characters in the
    collection [a-z] + [A-Z] + [0-9].
    All characters not in that collection are word separators."""
    # keep track of current word and previous and current characters
    curr_word = ''
    prev_char = ' '  # set to a word seperator value
    # make a collection containing all 'word' characters
    word_chars = A_TO_Z + DIGITS
    # make an empty dictionary to contain words and their counts
    word_counts = {}
    # iterate through string one character at a time
    for curr_char in a_str:
        if curr_char in word_chars:
            # this char is part of a word,
            # update curr_word and prev_char and move to next character
            curr_word += curr_char
            prev_char = curr_char
        else:
            # we are at a word seperator.
            if prev_char in word_chars:
                # we are at a word boundary.
                # Update count in dictionary for current word
                if curr_word in word_counts:
                    word_counts[curr_word] += 1
                else:
                    word_counts[curr_word] = 1
                # reset current word to empty
                curr_word = ''
    # a_str is exhausted, just return the result
    return word_counts


word_count_dict = word_count_dict_v1


def isa_pangram_v1(a_str: str) -> bool:
    """Answer true if a_str is a pangram and false if not.
    Ignore capitalisation and punctuation, only consider the characters a-z."""
    # Iterate through alphabet and check that every character is in a_str
    # Ignore capitalisation so convert everything to lower case
    a_str_lc = a_str.lower()
    # iterate through a..z and check every letter is in string
    for each_char in A_TO_Z_LC:
        if each_char not in a_str_lc:
            # a letter of the alphabet is missing from a_str
            # Hence it is not a pangram
            return False
    # all letters of alphabet are present, so it is a pangram
    return True


def isa_pangram_v2(a_str: str) -> bool:
    """Answer true if a_str is a pangram and false if not.
    Ignore capitalisation and punctuation, only consider the characters a-z."""
    # solve by removing all character in a_str
    # from a set of the alphabet characters
    # a pangram contains all the letters 'a' to 'z' so construct that set
    alphabet = set(A_TO_Z_LC)
    # convert string to lower-case and then cast to a set
    a_str_as_set = set(a_str.lower())
    # remove all the characters in a_str_as_set from alphabet
    remainder = alphabet - a_str_as_set
    # if remainder is empty set
    # then string contains all letters of alphabet and hence is a pangram
    return set() == remainder


def isa_pangram_v3(a_str: str) -> bool:
    """Answer true if a_str is a pangram and false if not.
    Ignore capitalisation and punctuation, only consider the characters a-z."""
    # solve using set algebra
    # a pangram contains all the letters 'a' to 'z' so construct that set
    alphabet = set(A_TO_Z_LC)
    # convert parameter string to lower-case and then cast to a set
    a_str_as_set = set(a_str.lower())
    # get the set of alphabetical characters in a_str_set
    # by intersecting it with alphabet
    a_str_as_set_set = a_str_as_set.intersection(alphabet)
    # if a_str_as_set is equal to the alphabet
    # then a_str is a pangram, else it is not
    return a_str_as_set_set == alphabet


# both options work but v1 seems simplest and best
isa_pangram = isa_pangram_v1


def zip_2(str_1, str_2):
    """Interleave the sorted strings str1 and str2 into a new string
    in such a way that the characters in the resulting string
    are maintained in ascending alphabetical order."""
    # build result as a list of characters
    result = []
    # we will need to index both strings so get both lengths
    len_1 = len(str_1)
    len_2 = len(str_2)
    # and we will need to index into both strings
    index_1 = 0
    index_2 = 0
    # iterate through both until one or other or both are exhausted
    while index_1 < len_1 and index_2 < len_2:
        if str_1[index_1] < str_2[index_2]:
            result.append(str_1[index_1])
            index_1 += 1
        else:
            result.append(str_2[index_2])
            index_2 += 1
    #  One of the parameter strings is exhausted (possibly both)
    if index_1 >= len_1:
        # str_1 is exhausted so just add remainder of str_2 to result
        result.append(str_2[index_2:])
    else:
        result.append(str_1[index_1:])
    # all done
    # join the characters in the list into a string
    result = ''.join(result)
    return result


def zip_n_iterative(*strings):
    # reuse zip_2() to merge list of strings iteratively
    num_strings = len(strings)
    if num_strings == 0:
        return ''
    if num_strings == 1:
        return strings[0]
    # there are at least two strings
    # create a variable to hold successive iterations of final result
    # and initialise it with the first string
    result_so_far = strings[0]
    # successively apply zip_2 to result_so_far and next string in strings
    for i in range(1, num_strings):
        result_so_far = zip_2(result_so_far, strings[i])
    # all done
    return result_so_far


def zip_n_all_at_once(*strings):
    # process all the strings in parallel
    # determine how many strings there are
    num_strings = len(strings)
    if num_strings == 0:
        return ''
    if num_strings == 1:
        return strings[0]
    # there are at least two strings
    # create a list to hold the result as it is built
    result = []
    # we need variables to track progress of zipping these strings
    # a list of variables that index current char in each string
    str_indices = [0] * num_strings
    # a list containing the length of each string
    str_lengths = [i for i in map(len, strings)]
    # start zipping the strings together
    while True:
        # find the first un-exhausted string
        list_with_lowest = -1
        for i in range(num_strings):
            if str_indices[i] < str_lengths[1]:
                list_with_lowest = i
                break
        # if there are no un-exhausted lists left exit while loop
        if list_with_lowest == -1:
            break
        # there is at least one un-exhausted list
        # iterate through the rest looking for an even lower character
        for i in range(list_with_lowest + 1, num_strings):
            # skip string if it is exhausted
            if str_indices[i] >= str_lengths[i]:
                continue
            # check if it has the lowest character so far
            if (strings[i][str_indices[i]] <
                    strings[list_with_lowest][str_indices[list_with_lowest]]):
                # it is the new lowest
                list_with_lowest = i
        # list with the lowest character identified, so add it to result
        result.append(strings[list_with_lowest][str_indices[list_with_lowest]])
        # and increment index for that list
        str_indices[list_with_lowest] += 1

    # all done, assemble the result into a string and return it
    return ''.join(result)


def zip_n_recursive(*strings):
    # solve using recursion
    num_strings = len(strings)
    if num_strings == 0:
        return ''
    if num_strings == 1:
        return strings[0]
    if num_strings == 2:
        return zip_2(strings[0], strings[1])
    # num_strings >= 2 so split and recurse
    return zip_n_recursive(
        zip_n_recursive(*strings[0:num_strings // 2]),
        zip_n_recursive(*strings[num_strings // 2:])
    )


# choose the algorithm I like best
zip_n = zip_n_recursive


def caesar(msg,
           shift=3,
           encode=True,
           alphabet=A_TO_Z_LC + DIGITS + A_TO_Z_UC + '.,!? '):
    # get the length of the alphabet
    alphabet_len = len(alphabet)
    # create list to contain letters of encoded message
    result = []
    # decoding is the inverse of encoding
    if not encode:
        shift *= -1
    # iterate through message processing each letter and adding to result
    for letter in msg:
        position = alphabet.find(letter)
        if position == -1:
            # character not in alphabet so add to result unchanged
            result.append(letter)
        else:
            # shift character along in alphabet ad add to result
            result.append(alphabet[(position + shift) % alphabet_len])
    # all done, assemble result into a string and return it
    return ''.join(result)
