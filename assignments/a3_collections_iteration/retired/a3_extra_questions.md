## robber_lingo(a_str)

Translate the text string `a_str` text into `'rovarspraket'` (Swedish for "robber's language").
That is, double every consonant and place an occurrence of the character `'o'` inbetween.
For example, `translate("this is fun")` should return the string `"tothohisos isos fofunon"`

**Hints:**

* A consonant is any character in the alphabet `a..z` that is not a vowel. A vowel is any one of `'aeiou'`.
* Create both of those as string variables. Might only need one, we can delete the other later.
* The problem asks for a string containing the translation so start by creating an empty string to contain
  the translation.
* The question asks us to read each character of `a_str` in turn and act differently if the `current_char`
  is a consonant or not.
* Reading each character in turn is iteration and which means we need a `while` or a `for` loop.
* If the `current_character` in `a_str` is in `consonants` then
  add `current_character + 'o' + current_character` to the end of the translation so far
* If not, just add the `current_character`.

The keyword operator `in` can be used to test if a character is in a string.
Try `'a' in 'syntax'` to see how it works.

Here is some skeleton code you can build on:

```python

a_string = 'abracadabra'  # this will be provided by the function parameter
vowels = 'aeioi'
consonants = 'bcdfghjklmnpqrstvwxyz'  # check this is correct (I think it is)
translation = []
for current_char in a_string:
    pass  # change this to the code that will build the translated string
if current_char in consonants:
    'add translated character to translation'
else:
    'just add character to translation'
```

When the `for` loop exits return the translated string.

## times2_dict(an_int)

The parameter is guaranteed to be a positive integer greater than zero.

Return a dictionary containing the integers 1 to an_int as keys, all associated with a value of twice the key.

| parameter value |           return value            |
|:---------------:|:---------------------------------:|
|       `1`       |             `{1: 2}`              |
|       `2`       |          `{1: 2, 2: 4}`           |
|       `5`       | `{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}` |

**Hints:**

* Create an empty dictionary.
* Iterate from 1 to `an_int` adding the key:value pairs one at a time



## letter_seq_count(a_str, seq_len, alphabet)

The parameter values are guaranteed to be:

* `a_str` : A string
* `seq_len`: An integer with a default value of 2
* `alphabet`: A collection of characters with a default value of [a-z]

Answer a dictionary that contains all the letter sequences of length `seq_len`
within the string `a_str` that contain
consecutive characters from the alphabet `alphabet` as its keys with an
associated value of the number of times that
sequence occurred in the parameter string `a_str`.

Characters in `a_str` that are seperated only by characters not in `alphabet`
are to be regarded as adjacent.

For example:

|         parameter values          |                      return value                       |
|:---------------------------------:|:-------------------------------------------------------:|
|               `''`                |                           {}                            |
|          `'silly billy'`          | `{'si':1 , 'il':2 , 'll':2 , 'ly':2 , 'yb':1 , 'bi':1}` |
|     `'silly billy', 2, 'ill'`     |              `{'il':2 , 'll':2 , 'li':1}`               |
| `'silly billy', alphabet = 'ill'` |              `{'il':2 , 'll':2 , 'li':1}`               |
