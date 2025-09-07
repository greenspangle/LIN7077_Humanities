""" These are my answers to LIN6209 Assignment 1 (assessed)"""

# define two constants for H:M:S calculations
MINUTES_IN_HOUR: int = 60  # the number of minutes in every hour
SECONDS_IN_MINUTE: int = 60  # the number of seconds in every minute

# define two constants for £sd calculations
SHILLINGS_IN_POUND = 20  # avoids having the 'magic number' 20 everywhere
PENNIES_IN_SHILLING = 12  # ditto


def all_ops_part1(int1, int2):
    """ This function takes any two integers and returns the tuple
    (int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2,
    int1 % int2)
    """

    return int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2


def all_ops_part2(int1, int2):
    """ Same as all_ops_pt1 but this time with the operators
    <, <=, ==, !=, >=, and >
    """
    return (int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2,
            int1 > int2)


def magic_number(a_num):
    """ If the parameter a_num contains the digit 7 answer boolean True.
    If not, answer boolean False.
    """
    return '7' in str(a_num)


def hms_to_s(hours, minutes, seconds):
    """Convert a duration of hours:minutes:seconds to seconds"""
    hours_as_seconds = hours * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
    minutes_as_seconds = minutes * SECONDS_IN_MINUTE
    total_seconds = hours_as_seconds + minutes_as_seconds + seconds
    return total_seconds


def s_to_hms(seconds):
    """Convert a duration in seconds to hours:minutes:seconds in standard form.
    Standard form means hours, minutes, seconds are all integers, and minutes
    and seconds are both < 60. Parameter is guaranteed to be positive integer.
    """
    # determine the number of whole hours in the parameter
    hours = seconds // (MINUTES_IN_HOUR * SECONDS_IN_MINUTE)
    # then the number of seconds remaining after the hours have been removed
    remaining_seconds = seconds % (MINUTES_IN_HOUR * SECONDS_IN_MINUTE)
    # now the number of whole minutes in those remaining seconds
    minutes = remaining_seconds // SECONDS_IN_MINUTE
    # now the seconds remaining after the minutes have been removed
    remaining_seconds = remaining_seconds % SECONDS_IN_MINUTE
    # reinstate the correct sign and return
    return hours, minutes, remaining_seconds


def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    """Add two hour:minute:seconds time durations and answer the sum in
    standard form. Standard form means the minutes and seconds are both < 60
    Parameters are all guaranteed to be positive integers"""
    # taking the hint
    hms1_as_seconds = hms_to_s(hr1, min1, sec1)
    hms2_as_seconds = hms_to_s(hr2, min2, sec2)
    total_seconds = hms1_as_seconds + hms2_as_seconds
    total_hms = s_to_hms(total_seconds)
    # alternatively,
    # `return s_to_hms(hms_to_s(hr1, min1, sec1) + hms_to_s(hr2, min2, sec2))`
    return total_hms


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    """Add two pre-decimalisation amounts of UK currency and return the result
    in standard form with pennies < 12 and shillings < 20.

    Prior to 15 February 1971, UK currency consisted of
    pounds, shillings and pence.
    Twelve pence made one shilling and twenty shillings made one pound.
    Prices were displayed as £5/10s/6d (pronounced as "five pounds ten
    shillings and sixpence" https://en.wikipedia.org/wiki/%C2%A3sd)

    Parameters are all guaranteed to be positive integers.
    """

    # use the helper functions to add the two old money amounts
    return pennies_to_psd(psd_to_pennies(pounds1, shillings1, pennies1) +
                          psd_to_pennies(pounds2, shillings2, pennies2))


# define two helper functions
def psd_to_pennies(pounds, shillings, pennies):
    """Convert Old UK £sd to old UK pennies"""
    pounds_as_pennies = pounds * SHILLINGS_IN_POUND * PENNIES_IN_SHILLING
    shillings_as_pennies = shillings * PENNIES_IN_SHILLING
    total_pennies = pounds_as_pennies + shillings_as_pennies + pennies
    return total_pennies


def pennies_to_psd(pennies):
    """Convert old UK pennies to Old UK £sd"""
    pounds = pennies // PENNIES_IN_SHILLING // SHILLINGS_IN_POUND
    remaining_pennies = pennies % (PENNIES_IN_SHILLING * SHILLINGS_IN_POUND)
    shillings = remaining_pennies // PENNIES_IN_SHILLING
    remaining_pennies = remaining_pennies % PENNIES_IN_SHILLING
    return pounds, shillings, remaining_pennies


def is_palindrome(phrase):
    """Ignoring spaces and capitalisation,
    if the parameter phrase reads the same backwards as forwards,
    return True, else False.

    The parameter phrase is guaranteed to be a string containing only the
    characters [A-Z][a-z] and space.
    """
    # make phrase lower case
    phrase = phrase.lower()
    # remove spaces by replacing them with empty strings
    phrase = phrase.replace(' ', '')
    # make a reversed copy
    phrase_reversed = phrase[::-1]
    # compare for equality and return that value
    return phrase == phrase_reversed


def is_anagram(phrase1, phrase2):
    """Answer `True` if phrase1 and phrase2 are anagrams of each other,
    otherwise answer `False`.

    Spaces and capitalisation are ignored during comparison.
    The parameters phrase1 and phrase2 are guaranteed to be
    type str and only contain the characters [A-Z][a-z] and space.
    """

    # same as before, make lowercase and remove spaces
    phrase1 = (phrase1.lower()).replace(' ', '')
    phrase2 = (phrase2.lower()).replace(' ', '')
    # now sort the characters into the same order
    phrase1 = sorted(phrase1)
    phrase2 = sorted(phrase2)
    # Compare the result for equality.
    # Although they are now lists not strings,
    # the comparison for equality is still valid
    return phrase1 == phrase2


def lucky_fun(lucky_str):
    """Returns a function that accepts a parameter of any type and answers boolean `True`
    if the string representation of the parameter contains the substring lucky_str."""

    def lucky_answer(given_object):
        # convert parameter given object to its string representation
        # and test if lucky_str is a substring
        return str(lucky_str) in str(given_object)

    return lucky_answer
