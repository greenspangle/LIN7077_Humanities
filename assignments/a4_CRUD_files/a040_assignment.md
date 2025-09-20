# LIN7077 Homework #4

Design, build and deliver functions that comply with the descriptions below.

All `filename` parameters are guaranteed to be legal file names and `utf-8`
encoded text.

## temperature_FtoC(temperature)

The parameter `temperature` is a number that represents a temperature on the
Fahrenheit scale. Return the equivalent temperature on the Celsius scale.

To convert a temperature from Fahrenheit to Centigrade,
first subtract thirty-two from the temperature, then divide that result by nine,
then multiply that result by five.

## thermostat(temperature)

If the `temperature` is less that `19` turn the heat on, if it's more than `24`
turn the heat off, and if it's neither, leave the heat setting as it is. Return
the string `'heat on'`, `'heat off'` or `'stet'` respectively.

For example:

| temperature | return value |
|:-----------:|:------------:|
|    `21`     |   `'stet'`   |
|    `16`     | `'heat on'`  |
|    `34`     | `'heat off'` |
|    `19`     |   `'stet'`   |
|    `24`     |   `'stet'`   |

**Hints:**

* A few `if` statements with possibly some `elif` and `else` should get the job
  done.

## read_alternate_chars(filename)

Open the file `filename` and return two **sets** of characters:

* set_1 : the set of the first, third, fifth, and so on, characters from the
  file
* set_2 : the set of the second, fourth, sixth, and so on, characters from the
  file

**Hints:**

* Create two empty sets `set_1` and `set_2` (or whatever names you choose)
* Open `filename` read-only as you do not intend to modify it
* Read the successive characters in `filename` and add them alternately to
  `set_1` and `set_2`
* Return the two sets as the tuple `set_1, set_2`

For example:

| file content |          return value          |
|:------------:|:------------------------------:|
| `'1234567'`  |  `({1, 3, 5, 7}, {2, 4, 6})`   |
|  `'abc123'`  | `({'a', 'c', 2}, {'b', 1, 3})` |

Note: The elements of a set are not ordered which means that the elements in
your sets may display differently. As long as two sets contain the same elements
they are the same set.

## write_ints(filename, an_int)

The parameters are guaranteed to be a legal filename and an integer greater than
or equal to zero.

Create the file and write `an_int` lines to the file.

The structure of each successive line of the file is:

* the `current_integer` in the sequence from `1` to `an_int` inclusive
* the string `' - '` (space - dash - space)
* the sequence of integers beginning with `1 * current_integer` and proceeding
  up to `current_integer * current_integer`, each seperated from the
  preceding one by a space (but no space after the final one)

For example:

| parameter value | file content                                                                      |
|:---------------:|:----------------------------------------------------------------------------------|
|       `0`       | empty                                                                             |
|       `1`       | `1 - 1`                                                                           |
|       `2`       | `2 - 1`<br/>`2 - 2 4`                                                             |
|       `5`       | `5 - 1`<br/>`5 - 2 4`<br/>`5 - 3 6 9`<br/>`5 - 4 8 12 16`<br/>`5 - 5 10 15 20 25` |

**Hints:**

* This feels like a loop within a loop.
    * A `for` or `while` loop to generate the sequence of integers from 1
      to `an_int`
    * and then another `for` or `while` loop within that to generate the
      ascending sequence
      from `next_integer` to `next_integer * next_integer`.

## read_ints_csv(filename)

The file `filename` is guaranteed to be a CSV file  (comma seperated variables)
with variable length records and integer valued fields.

Every record should comply with the constraints that:

* Every record has either zero fields or at least two fields
* The value in the last field of a record must equal the sum of all the
  preceding fields in that record

Open the file, read it, and return `True` if it complies with these constraints
and `False` otherwise.

**Hints**

* There is a module in the python standard library specifically designed to
  read, write, and process CSV files. Find it and use it. It should help you
  greatly.
* Open the file read only and read it a record at a time
* Check that all the field values are integers
    * If any are not then return `False`
* Check that the value of the last field equals the sum of all the preceding
  fields
    * If not return `False`
* If you reach the end of the file without finding any problems, return `True`

## write_random(filename, size, alphabet)

Write `size` random characters from `alphabet` to a file named `filename`.

The parameters are:

* filename: a legal file name with a default value of `'random_chars.txt'`
* size: a positive integer with a default value of `7077`
* alphabet: a string of characters with a default value of `'0123456789'`

**Hints:**

* The `random` library contains functions that select random elements from a
  collection
* Open the file `filename` for write
* Write `size` randomly selected characters from `alphabet` to the file
  called `filename`

## is_alphabetical(a_str)

Do not use the built-in function `sorted()` or `reversed()` or any other Python
sorting feature in your answer to this question.

