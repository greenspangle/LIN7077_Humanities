"""Analysing text - practice variable_names"""


def remove_hf(oldfilename, newfilename):
    """read the file from Project Gutenberg and remove the header and footer to leave just the parts that
    contain the book"""
    with open(oldfilename, 'r', encoding='utf-8') as oldtext:
        # read the whole file into a string
        g_book = oldtext.read()
        # split string into three parts
        parts123 = g_book.partition('*** START OF THIS PROJECT GUTENBERG EBOOK A STUDY IN SCARLET ***')
        # and we only want the part after that line
        g_book = parts123[2]
        # partition it again
        parts123 = g_book.partition('*** END OF THIS PROJECT GUTENBERG EBOOK A STUDY IN SCARLET ***')
        # and we only want the part before that line
        g_book = parts123[0]
    # now write just the book out to the new file
    with open(newfilename, 'w', encoding='utf-8') as newtext:
        # the book is in the variable g_book, so write all of that
        newtext.write(g_book)
    #  all done, so just return
    return


def contains(a_str, filename):
    """Test if a given string occurs anywhere in the file filename"""
    # Open the file and read it into a string
    with open(filename, 'r', encoding='utf-8') as text:
        book = text.read()
        # test if a_str is in text
        if a_str in book:
            return True
        else:
            return False


def char_count_v1(a_char, filename):
    """Count the number of occurrences or the character a_char in the file filename"""
    # read the file into a string
    with open(filename, 'r', encoding='utf-8') as text:
        book = text.read()
        # we can close the file now as we have contents as a string
    # count the number of occurrences
    count = 0
    for char in book:
        if a_char == char:
            count += 1
    # all done, return the count
    return count


def char_count_v2(a_char, filename):
    """Count the number of occurrences of the character a_char in the file filename"""
    # read the file into a string
    with open(filename, 'r', encoding='utf-8') as text:
        book = text.read()
        # we can close the file now as we have contents as a string
    # count the number of occurrences using the string method count()
    count = book.count(a_char)
    # and return the result
    return count

char_count = char_count_v2 

def char_counts(filename):
    """Count all the characters in filename and return the result in a dictionary.
    The keys of the dictionary ar the different characters, the vales are the counts of those respective
    characters in filename."""
    # could read the file a line at a time, just in case it is too big
    # for each_line in f:
    #      print(x) 
    
    
    
    # read the file into a string
    with open(filename, 'r', encoding='utf-8') as text:
        book = text.read()
        # we can close the file now as we have contents as a string
    # create the dictionary from the string
    char_dict = dict.fromkeys(book, 0)
    # iterate through string one character at a time
    for this_char in book:
        # for each character in string, update character count by 1
        char_dict[this_char] = char_dict[this_char] + 1
    # all characters in string accounted for, return the dictionary
    return char_dict


def word_count_v1(a_word, filename):
    """Count the number of occurrences of the string a_word in the file filename"""
    # read the file into a string
    with open(filename, 'r', encoding='utf-8') as text:
        book = text.read()
        # we can close the file now as we have contents as a string
    # split the string every time there is a whitespace character
    # place resultant word in a list
    words = book.split()
    # create a counter and then iterate list of words searching for a_word
    count = 0
    for each_word in words:
        if each_word == a_word:
            count = count + 1
    # all done, return the count of matches found
    return count


def word_count_v2(a_word, filename):
    """Count the number of occurrences of the string a_word in the file filename"""
    # read the file into a string
    with open(filename, 'r', encoding='utf-8') as text:
        book = text.read()
        # we can close the file now as we have contents as a string
    # split the string every time there is a whitespace character
    # place resultant word in a list
    words = book.split()
    # use the list method count() to count the occurrences of a_word
    count = words.count(a_word)
    # and return the result
    return count


def word_counts_v1(filename):
    """Count all the words in filename and return the result in a dictionary.
       The keys of the dictionary are the different words, the values are the counts of those respective
       characters in filename."""
    # read the file into a string
    with open(filename, 'r', encoding='utf-8') as text:
        book = text.read()
        # we can close the file now as we have contents as a string
    # split the string every time there is a whitespace character
    # place resultant words in a list
    words = book.split()
    # create the dictionary from the list of words
    word_dict = dict.fromkeys(words, 0)
    # iterate through string one character at a time
    for each_word in words:
        # for each word in list, update that words count by 1
        word_dict[each_word] = word_dict[each_word] + 1
    # all characters in string accounted for, return the dictionary
    return word_dict



def word_counts_v2(filename):
    """Count all the words in filename and return the result in a dictionary.
       The keys of the dictionary are the different words, the values are the counts of those respective
       characters in filename."""
    # read the file into a string
    with open(filename, 'r', encoding='utf-8') as text:
        book = text.read()
        # we can close the file now as we have contents as a string
    book = remove_punctuation(book)   # remove punctuation from book
    book = book.lower()  # convert everything to lower case
    # split the string every time there is a whitespace character and place words in a list
    words = book.split()
    # create the dictionary from the list of words
    word_dict = dict.fromkeys(words, 0)
    # iterate through string one character at a time
    for each_word in words:
        # for each word in list, update that words count by 1
        word_dict[each_word] = word_dict[each_word] + 1
    # all characters in string accounted for, return the dictionary
    return word_dict


def get_words(filename):
    # read the file into a string
    with open(filename, 'r', encoding='utf-8') as text:
        book = text.read()
    # split the string every time there is a whitespace character. Place resultant words in a list
    return book.split()


def remove_punctuation(a_str):
    punctuation = '`¬!"“”£$%^&*()_+-={}[]:@~;\'’‘#<>?,./|\\ '
    list_of_chars = []
    for i in range(len(a_str)):
        if a_str[i] in punctuation:
            list_of_chars.append(' ')
        else:
            list_of_chars.append(a_str[i])
    return ''.join(list_of_chars)


def sort_dict_k(a_dict):
    sorted(a_dict.items())

if __name__ == '__main__':
    w = word_counts_v1('scarlet.txt')
    x = word_counts_v2('scarlet.txt')

    pass
    # remove_hf('A Study In Scarlet.txt', 'scarlet.txt')
