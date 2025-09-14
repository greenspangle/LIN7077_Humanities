# LIN7077 Assignment #3

Deliver functions that comply with the descriptions below and
pass all the tests in `test_a3.py`.

## robber_lingo(a_str)

The parameter `a_str` is guaranteed to be a lowercase string.

Translate `a_str` into `'rovarspraket'` (Swedish for "robber's language").
That is, double every consonant and place an occurrence of the character `'o'`
inbetween.
For example, `translate("this is fun")` should return the
string `"tothohisos isos fofunon"`

**Hints:**

* A consonant is any character in the alphabet `a..z` that is not a vowel.
* A vowel is any one of `'aeiou'`.
* Create both of those as string variables.
  Might only need one, we can delete the other later if it's not required.
* The problem asks for a string containing the translation so start by creating
  an empty string or list to contain the translation.
* The question asks us to read each character of `a_str` in turn and act
  differently if the `current_char` is a consonant or not.
* Reading each character in turn is iteration and which means we need a `while`
  or a `for` loop.
* If the `current_character` in `a_str` is in `consonants` then
  add `current_character + 'o' + current_character` to the end of the
  translation so far
* If not, just add the `current_character`.

The keyword operator `in` can be used to test if a character is in a string.
Try `'a' in 'syntax'` to see how it works.

Here is some skeleton code you might choose to build on,
or choose your own way:

```python
a_str = 'abracadabra'  # this will be provided by the function parameter
vowels = 'aeioi'
consonants = 'bcdfghjklmnpqrstvwxyz'  # check this is correct (I think it is)
translation = []  # an empty list to contain pieces of the result
for current_char in a_str:  # iterate through a_str one character at a time
    # change the code below to build the translated string
    if current_char in consonants:
        'add translated character to translation[]'
    else:
        'just add character to translation[]'
result = ('join all the parts of the result in translation[] together into'
          'a single string using the string method "str.join(iterable)" ')
# all done so just remains to return the result
```

## char_counts(a_str)

Return the number of vowels, the number of consonants, the number of digits, and
the number of other characters in the parameter string `a_str`.

* A vowel is any character in `'aeiou'` or `'AEIOU'`
* A consonant is any character in [a-z] + [a-Z] that is not a vowel
* A digit is any character in [0-9]
* The 'other characters' are all characters that are neither a vowel nor a
  consonant nor a digit

For example:

|      parameter value       |  return value  |
|:--------------------------:|:--------------:|
|           `'1'`            | `(0, 0, 1, 0)` |
|           `'a'`            | `(1, 0, 0, 0)` |
|          `'aAa'`           | `(3, 0, 0, 0)` |
|         `'rhythm'`         | `(0, 6, 0, 0)` |
| `'aebre? 535 code.3.ibra'` | `(7, 6, 4, 5)` |

**Hints**

* Create four variables to hold the counts of vowels, consonants, digits, and
  other characters and set their value to zero
* Iterate through the characters of the parameter string `a_str`
* For each character determine which category it belongs to and add one to the
  correct running total
* You might find the `in` operator shortens the number of cases you need to
  decide between.

## seq_collections(an_int)

The parameter `an_int` is guaranteed to be a positive integer greater than zero.
Return a tuple containing the integers 1 to an_int inclusive, as a string, a
set, and a list.

* The string must be in ascending order starting from 1, ending with an_int,
  with a single space between adjacent integers, but no space at the beginning
  or end
* The set contains all the integers from 1 to an_int inclusive
* The list contains two sublists
    * The first sublist is all the even integers in 1 to an_int in ascending
      order
    * The second sublist is all the odd integers in 1 to an_int in descending
      order

For example:

| parameter value |                  return value                  |
|:---------------:|:----------------------------------------------:|
|       `1`       |            `('1', {1}, [[],[1]] )`             |
|       `2`       |          `('1 2', {1, 2}, [[2],[1]])`          |
|       `5`       | `('1 2 3 4 5', {1,2,3,4,5}, [[2,4], [5,3,1]])` |

**Hints:**

* Create variables to hold the string, the set, and the list you need to build
* Generate the integer sequence in the range from 1 to `an_int` inclusive.
  There is a built-in function that does this
* Iterate through the sequence of integers and as you do so:
    * Build the string one digit and one space at a time, but don't forget there
      should be no space at the end of the string
    * Build the set in the same way
    * The list is more complicated as you need to decide which sublist to add
      the current integer to.
        * An `if` statement with some integer arithmetic could do this
        * if `n` is even then `n%2` is integer zero which is equivalent to
          Boolean `False`
        * Conversely, if `n` is odd then `n%2` is integer one which is
          equivalent to Boolean `True`

Also remember that:

* You can insert an item into any position in a list or append it onto the end
* You can reverse the order of the elements in a list

## fiddledee_dict(an_int)

The parameter `an_int` is guaranteed to be a positive integer greater than zero.

