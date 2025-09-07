def write_ints(filename: str, an_int: int) -> None:
    """The parameters are guaranteed to be a legal filename and an integer
    greater than or equal to zero.
    Create the file and write `an_int` lines to the file.
    The successive lines of the file each start with the `next integer`
    in the ascending sequence from 1 to `an_int`
    followed by the sequence of integer multiples of `next_integer`
    up to and including `next_integer * next_integer`.
    All the integers in the same line are separated by a single space.
    No space is added at the beginning or the end of the line."""
    # open the named file for writing
    with open(filename, mode='wt', encoding='utf-8') as f:
        # the file has been opened for write hence exists and is empty
        # which satisfies the condition when an_int is zero
        # loop through the integers from 1 to an_int to create each line
        for i in range(1, an_int + 1):
            # start each line with the current integer
            line = str(an_int) + ' -'
            # and a loop for every following integer on that line
            for j in range(1, i + 1):
                line = line + ' ' + str(i * j)
            f.write(line + '\n')
    return  # no return value
