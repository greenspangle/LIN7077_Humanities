# LIN7077 2nd assignment
# my answers

def signum(a_num):
    """If a_num is greater than zero, return integer 1.
    If it's less than zero, return integer -1.
    If it is zero, return integer 0."""
    if a_num > 0:  # it's greater than zero
        return 1
    if a_num < 0:  # it's less than zero
        return -1
    # The only option left is that it IS zero
    return 0


def contains_vowel_v1(a_str):
    """If parameter contains one or more of the vowels 'aeiouAEIOU'
    answer `True`, else answer False`."""
    # convert string to lower case so there is no need to check for capitals
    a_str = a_str.lower()
    # check each vowel in turn
    if 'a' in a_str:
        return True
    if 'e' in a_str:
        return True
    if 'i' in a_str:
        return True
    if 'o' in a_str:
        return True
    if 'u' in a_str:
        return True
    # None of the vowels are present in the string, hence return False
    return False


def contains_vowel_v2(a_str):
    """If parameter contains one or more of the vowels 'aeiouAEIOU'
    answer `True`, else answer False`."""
    # convert string to lower case so no need to check for capitals
    a_str = a_str.lower()
    # use logical 'or' to check all thet vowels in a single statement
    if ('a' in a_str
            or 'e' in a_str
            or 'i' in a_str
            or 'o' in a_str
            or 'u' in a_str):
        return True
    # None of the vowels are present in the string, hence return False
    return False


# I prefer version 1 for no other reason than I do
contains_vowel = contains_vowel_v1


def len_longest_2(str1, str2):
    """Return the length of the longest string.
    Both parameters are guaranteed to be strings."""
    len_str1 = len(str1)
    len_str2 = len(str2)
    if len_str1 > len_str2:
        # str1 is the longest
        return len_str1
    # Either str2 is the longest or they are both the same.
    # In either case, return len_str2
    return len_str2


def len_longest_3(str1, str2, str3):
    """Return the length of the longest, or joint longest, string.
    All parameters are guaranteed to be strings."""
    len_str1 = len(str1)
    len_str2 = len(str2)
    len_str3 = len(str3)
    # check if str1 is the longest
    if len_str1 >= len_str2 and len_str1 >= len_str3:
        return len_str1
    # check if str2 is the longest
    if len_str2 >= len_str3 and len_str2 >= len_str1:
        return len_str2
    # and the only remaining option is:
    return len_str3


def len_smallest_3(str1, str2, str3):
    len_str1 = len(str1)
    len_str2 = len(str2)
    len_str3 = len(str3)
    # check if str1 is the smallest
    if len_str1 <= len_str2 and len_str1 <= len_str3:
        return len_str1
    # check if str2 is the smallest
    if len_str2 <= len_str3 and len_str2 <= len_str1:
        return len_str2
    # and the only remaining option is:
    return len_str3


def len_middle_3_v1(str1, str2, str3):
    """Return the length of the intermediate length string.
    The length that is neither the shortest nor longest."""
    len_str1 = len(str1)
    len_str2 = len(str2)
    len_str3 = len(str3)
    # check if len_str2 is midway
    if ((len_str1 >= len_str2) and (len_str2 >= len_str3)
            or (len_str1 <= len_str2) and (len_str2 <= len_str3)):
        # len_str2 is in the middle
        return len_str2
    # check if len_str3 is midway
    if ((len_str2 >= len_str3) and (len_str3 >= len_str1)
            or (len_str2 <= len_str3) and (len_str3 <= len_str1)):
        # len_str3 is in the middle
        return len_str3
    # the only option remaining is len_str1
    return len_str1


def len_middle_3_v2(str1, str2, str3):
    """Return the length of the intermediate length string.
    The length that is neither the shortest nor longest."""
    len_str123 = len(str1) + len(str2) + len(str3)
    len_str123 = len_str123 - (len_smallest_3(str1, str2, str3))
    len_str123 = len_str123 - (len_longest_3(str1, str2, str3))
    return len_str123


def len_middle_3_v3(str1, str2, str3):
    len_str1 = len(str1)
    len_str2 = len(str2)
    len_str3 = len(str3)
    if len_str1 > len_str2:
        biggest_12 = len_str1
        smallest_12 = len_str2
    else:
        biggest_12 = len_str2
        smallest_12 = len_str1
    if len_str3 > biggest_12:
        return biggest_12
    elif len_str3 < smallest_12:
        return smallest_12
    else:
        return len_str3


len_middle_3 = len_middle_3_v3


