# read the book and do some basic cleanup to remove file header and footer

books=[('A Study In Scarlet.txt', 'A Study In Scarlet', 631, 241110),
       ]

def read_book(filename, mode='rt', library='gutenberg', encoding='utf-8') -> str:
    """Read the file, do some basic cleanup to remove file header and footer, and return the book contents as a string.

    :param filename: The name of the file containing the book
    :param library: The institution proving access to the book
    :param encoding: file encoding which is almost universally utf-8
    :return: A single string containing the text of the book
    """
    with open(filename, mode='rt', encoding=encoding) as f:
        book = f.read()
    # NO CLEANING is done on the text as the variations between texts are too numerous to reasonably accommodate.
    # Gross cleaning of the original file should be done manually.
    #
    # if library=='gutenberg':
    #     # header and footer are bracketed  by
    #     # *** START OF THIS PROJECT GUTENBERG EBOOK book title ***
    #     # *** END OF THIS PROJECT GUTENBERG EBOOK book title ***
    #     # so use that info to partition the file
    #     book=book.partition('*** START OF THIS PROJECT GUTENBERG EBOOK')
    #     book = book[2].partition('***')
    #     # and now the book footer
    #     book = book[2].partition('*** END OF THIS PROJECT GUTENBERG EBOOK')
    #     book = book[0]
    #     # but that still leaves many of the transcribers footnotes
    #
    return book