The parameter `a_str` is a string guaranteed to consist of only lower case
letters from `string.ascii_lowercase`
(see https://docs.python.org/3/library/string.html )
with a default value of `''` (the empty string) which is deemed to be in
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

## deal(an_int):

This function simulates dealing `an_int` number of cards from a shuffled deck of
playing cards. The parameter `an_int` is guaranteed to be an integer in the
range 1 to 52 inclusive with a default value of one.

A set of playing cards consists of 52 individual cards each marked as belonging
to one of four suits (clubs, diamonds, hearts, spades) and one of thirteen face
values (ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, knave, queen, king). The pack contains
no duplicates so every card is unique within its deck.

When called, this function should return a list of `an_int` playing cards with
each card being a tuple containing two strings. The first for its face value and
the second for its suit.

Just like a real deck of cards, the same card cannot be dealt twice on a single
call of `deal()`.

**Hints:**

* The `random` module is part of the python standard library and will do most of
  what you need to write this function.

For example:

| an_int |                        example return value                         |
|:------:|:-------------------------------------------------------------------:|
|        |                                `[]`                                 |
|   1    |                       `[('knave', 'spades')]`                       |
|   1    |                         `[('3', 'clubs')]`                          |
|   2    |              `[('2', 'spades'), ('ace', 'diamonds')]`               |
|   2    |            `[('knave', 'spades'), ('queen', 'hearts')]`             |
|   3    | `[('seven', 'clubs'), ('seven', ' 'hearts'),('seven', 'diamonds')]` |

## ascending(filename, alphabet)

The parameter `alphabet` is a string of characters with no duplicates and has a
default value of `string.ascii_letters`.
Note that `string` is a module in the standard python library and is not
the same thing at all as the `str` module.

The characters in `filename` are NOT all guaranteed to be in `alphabet`.
Any character in `filename` that is not in `alphabet` is a word separator.
Uninterrupted consecutive sequences of characters from `alphabet` in `filename`
are words.

The order of the characters in `alphabet` defines ascending alphabetical order
for this function.
For instance, if `alphabet = 'azbrdvkge'` then the
strings `'aardvark', 'badger', 'zebra'` arranged in `alphabet` order
are `'aardvark', 'zebra', 'badger'`.

Answer two tuples containing the starting position within `filename`
and length of:

* the longest consecutive sequence of characters within `filename` that are
  all in `alphabet`
* the longest consecutive sequence of characters within `filename` that are
  all in `alphabet` AND in non-decreasing order as defined by `alphabet`

If there are multiple such substrings, report the first. If the file is empty
return zeros

For example:

|    file content    | alphabet |   return value   |
|:------------------:|:--------:|:----------------:|
|        `''`        |   `''`   | `(0, 0),(0, 0)`  |
|       `'z'`        |  `'z'`   | `(0, 1),(0, 1)`  |
|     `'ababcb'`     | `'abc'`  | `(0, 6),(2, 3)`  |
|  `'testedresult'`  | `'est'`  | `(0, 5),(1, 3)`  |
|  `'testedresult'`  | `'tse'`  | `(0, 5),(0, 2)`  |
|   `'ababcccdab'`   | `'abcd'` | `(0, 10),(2, 6)` |
| `'zapibracadabra'` | `'abr'`  | `(4, 3),(10, 3)` |

**Hints:**

* This is a more complex problem so rather than try to solve the whole problem
  at once, break it into smaller pieces and try solving a simpler/smaller
  versions first.
* Then, once the pieces are working, you can start assembling them into bigger
  pieces and, eventually, solve the whole problem.
* Perhaps you might:
    * Start by just solving it for a strings, not files
    * Even simpler just work on finding the longest sub-sequence of characters
      in a string that are all in `alphabet`
* Once that is done:
    * Still considering just a string, next work out how to find the longest
      sub-sequence of characters all in the string that are all in `alphabet`
      and in the same order as in `alphabet` with repetitions being allowed (
      which is the same as saying the characters are arranged in non-decreasing
      order)
* Now that you have solved both halves of the problem, wrap both parts into a
  single function, open a file and read it into a string, and you are done.

The code may or may not be very elegant nor very efficient - but get it working
first before you even think about anything like that.

Also:

* It is often very helpful when trying to solve these more difficult problems to
  first try and think how it might be solved with 'paper & pencil'.
* Doing a 'paper & pencil' walk-through of a human-speak solution (yes I
  actually did do that) shows that just one iteration through the list is all
  that is needed but there are several things to keep track of at
  the same time including, at a minimum:
    * the start index of the longest substring found so far
    * the end index (or length) of the longest substring found so far
    * the start index of the longest non-decreasing substring found so far
    * the end index (or length) of the longest non-decreasing substring found so
      far
    * the start index of the current substring
    * the index of the current character being examined
* Your algorithm may be different, and that is fine, and it certainly does not
  matter how many times you iterate through the file.
* Whatever your problem-solving strategy is though I strongly urge you to do a
  walk-through on paper **before** rushing to the computer

