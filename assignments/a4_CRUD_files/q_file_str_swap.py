def file_to_str(filename):
    """open the named file, read it into a string, and return that string """
    with open(filename, mode='rt', encoding='utf-8') as f:
        # the file has been opened for write hence exists and is empty
        # which satisfies the condition when an_int is zero
        # loop through the integers from 1 to an_int to create each line
        a_str = f.read()
    return a_str


def csvfile_to_str(filename):
    """open the named file, read it into a string, and return that string """

    pass


def str_to_file(a_str, filename):
    """open the named file, read it into a string, and return that string """
    with open(filename, mode='wt', encoding='utf-8') as f:
        # the file has been opened for write hence exists and is empty
        f.write(a_str)
    return  # no return value


def str_to_csvfile(filename):
    """open the named file, read it into a string, and return that string """

    pass
