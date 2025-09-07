import string


def write_random(filename: str = 'random_chars.txt',
                 size: int = 6209,
                 alphabet: str = string.digits) -> None:
    """Write `size` random characters from `alphabet` to a file named `filename`.
    The parameters are:
    * filename: a legal file name with a default value of `'random_chars.txt'`
    * size: a positive integer with a default value of `6209`
    * alphabet: a collection of characters with a default value of `'0123456789'`

    **Hints:**
    * The `random` library contains functions that select random elements from a
      collection
    * Open the file `filename` for write
    * Write `size` randomly selected characters from `alphabet` to the file
      called `filename`
    """
    import random

    with open(filename, mode='wt', encoding='utf-8') as out_file:
        counter = 0
        while counter < size:
            random_char = random.choice(alphabet)
            out_file.write(random_char)
            counter += 1
        # all done
    return  # no return value specified
