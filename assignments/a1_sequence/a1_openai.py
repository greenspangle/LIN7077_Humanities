def all_ops_part1(int1, int2):
    return (int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2,
            int1 % int2)


# Example test
assert all_ops_part1(5, 3) == (8, 2, 15, 5 / 3, 1, 2)


def all_ops_part2(int1, int2):
    return (int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2,
            int1 > int2)


# Example test
assert all_ops_part2(5, 3) == (False, False, False, True, True, True)


def magic_number(a_num):
    return '7' in str(a_num)


# Example test
assert magic_number(77) == True
assert magic_number(3.714) == True
assert magic_number(123) == False
assert magic_number(7.0) == True


def hms_to_s(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


# Example tests
assert hms_to_s(0, 0, 0) == 0
assert hms_to_s(1, 0, 0) == 3600
assert hms_to_s(0, 1, 0) == 60
assert hms_to_s(0, 0, 1) == 1
assert hms_to_s(1, 1, 1) == 3661


def s_to_hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return (hours, minutes, seconds)


# Example tests
assert s_to_hms(0) == (0, 0, 0)
assert s_to_hms(3600) == (1, 0, 0)
assert s_to_hms(3661) == (1, 1, 1)
assert s_to_hms(59) == (0, 0, 59)
assert s_to_hms(86399) == (23, 59, 59)


def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    # Convert both times to seconds
    total_seconds1 = hms_to_s(hr1, min1, sec1)
    total_seconds2 = hms_to_s(hr2, min2, sec2)

    # Sum the seconds
    total_seconds = total_seconds1 + total_seconds2

    # Convert back to hours, minutes, seconds
    return s_to_hms(total_seconds)


# Example test
assert add_hms(0, 0, 3600, 0, 0, 61) == (1, 1, 1)


# Helper function to convert pounds, shillings, and pennies to total pennies
def old_uk_psp_to_p(pounds, shillings, pennies):
    return pounds * 240 + shillings * 12 + pennies


# Helper function to convert total pennies back to pounds, shillings, and pennies
def old_uk_p_to_psp(pennies):
    pounds = pennies // 240
    pennies %= 240
    shillings = pennies // 12
    pennies %= 12
    return (pounds, shillings, pennies)


# Main function to add two amounts
def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    # Convert both amounts to pennies
    total_pennies1 = old_uk_psp_to_p(pounds1, shillings1, pennies1)
    total_pennies2 = old_uk_psp_to_p(pounds2, shillings2, pennies2)

    # Sum the pennies
    total_pennies = total_pennies1 + total_pennies2

    # Convert back to pounds, shillings, and pennies
    return old_uk_p_to_psp(total_pennies)


# Example test
assert add_old_uk(0, 19, 11, 19, 0, 1) == (20, 0, 0)


def is_palindrome(phrase):
    # Convert to lowercase and remove spaces
    cleaned_phrase = phrase.lower().replace(" ", "")

    # Check if the cleaned phrase is equal to its reverse
    return cleaned_phrase == cleaned_phrase[::-1]


# Example test
assert is_palindrome('Abba') == True
assert is_palindrome('A man a plan a canal Panama') == True
assert is_palindrome('Hello World') == False


def is_anagram(phrase1, phrase2):
    # Convert to lowercase and remove spaces from both phrases
    cleaned_phrase1 = phrase1.lower().replace(" ", "")
    cleaned_phrase2 = phrase2.lower().replace(" ", "")

    # Sort characters in both cleaned phrases and compare
    return sorted(cleaned_phrase1) == sorted(cleaned_phrase2)


# Example tests
assert is_anagram('Dusty', 'Study') == True
assert is_anagram(' ', ' ') == True
assert is_anagram('Dusty', 'Books') == False


def is_anagram(phrase1, phrase2):
    # Convert both phrases to lowercase, remove spaces, and sort the characters
    cleaned_phrase1 = sorted(phrase1.lower().replace(" ", ""))
    cleaned_phrase2 = sorted(phrase2.lower().replace(" ", ""))

    # Check if the sorted characters are equal
    return cleaned_phrase1 == cleaned_phrase2


# Example tests
assert is_anagram('Dusty', 'Study') == True
assert is_anagram(' ', ' ') == True
assert is_anagram('Dusty', 'Books') == False


def lucky_fun(lucky_object):
    # Convert lucky_object to string
    lucky_str = str(lucky_object)

    # Return a function that checks for the occurrence
    def checker(arg):
        return lucky_str in str(arg)

    return checker


# Example tests
assert lucky_fun(7)(7) == True
assert lucky_fun('7')(7) == True
assert lucky_fun(7)('7') == True
assert lucky_fun(123)(456) == False
