# A short diversion to Unicode.
[www.unicode.org](www.unicode.org)

Unicode is a very successful attempt to represent [every character of every language](https://www.unicode.org/charts/) in a form that can be manipulated in a computer. It also now includes [emojis](https://www.unicode.org/emoji/charts/emoji-list.html).

For an introduction see the lesson at [https://realpython.com/python-encodings-guide/](https://realpython.com/python-encodings-guide/)

The examples below print the character sets for Arabic, Bengali, and Ancient Egyptian Hieroglyphs. You can find the codes for many other character sets at www.unicode.org/charts/ . NOTE: the code numbers for the Unicode characters is a [HEXADECIMAL](https://en.wikipedia.org/wiki/Hexadecimal) (base 16) number and not a more familiar denary (base 10) number. That is a number to base 16 rather than the usual base 10. Python understands hexadecimal numbers provided they are prefixed by '0x'. That means that the hexadecimal number 9e (158 denary, 10011110 binary) is written 0x9e in Python.

``` python 
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
```

Find a character set for your language of choice and write a 'while' routine to print them out.

Not every character set will have the been installed on Your PC will almost certainly not have all the fonts for all the unicode character sets installed. If the font is missing you will probably get a list of small empty rectangles printing instead.

See the Unicode documentation for all the glorious details.
