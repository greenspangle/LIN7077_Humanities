def is_alphabetical(a_str: str = '') -> bool:
    """
    Do not use the built-in function `sorted()` or `reversed()` or any other
    Python sorting feature in your answer to this question.

    The parameter `a_str` is a string guaranteed to consist of only lower case
    letters from `string.ascii_lowercase`.
    (see https://docs.python.org/3/library/string.html )
    It has a default value of `''` (the empty string) which is deemed to be in
    alphabetical order.

    If the characters in `a_str` are all in normal alphabetical order then
    return `True`, else return `False`.

    For example:

    |   a_str   | return value |
    |:---------:|:------------:|
    |   `''`    |    `True`    |
    |   `'a'`   |    `True`    |
    |  `'aaa'`  |    `True`    |
    |  `'ace'`  |    `True`    |
    | `'abbab'` |   `False`    |
    | `'aazaa'` |   `False`    |
    """
    # if the string has length zero or one then it is in alphabetical order.
    if len(a_str) <= 1:
        return True
    # now iterate through the rest of a_str, testing that every character
    # is not less than the preceding character.
    preceding_character = a_str[0]
    for current_character in a_str[1:]:
        if current_character < preceding_character:
            return False
        preceding_character = current_character
    # all done, all in order
    return True
