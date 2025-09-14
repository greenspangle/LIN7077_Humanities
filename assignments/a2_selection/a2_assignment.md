# LIN7077 Assignment #2

Deliver functions that comply with the descriptions below and
pass all the tests in `test_a2.py`.

## signum(a_num)

The parameter `a_num` is guaranteed to be a number.

* If `a_num` is greater than zero then return integer one.
* If it's less than zero then return integer minus one.
* If it is zero then return integer zero.

## contains_vowel(a_str)

The parameter `a_str` is guaranteed to be a string.

If `a_str` contains a vowel return `True`, else return `False`.

The vowels are any of the characters in `'aeiou'` or `'AEIOU'`.

**Hints:**

* Look up the operator `in` in the python index and read the documentation
  referenced. Then try using `in` on a few strings interactively.
* To reduce the number of `if` statements you might want to convert the
  parameter string `a_str` to lowercase (or uppercase).
  There is a built-in function that does this.

## len_longest_2(str1, str2)

**Do not use the built-in functions `max`, `min`, or `sorted` to solve this problem**

Both parameters are guaranteed to be strings.

Return the length of the longest of the two strings.

**Hint:**

* There is a built-in function that will tell you the **len**gth of a string.

## len_longest_3(str1, str2, str3)

**Do not use the built-in functions `max`, `min`, or `sorted` to solve this problem**

All three parameters are guaranteed to be strings.

Return the length of the longest.

## len_middle_3(str1, str2, str3)

**Do not use the built-in functions `max`, `min`, or `sorted` to solve this problem**

All three parameters are guaranteed to be strings.

Return the length of the string that is not longer than the longest
and not shorter than the shortest.

## isa_triangle(len1, len2, len3)

**Do not use the built-in functions `max`, `min`, or `sorted` to solve this problem**

All three parameters are guaranteed to be numbers greater than zero.

If they are interpreted as the lengths of the sides of a Euclidean triangle
return an integer to indicate which type of triangle they would construct
according to this table:

| Return Value |       Meaning        |
|:------------:|:--------------------:|
|    **0**     | No triangle possible |
|    **1**     |       Scalene        |
|    **2**     |      Isosceles       |
|    **3**     |     Equilateral      |

**Hints:**

* Triangles have three sides.
* The sum of any two sides must be strictly _**greater**_ than the third.
* If all sides are equal lengths then it's an equilateral.
* If only two sides are equal lengths then it's an isosceles triangle.
* If all three sides are different lengths then it's a scalene triangle

Do remember though that there are *_four_* possibilities.
For example what should `isa_triangle(3,7,3)` return?
If you can't see why a triangle with sides `3, 7, 3` is a problematic triangle
then try drawing it to scale on paper.

## score_2(dice_1, dice_2)

**Do not use the built-in functions `max`, `min`, or `sorted` to solve this problem**

The parameters are guaranteed to be integers between 1 and 6 inclusive and
represent the face values on the throw of two six-sided dice.
Calculate the score according to this rule:

* The score is the sum of both dice
* unless it is a 'double' (both dice the same) in which case add one of the dice
  to the score again
* unless it is 'double six' (both dice six) in which case add both dice to the
  score again
* unless the sum of the two dice is seven in which case double it

For example:

| parameter values | return value |
|:----------------:|:------------:|
|      `1, 5`      |     `6`      |
|      `5, 1`      |     `6`      |
|      `3, 4`      |     `14`     |
|      `5, 2`      |     `14`     |
|      `2, 2`      |     `6`      |
|      `6, 6`      |     `24`     |

**Hints:**

* A few `if` statements with possibly some `elif` and `else`, should get the job
  done.

## score_4(red1, red2, blue1, blue2)

**Do not use the built-in functions `max`, `min`, or `sorted` to solve this problem**

The parameters are guaranteed to be integers between 1 and 6 inclusive.
They represent the face values on the throw of four six-sided dice,
two coloured red and two coloured blue.
Calculate the score according to the rule:

* The score is the face value of the lowest of all four dice
* Unless the sum of any one red dice and any one blue dice is seven in which
  case score 7
* Unless the sum of any one red dice and any one blue dice is seven,
  and the sum of the remaining red and blue dice is also seven,
  in which case score 14
* Unless the four dice are any permutation of (3,3,4,4), in which case score 21

For example:

| parameter values | return value |
|:----------------:|:------------:|
|   `1, 5, 6, 6`   |     `7`      |
|   `3, 2, 3, 3`   |     `2`      |
|   `2, 6, 1, 5`   |     `14`     |
|   `1, 1, 2, 6`   |     `7`      |
|   `1, 2, 3, 4`   |     `1`      |
|   `3, 3, 3, 4`   |     `7`      |
|   `3, 3, 4, 4`   |     `21`     |
|   `4, 3, 3, 4`   |     `21`     |

**Hints:**

* Same again: `if`, `elif` and `else`.
* Just be careful you cover all the permutations and test them.

## isa_leap_year(year)

The parameter `year` is guaranteed to be an integer greater than zero.
If that year is a leap year in the Gregorian calendar answer `True`, else
answer `False`.

**Hint:**

* A year is a leap year if it is an integer multiple of 4
    * Except if it is an integer multiple of 100
        * Except if it is an integer multiple of 400

Alternatively, Wikipedia has a flowchart showing how to determine whether a
year is a leap year or not.
See: [Wikipedia - leap year algorithm](https://en.wikipedia.org/wiki/File:Leap_Year_Algorithm.png)

## true_date(year, month, day)

**Do not use the built-in `calendar` library to solve this problem.**

All three parameters are guaranteed to integers greater than zero.

If the date represented by the parameters `year, month, day` corresponds to a
valid date in the Gregorian calendar then return `True`, else return `False`.
Your function should deal correctly with leap years for which February 29th
is a valid date.

**Hint:**

* Remember the rhyme: 'Thirty days hath September, April, June, ...'
* You wrote a function that determines if a particular year is a leap year, so
  re-use that.