This function uses a function called `fiddledee()` which you also need to build.

The `fiddledee()` function accepts a single integer which is guaranteed to be
greater than zero and returns a string according to these rules:

* If it is a multiple of 2 return 'Dee'.
* If it is a multiple of 3 return 'Fiddle'.
* If it is a multiple of 2 and 3 return 'FiddleDee'.
* If it is none of those then return the integer as a string.

The `fiddledee_dict(an_int)` function returns a dictionary containing the
integers 1 to an_int as keys associated with the string returned by fiddledee().

| parameter value |                            return value                             |
|:---------------:|:-------------------------------------------------------------------:|
|       `1`       |                             `{1: '1'}`                              |
|       `2`       |                        `{1: '1', 2: 'Dee'}`                         |
|       `3`       |                  `{1: '1', 2: 'Dee', 3: 'Fiddle'}`                  |
|       `6`       | `{1: '1', 2: 'Dee', 3: 'Fiddle', 4: 'Dee', 5: '5', 6: 'FiddleDee'}` |

## char_count_dict(a_str)

Return a dictionary with every character (including spaces and punctuation) in
`a_str` as a key in the dictionary with a value equal to the number of
occurrences of that character in a_str.
Only the characters in a_str are keys in the returned dictionary.

For example:

| parameter values |            return value             |
|:----------------:|:-----------------------------------:|
|       `''`       |                `{}`                 |
|      `'a'`       |             `{'a' : 1}`             |
|     `'aaa'`      |             `{'a' : 3}`             |
|  `'abb ab ab'`   |   `{'a' :  3, 'b' : 4, ' ' : 2}`    |
| `'abracadabra'`  | `{'a' : 5, 'b': 2, 'c': 1, 'd': 1}` |

**Hints:**

* First create a dictionary to contain the result.
  There are several ways to do this but the easiest options are
  probably `d = dict()` which creates an empty dictionary
  and `d = dict.fromkeys(a_str, 0)` which creates a dictionary with a _key_ for
  every character in `a_str` associated with a _value_ of `0`.
* Now that the dictionary exists, iterate through `a_str` and update the count
  associated with each character, adding the character as a key if it is not
  already present.

## word_count_dict(a_str)

Return a dictionary with every word in `a_str` as a key with an associated value
of the number of times that word occurs in `a_str`.

A word is any unbroken sequence of characters in the collection [a-z] + [A-Z].

All characters not in that collection are word separators that mark the boundary
between words.

For example:

|  parameter values   |             return value             |
|:-------------------:|:------------------------------------:|
|        `''`         |                 `{}`                 |
|        `'a'`        |             `{'a' : 1}`              |
|       `'aaa'`       |            `{'aaa' : 1}`             |
| `'ab a ab cde ab'`  |    `{'ab' : 3, 'a': 1, 'cde':1}`     |
| `'jane's escapade'` | `{'jane': 1, 's': 1, 'escapade': 1}` |

**Hints:**

* First create a dictionary to contain the result.
* Decide how you will split `a_str` into words. One way to do this is
    * iterate through `a_str` one character at a time
    * replace every character NOT in [a-z] + [A-Z] with a space
    * use the string method `str,split()` to split a_str into a list of 'words'
* Iterate through the words
* Update the dictionary as you iterate through the words
* Be careful though, the empty string `''` is NOT a word

## isa_pangram(a_str)

A pangram is a phrase that contains all the letters of the alphabet [a-z] at
least once.

Ignore capitalisation, punctuation, spaces, and any other characters in the
phrase.

Answer `True` if `a_str` is a pangram, `False` if not.

For example:

|                   parameter values                    | return value |
|:-----------------------------------------------------:|:------------:|
|    `'the quick brown fox jumps over the lazy dog'`    |    `True`    |
| `'the quick brown fox ?<!>? jumps over the lazy dog'` |    `True`    |
|   `'the quick brown fox jumped over the lazy dog'`    |   `False`    |

**Hints:**

* The question says to ignore capitalisation so a good first step is to
  convert `a_str` to all lower case
* Create a collection containing all the letters of the alphabet
* Iterate through that collection and check that every character is present
  in `a_str`.

Alternatively you could:

* Put all the characters in `a_str` into a set
* Put all the characters of the alphabet into another set
* Create a set that is the intersection of those two sets
* If the intersection set does not contain all the letters of the
  alphabet, `a_str` cannot be a pangram.

## zip_2(str_1, str_2)

**DO NOT use the built-in functions `sorted()` or `zip()` or any python library
while solving this problem**

Both `str_1` and `str_2` have default values of `''` (the empty string) and are
guaranteed to be strings constructed from the alphabet [a-z] with their
characters arranged in normal ascending alphabetical order.

Interleave the successive characters of `str_1` and `str_2` into a new string in
such a way that the characters in the resulting string are maintained in
ascending alphabetical order. Return that string.

For example:

