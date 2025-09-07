"""The examples below print the character sets for Arabic, Bengali, and Ancient Egyptian Hieroglyphs."""


def chars_arabic():
    """Print the Arabic character set (unicode 0600-06ff)"""
    print('\n\nThe Arabic character set:')
    code = 0x0600
    stop = 0x06ff
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()


def chars_bengali():
    """Print the Bengali character set (unicode 0980—09FF)"""
    print('\n\nThe Bengali character set')
    code = 0x0980
    stop = 0x09ff
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()


def chars_hieroglyphs():
    """print the Egyptian Hieroglyphs character set (unicode  Range: 13000—1342F , 1072 characters)"""
    print('\n\nThe Egyptian Hieroglyphs')
    code = 0x13000
    stop = 0x1342F
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()


if __name__ == '__main__':
    chars_arabic()
    chars_bengali()
    chars_hieroglyphs()
