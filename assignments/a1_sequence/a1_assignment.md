# LIN6209 Assignment #1

Design, build and deliver functions that comply with the descriptions below.

All the python required to build these functions is covered in lectures 1–2.
(So no `if` statements are to be used)

**Remember:** The code you submit for your assignment **MUST** execute.
If your code does not execute on MY PC, then you will score ZERO marks.

## all_ops_part1(int1, int2):

The parameters `int1` and `int2` are guaranteed to be non-zero integers.

This function returns the tuple `( int1 + int2, int1 - int2, int1 * int2,
int1 / int2, int1 // int2, int1 % int2)`

Example test: `assert all_ops_part1(5, 2) == (7, -3, 10, 2.5, 2, 1)`

## all_ops_part2(int1, int2)

Same as all_ops_pt1 but this time with the
operators `<`, `<=`, `==`, `!=`, `>=`, and `>`.

Example test: `assert all_ops_part2(5, 2) == (False, False, False, True, True) `

## lucky_number(a_num)

The parameter `a_num` is guaranteed to be a number.

A lucky number is any number that contains the digit `7` as one of its
(base 10) digits.

If the parameter `a_num` is a lucky number then answer boolean `True`.
If not, then answer boolean `False`.

**Hints:**

* If the argument `a_num` passed to the function was a string then the
  expression `'7' in a_num` would do the job
* But `a_num` not a string, it's a number
* Fortunately, there is a built-in function called `str` that will convert any
  object, including numbers, into its string representation
* Once you have converted the function argument into a string, the first hint
  tells you the code you need for the innards of your function

For example: `lucky_number(3 + 4) # evaluates to True`

## hms_to_s(hours, minutes, seconds)

The parameters `hours`, `minutes`, and `seconds` are each guaranteed to be an
integer number greater than or equal to zero.

Return a duration of `hours`, `minutes`, and `seconds` as the same duration
expressed as a total number of `seconds`.

**Hints:**

* There are sixty seconds in every minute
* There are sixty minutes in every hour

Example test: `assert hms_to_s(0, 0, 0) == 0`
Example test: `assert hms_to_s(100, 10, 1) == 360601`

## s_to_hms(seconds):

The parameter `seconds` is guaranteed to be an integer greater than or equal to
zero.

Covert the time duration `seconds` to the equivalent `hours`, `minutes`,
and `seconds` with `minutes` and `seconds` both in the range 0–59 inclusive.

Return the tuple `(hours, minutes, seconds)`.

**Hints:**

* There are 60 seconds in one minute and 60 minutes in one hour
* The operators `//` and `%` do whole number division and remainder division.
* `4567 // 60` will return the number of 60's (minutes) in 4567 (seconds)
* `4567 % 60` will return the number remaining after 4567 (seconds) has been
  whole-number-divided by 60

Example test: `assert s_to_hms(0) == (0, 0, 0)`
Example test: `assert s_to_hms(360601) == (100, 10, 1)`

## add_hms(hr1, min1, sec1, hr2, min2, sec2)

All parameters are guaranteed to be positive integers and represent two
time durations each expressed as hours, minutes, and seconds.

Answer the sum as a time in hours, minutes, and seconds with minutes and seconds
both in the range 0–59 inclusive.

**Hints:** \
* In the previous two tasks, you created the functions:
    * `hms_to_s(hours, minutes, seconds)  \
      which converts any duration in hours, minutes, and seconds to seconds
    * `s_to_hms(seconds)`  \
      which converts any number of seconds into hours, minutes, and seconds
* To write this new function:
    * use `hms_to_s(hours, minutes, seconds)`  \
      to convert both of the input times to seconds
    * add together both of the times as seconds
    * use `s_to_hms(seconds)` \
      to convert the total seconds back to hours, minutes and seconds

Example test: `assert add_hms(0, 0, 3600, 0, 0, 61) == (1, 1, 1)`

## add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2)

All parameters are guaranteed to be positive integers.

Add two pre-decimalisation amounts of UK currency and return the result in
standard form with shillings < 20 and pennies < 12.

Prior to decimalisation day on 15 February 1971, UK currency consisted of 
pounds, shillings and pence.
Twelve pence made one shilling and twenty shillings made one pound.
Prices were displayed as £5/10s/6d (pronounced as "five pounds ten and six").
See [Wikipedia £sd](https://en.wikipedia.org/wiki/%c2%a3sd) for more info and history.

**Hints:** \
Break the problem into two simpler parts and write two helper functions:

* `old_uk_psp_to_p(pounds1, shillings1, pennies1) -> pennies`  
  This converts any number of pounds, shillings and pence into the equivalent
  number of pennies.
* `old_uk_p_to_psp(pennies) -> pounds, shillings, pennies`  
  This converts any number of pennies into the equivalent number of pounds,
  shillings and pennies.

Then use these two helper functions to
write `add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2)`
in the same way as you did for adding hours, minutes and seconds together.

Example test: `assert add_old_uk(0,19,11,19,0,1) == (20,0,0)`

## is_palindrome(phrase)

The parameter `phrase` is guaranteed to be a string (str) and only contain the
characters [A-Z], [a-z] and spaces.

If, ignoring spaces and capitalisation, the parameter `phrase`
reads the same backwards as forwards return `True`, else return `False`.

**Hints:**

1. Make the phrase all lower-case or all upper case. See `str.lower()`
   and `str.upper()`.
2. Remove spaces. See `str.replace()`
3. Make a reversed copy of the string. See string slicing `str[x:y:z]`
4. Now compare the two strings for equality. See the `==` operator

Example test: `assert is_palindrome('Abba')`
Example test: `assert not is_palindrome('Adele')`

## is_anagram(phrase1, phrase2)

Both parameters are guaranteed to be text strings and only contain the
characters [a-z], [A-Z] and space.

Ignoring spaces and capitalisation answer `True` if `phrase1` and `phrase2` are
anagrams of each other, otherwise answer `False`.

**Hints:**

1. Everything you need is either a built-in function or a string method
2. Make both parameters all upper-case or all lower-case (there is a string
   method for this)
3. Remove spaces by replacing spaces with the empty string (another string
   method)
4. Sort the characters in both strings into the same order (a built-in function)
5. Compare the results with the equality operator

Example test: `assert is_anagram('Dusty', 'Study')`
Example test: `assert is_anagram(' a b   c ', 'ab     c')`
Example test: `assert is_anagram(' ', '     ')`

Example test: `assert not is_anagram('Dusty', 'Books')`
Example test: `assert is_anagram('Dusty', 'Books') == False`

## lucky_fun(lucky_object)

This function accepts any object as its parameter and returns a function.

The returned function accepts a single object of any type as its argument and
answers boolean `True` if the string representation of `lucky_object` occurs
within the string representation of its argument and `False` otherwise.

Example test: `assert lucky_fun(7)(7)`
Example test: `assert lucky_fun('7')(7)`
Example test: `assert lucky_fun(7)('7')`

---
End of assignment

---