def isa_triangle(side_1, side_2, side_3):
    """The three parameters are guaranteed to be numbers.
    If they are interpreted as the lengths of the sides of a Euclidean triangle
    return an integer indicating which type of triangle they would construct:
    0 is no triangle possible, 1 is Scalene, 2 is Isosceles, 3 is equilateral."""
    # make all values non-negative, just to be sure
    side_1, side_2, side_3 = abs(side_1), abs(side_2), abs(side_3)
    # and now test
    # Impossible triangle?
    if (side_1 > (side_2 + side_3)
            or side_2 > (side_1 + side_3)
            or side_3 > (side_1 + side_2)):
        # one of the sides is greater than the sum of the other two,
        # hence no triangle is possible
        return 0
    # Equilateral triangle?
    if side_1 == side_2 and side_2 == side_3:
        # all three sides are equal hence equilateral
        return 3
    # Isosceles triangle?
    if side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
        # two sides equal hence isosceles
        return 2
    # after all alternatives have been exhausted, whatever remains must be true,
    # Hence it must be a scalene triangle
    return 1


def score_2(dice_1, dice_2):
    """Calculate the score on the throw of two dice.
    The parameters are guaranteed to be integers between 1 and 6 inclusive."""
    # First bullet: start by adding both dice together
    score = dice_1 + dice_2
    # Fourth bullet:
    if score == 7:  # implies it cannot be a 'double'
        return 14
    # second bullet, and then third bullet within that
    if dice_1 == dice_2:  # it's a 'double'
        score += dice_1  # so add one of the dice again
        if dice_1 == 6:  # it's a double six so add another dice again
            score += dice_1
    # that's all the alternatives checked, so return the score
    return score


def score_4(red1, red2, blue1, blue2):
    """    Calculate the score of four six-sided dice, two blue and two red."""
    # this could be implemented as a single if-elif statement,
    # BUT the best policy is always to keep things as simple as possible
    # so taking the rules one-by-one:
    # rule 1
    if red1 < red2:
        smallest = red1
    else:
        smallest = red2
    if blue1 < smallest:
        smallest = blue1
    if blue2 < smallest:
        smallest = blue2
    score = smallest
    # rule 2
    if (red1 + blue1 == 7
            or red1 + blue2 == 7
            or red2 + blue1 == 7
            or red2 + blue2 == 7):
        score = 7
    # rule 3
    if (red1 + blue1 == 7 and red2 + blue2 == 7
            or red1 + blue2 == 7 and red2 + blue1 == 7):
        score = 14
    # rule 4
    if (red1 == 3 and red2 == 3 and blue1 == 4 and blue2 == 4
            or red1 == 3 and red2 == 4 and blue1 == 3 and blue2 == 4
            or red1 == 3 and red2 == 4 and blue1 == 4 and blue2 == 3
            or red1 == 4 and red2 == 3 and blue1 == 3 and blue2 == 4
            or red1 == 4 and red2 == 3 and blue1 == 4 and blue2 == 3
            or red1 == 4 and red2 == 4 and blue1 == 3 and blue2 == 3):
        score = 21
    # and done
    return score


def isa_leap_year_v1(year):
    """If a year is a leap year in the Gregorian calendar,
    answer True else answer False.
    If a year is an integer multiple of 4 years, then it is a leap year,
    except for years evenly divisible by 100,
    but not by 400.
    The parameter year is guaranteed to be a positive integer. """
    # Simple interpretations of the rules
    if year % 4 == 0:  # divisible by 4 so could be a leap year
        if year % 100 == 0:  # check if div by 100
            if year % 400 == 0:  # it is so check 400
                return True  # divisible by 400
            return False  # divisible by 100 but not 400
        return True  # divisible by 4 but not 100 or 400
    # year not divisible by 4 hence cannot be a leap year
    return False


def isa_leap_year_v2(year):
    """If a year is a leap year in the Gregorian calendar,
    answer True else answer False.
    If a year is an integer multiple of 4 years, then it is a leap year,
    except for years evenly divisible by 100,
    but not by 400.
    The parameter year is guaranteed to be a positive integer. """
    # Reversing the logic makes the code much simpler
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


# I like version 2 best
isa_leap_year = isa_leap_year_v2


def true_date_v1(year, month, day):
    """All three parameters are guaranteed to be positive integers.
    If the date they represent corresponds to a valid calendar date,
    then return True, else return False."""
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    #  now check the individual months
    if month == 1:
        return True
    if month == 2 and day <= 29:
        if day == 29 and not isa_leap_year(year):
            return False
        return True
    if month == 3:
        return True
    if month == 4 and day <= 30:
        return True
    if month == 5:
        return True
    if month == 6 and day <= 30:
        return True
    if month == 7:
        return True
    if month == 8:
        return True
    if month == 9 and day <= 30:
        return True
    if month == 10:
        return True
    if month == 11 and day <= 30:
        return True
    if month == 12:
        return True
    return False


def true_date_v2(year, month, day):
    """All three parameters are guaranteed to be positive integers.
    If the date they represent corresponds to a valid calendar date,
    then return True, else return False."""
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    #  now check the individual months
    if month in (1, 3, 5, 7, 8, 10, 12):
        return True
    if month in (4, 6, 9, 11) and day <= 30:
        return True
    # February (month 2) is the only month remaining to check
    if day <= 28:
        return True
    if day == 29 and isa_leap_year(year):
        return True
    # all other options are False
    return False


# assign the function name true_date to one or other of the above
true_date = true_date_v1
# end #
