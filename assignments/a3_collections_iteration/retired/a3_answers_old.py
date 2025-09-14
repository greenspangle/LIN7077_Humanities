# LIN7077 Collections & Iteration Assignment (#3 assessed)


#  The functions count_a(), count_digits(), count_vowels(), count_consonants are all built to the same pattern.
# So rather than repeat that pattern in code several times in each function,
# generalise the problem, solve that, and apply the general solution to each instance
def count_special_chars(a_str, special_chars):
    """Return the count of characters present in a_str that are also present in special_chars"""
    count = 0
    for each_char in a_str:
        if each_char in special_chars:
            count += 1
    return count


def count_a(a_str: str):
    """Return the number of times the character `'a'` occurs in the parameter a_str which is guaranteed to be a
    string."""
    return count_special_chars(a_str.lower(), 'a')


def count_digits(a_str):
    """Return the number of numeric digits in the parameter string a_str.
    A digit is any one of the characters ‘0123456789’."""
    return count_special_chars(a_str.lower(), '0123456789')


def count_vowels(a_str):
    """Count the number of vowels"""
    return count_special_chars(a_str.lower(), 'aeiou')


def count_consonants(a_str):
    """Count the number of consonants"""
    return count_special_chars(a_str.lower(), 'bcdfghjklmnpqrstvwxyz')


def contains_substr(a_str, b_str):
    return b_str in a_str


def count_substr(a_str, b_str):
    return a_str.count(b_str)


def get_sequence_list(an_int):
    return list(range(1, an_int + 1))


def get_sequence_set(an_int):
    return set(range(1, an_int + 1))


get_sequence_as_set = get_sequence_set


def get_sequence_str(an_int):
    return ' '.join(map(str, list(range(1, an_int + 1))))


def times2_dict(an_int):
    return {i: i * 2 for i in range(1, an_int + 1)}


def fizzbuzz_dict(an_int):
    from assignments.a02_selection.a02_answers import fizzbuzz
    return {i: fizzbuzz(i) for i in range(1, an_int + 1)}


def robber_lingo(a_str):
    """Translate a_str text into 'rövarspråket'
    (Swedish for “robber’s language”).
    That is, double every consonant and place an occurrence of 'o' in between.
    For example, robber_lingo('this is fun') should return the string
    'tothohisos isos fofunon'.
    """
    # Example in problem statement is all lower-case and
    # statement says nothing about upper case.
    # Assume therefore that uppercase is just copied verbatim into the result
    #
    # create a list to build result in
    robber_lst = []
    # consonants are characters that are not vowels
    consonants = set('abcdefghijklmnopqrstuvwxyz') - set('aeiou')
    # iterate through string
    # testing for consonants and constructing result as we go.
    for char in a_str:
        # all characters in a_str are retained in translated text
        robber_lst.append(char)
        if char in consonants:
            # consonants are repeated with an 'o' between them
            robber_lst.append('o')
            robber_lst.append(char)
    # All input string processed. Assemble result into a string and return it
    result = ''.join(robber_lst)
    return result


def isa_pangram_v1(a_str: str) -> bool:
    """Answer true if a_str is a pangram and false if not.
    Ignore capitalisation and punctuation, only consider the characters a-z."""
    # a pangram contains all the letters 'a' to 'z' so construct that set
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # convert string to lower-case and then cast to a set
    a_str_as_set = set(a_str.lower())
    # get the set of alphabetical characters in a_str_set
    # by intersecting it with alphabet
    a_str_as_set_set = a_str_as_set.intersection(alphabet)
    # if a_str_as_set is equal to the alphabet then a_str is a pangram
    # else it is not
    return a_str_as_set_set == alphabet


def isa_pangram_v2(a_str: str) -> bool:
    """Answer true if a_str is a pangram and false if not. Ignore capitalisation and punctuation, only consider
    the characters a-z."""
    # a pangram contains all the letters 'a' to 'z' so construct that set
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # convert string to lower-case and then cast to a set
    a_str_as_set = set(a_str.lower())
    # remove all the characters in a_str_as_set from alphabet
    remainder = alphabet - a_str_as_set
    # if remainder is empty set then string contains all letters of alphabet and hence is a pangram
    return set() == remainder


# both options are good
# but I have to choose one of them so let it be this choice
isa_pangram = isa_pangram_v2


def merge2(str1, str2):
    """Interleave the successive characters of two strings of the same length into a single string and return
    the result."""
    # the two strings are stated to be the same length
    # but let's check regardless
    if len(str1) != len(str2):
        print(
            "please stop breaking the function contract and expecting me to cope!")
        return ''
    # build result as a list of strings
    result = []
    for i in range(len(str1)):
        result.append(str1[i] + str2[i])
    # both strings processed, now transform the result from list to a single string
    result = ''.join(result)
    # and return it
    return result


def merge3(str1, str2, str3):
    """Interleave the successive characters of three strings of the same length into a single string and return
    the result."""
    # exactly the same logic as merge2()
    # the strings are stated to be the same length but let's check regardless
    if len(str1) != len(str2) or len(str2) != len(str3):
        print(
            "please stop breaking the function contract and expecting me to cope!")
        return ''
    # build result as a list of strings
    result = []
    for i in range(len(str1)):
        result.append(str1[i] + str2[i] + str3[i])
    # all 3 strings processed, now transform the result from list to a single string
    result = ''.join(result)
    # and return it
    return result


def mergen_short(*tuple_of_strings):
    """Interleave the successive characters of any number of strings of any length into a single string and return the
    result. Interleaving is halted when the shortest string is exhausted."""
    # the strings to be interleaved are the elements of the tuple tuple_of_strings
    # get the length of the shortest
    lengths = []
    for each_str in tuple_of_strings:
        lengths.append(len(each_str))
    shortest_len = min(lengths)
    # and now it's the same logic as merge2 and merge3 except we have to use another loop
    result = []
    for i in range(shortest_len):
        for each_str in tuple_of_strings:
            result.append(each_str[i])
    # all strings processed, now transform the result from list to a single string
    result = ''.join(result)
    # and return it
    return result


merge3_short = mergen_short


def mergen_long(*tuple_of_strings):
    """Interleave the successive characters of any number of strings of any length into a single string and return
    the result. As individual strings become exhausted, continue interleaving  the remaining strings until all
    are exhausted."""
    # the strings to be interleaved are the elements of the tuple tuple_of_strings
    # get the length of the longest
    string_lengths = []
    for each_str in tuple_of_strings:
        string_lengths.append(len(each_str))
    longest_len = max(string_lengths)
    # and now it's the same logic as mergen_shortest except we have to use an explicit
    # test to skip exhausted strings
    result = []
    for i in range(longest_len):
        for each_str in tuple_of_strings:
            if i < len(each_str):
                result.append(each_str[i])
    # all strings processed, now transform the result from list to a single string
    result = ''.join(result)
    # and return it
    return result


merge3_long = mergen_long


def letter_count(a_str):
    """Return a dictionary with every character (including spaces and punctuation) in a_str as a key with a value
    equal to the number of occurrences of that character in a_str. Only characters in a_str are keys in the
    returned dictionary."""
    # create the dictionary with the key entries associated with a value of 0
    letter_dict = dict.fromkeys(a_str, 0)
    # now iterate through string, incrementing the respective entry for every character encountered
    for each_char in a_str:
        letter_dict[each_char] += 1
    # all letters done, return the resulting dictionary
    return letter_dict


def letter_count_v2(a_str):
    a_str_set = set(a_str)
    return {char: a_str.count(char) for char in a_str_set}
