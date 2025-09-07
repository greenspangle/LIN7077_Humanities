"""Simple example of while loops"""


def example_1():
    """Count from 0 to 10"""
    a = 0  # set a to an initial value
    while a <= 10:  # if true execute block of code
        print(a)  # print current value of a
        a = a + 1  # increment current value of a


def example_2():
    """print the alphabet """
    code = ord('a')
    stop = code + 26
    while code < stop:
        print(chr(code), end='')
        code = code + 1


alphabet_1 = example_2


def only_vowels(a_str='the quick brown fox jumps over the lazy dog'):
    """Print only the vowels from a string. Replace all else by '_'"""
    vowels = 'aeiou'
    index = 0
    while index < len(a_str):
        if a_str[index] in vowels:
            print(a_str[index], end=' ')
        index = index + 1


def chars_arabic():
    print('Arabic alphabet (unicode 0600-06ff) and please pardon my ignorance')
    code = 0x0600
    stop = 0x06ff
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()


def chars_bengali():
    print('Bengali character set (unicode 0980—09FF) ')
    code = 0x0980
    stop = 0x09ff
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()


def chars_hieroglyphs():
    print('Egyptian Hieroglyphs character set (unicode  Range: 13000—1342F , 1072 characters)')
    code = 0x13000
    stop = 0x1342F
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()