|   str_1    |    str_2     |    return value    |
|:----------:|:------------:|:------------------:|
|    `''`    |     `''`     |        `''`        |
|   `'a'`    |    `'x'`     |       `'ax'`       |
|   `'x'`    |    `'a'`     |       `'ax'`       |
|  `'abc'`   |   `'def'`    |     `'abcdef'`     |
|  `'adf'`   |   `'bce'`    |     `'abcdef'`     |
|  `'ace'`   | `'adfjnoqy'` |  `'aacdefjnoqy'`   |
| `'afgmpt'` | `'adfjnoqy'` | `'aadffgjmnopqty'` |

**Hints:**

* Strings can be indexed:
    * `str_1[0]` is the first character
    * `str_1[1]` the second
    * `str_1[2]` the third and so on.
* Create two index counters/pointers to keep track of where you are in each
  string
* Compare the two indexed characters using a relational
  operator (<, <=, ==, !=, >=, >).
* Add the character lowest in alphabetical order to the new string and increment
  the index counter for that string.
* Repeat until both strings are exhausted.

## zip_n(*strings)

Same rules and conditions as `zip_2()` but this time the function accepts
any number of strings.

For example:

|         parameter values          |     return value     |
|:---------------------------------:|:--------------------:|
|               `''`                |         `''`         |
|               `'a'`               |        `'a'`         |
|             `'a', ''`             |        `'a'`         |
|           `'', '', ''`            |         `''`         |
|           `'a', '', ''`           |        `'a'`         |
|            `'a',  'b'`            |        `'ab'`        |
|      `'abc',  'def', 'ghj'`       |    `'abcdefghj'`     |
|      `'def',  'ghj', 'abc'`       |    `'abcdefghj'`     |
|     `'anx',  'amz', 'bjsuy'`      |   `'aabjmnsuxyz'`    |
| `'anx',  'amz', 'bjsuy', 'cddjy'` | `'aabcddjjmnsuxyyz'` |

**Hints v1:**

* Same pattern as for `zip_2()`
* The difference is that there are now any number of strings instead of two
* Instead of creating individual variables to index the current position in a
  string, create a list of index variables with the same length as the number
  of parameter strings
* That way, the position of the string in the parameter list will be the same as
  the position of the index variable in the list of variables

**Hints v2:**

You have already solved `zip_2()` so use that to iteratively solve this
problem.

* use `zip_2` on the first two strings
* then `zip_2` on the result of that with the third string
* and then the fourth ....

**Hints v3:**

Recursively divide the list of strings into ever smaller lists of strings until
you can apply `zip_2()`.
As the recursion is unwound, successively apply `zip_2()` to the resulting
pairs of strings to solve the whole problem.

## caesar(msg, shift, encode, alphabet)

Since writing was invented people have wanted to keep the content of their
written messages secret.

Thus was cryptography born.

An early encryption algorithm is the so called 'Caesar Cipher'.
Although this algorithm significantly pre-dates Julius Caesar, or any other
Julius we know, tradition insists that we never let facts get in the way of a
good story!

The caesar cipher encrypts a message by substituting each letter in the message
with the letter three characters further up in the alphabet, looping to the
beginning again if we run off the end of the alphabet.

Decryption is the reverse of this process.
Each letter in the 'secret' message is moved three characters down the alphabet
to reveal the plaintext.

Your task is to write a function caesar() that:

* Accepts four parameters. One mandatory and three optional:
    * msg  
      A mandatory string parameter.  
      This is the message to be encrypted/decrypted.

    * shift  
      An optional integer parameter with a default value of three.\
      This determines how far each letter will be shifted during
      encryption/decryption.\
      Positive values are interpreted as shifts UP the alphabet, negative values
      DOWN the alphabet. Large numbers just loop around the alphabet.

    * encode  
      An optional boolean parameter with a default value of `True`.  
      If `encode` is `True` then the message is to be encoded,
      if `False` then it is to be decoded.

    * alphabet  
      An optional string parameter with no duplicate characters and a
      default value of [a-z]+[0-9]+[A-Z]+[.,!?]+[' ']\
      This string contains all the letters of the alphabet to be used
      for encoding/decoding the message.
      If during encoding/decoding a character is encountered that is not in ths
      alphabet then it should remain unchanged.

For example, using the default parameter values:

|                     parameter values                     |  return value   |
|:--------------------------------------------------------:|:---------------:|
|                     'Caesar Cipher'                      | 'FdhvducFlskhu' |
|               'secret msg', encode = False               |  'pb obq,jpd'   |
|               'Caesar Cipher', shift = 17                | 'Trv9r8qTz6yv8' |
|         'Trv9r8qTz6yv8', encode=False, shift= 17         | 'Caesar Cipher' |
| 'eddcbad!', alphabet='fedc bma', encode=False, shift= 17 |   'feed me!'    |

-=- END of ASSIGNMENT #3 -=-
