## word_frequency(filename)

Return a dictionary with every word in filename as a key and the associated value the number of its
occurrences with filename.

**Hints:**

* Isolate the words
* Use your function `count_words(filename)` for each word you put in the dictionary.

## average_word_length(filename)

The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and return the
average length of the words in the file. The average length is calculated as the (sum of the lengths of
every word) / (number of words). <br/>For example:

| file content           | return value  |
|------------------------|---------------|
| `''`                   | `0`           |
| `'abd def xyz'`        | `3`           |
| `'a bc def '`          | `2`           |
| `'Andover and shandy'` | `float(16/3)` |

**Hints:**\
Count the number of words and sum their lengths then calculate the arithmetic mean of their lengths. Be sure
to guard against division by zero.

## adjacency(filename)

The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and return a
dictionary containing every word as a key.\
Associated with each key are two lists:

* The words that have occurred immediately **before** the key word in `filename`
* The words that have occurred immediately **after** the key word in `filename`

## get_all_non_ascii(filename)

The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and return the set
of all non-ASCII characters present in the file. A non-ASCII character is one for which ord(character)
returns a value of outside the range 0-127 decimal.
