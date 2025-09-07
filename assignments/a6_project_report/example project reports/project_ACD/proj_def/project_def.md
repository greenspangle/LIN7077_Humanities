# Peter McGinty - Project Definition

## Project Objectives

I intend to examine the published novels of Arthur Conan Doyle (ACD) for
patterns in letter-frequency, word-frequency, word length, sentence
length and paragraph length - wherever these measures make sense.

The texts I examine will need to be out of copyright (I cannot afford to buy
them) and readily accessible online (I cannot afford to wait for access).
Fortunately (at least for me) ACD died in 1930 and all his published works are
now out of copyright.

If time permits I will compare ACD with other authors and possibly also
different time periods and different languages.

## Data Sources

Although [Google Books](https://books.google.com/) is perhaps the best known,
[Project Gutenberg](https://www.gutenberg.org/ "Project Gutenberg") seems to
be the original source of most text copies of out-of-copyright works and seems
to have an almost full selection of the works of ACD.
That should provide more than enough source material to get started.

Conveniently, all [Project Gutenerg](https://www.gutenberg.org/) books are utf-8
encoded text files.

# Project Iteration 1

In order to keep things simple and 'get started' ASAP, I propose to concentrate
on just one novel and create a generalised set of basic functions that would
seem to be useful for textual analysis.

The functions will include reading and cleaning the file, extracting the text
into a string, breaking it into characters, words, sentences, paragraphs, and
producing some charts of the data.

Iteration 1 is time-limited to just one to two weeks.

## Function Specifications

### file_to_str(filename) -> str

Extract the text of an authors book from a file and __possibly__ do some basic
data cleaning.

The function will assume the contents of filename are UTF-8 encoded text, read
the entire contents, and return the text of the book as a single string.

### get_chars(a_str, filter = None) -> \[ str ]

Extract the characters in a_str for which filter(character)==True.
If filter is none return every character.
Returns the result as a list of characters.

### get_words(a_str, sep = ' ', filter = None) -> \[ str ]

Split a_str at every sep character and return a list of wirds (segments) for
which filter(character)==True.
If filter is none return every word.
Returns the result as a list of words.

### get_sentences(a_str, sep = ' ', filter = None) -> \[ str ]

Split a_str at every sep character and return a list of segments for which
filter(character)==True.
If filter is none return every sentence.
Returns the result as a list of sentences.

### get_paragraphs(a_str, sep = ' ', filter = None) -> \[ str ]

Split a_str at every sep character and return a list of segments for which
filter(character)==True.
If filter is none return every paragraph.
Returns the result as a list of paragraphs.

### get_item_count(\[a_str\]) -> { str:count }

Given a list of strings return a dictionary containing the count of every string
in the list of strings.

As characters, words and sentences are all strings, this function provides count
functionality for all of them.

### remove_punctuation(a_str) -> a_str:

### remove_punctuation(\[a_str]) -> \[a_str]:

Using the string library this is just a specialisation of the get_xxx functions

* get_chars(a_str, lambda x: x not in string.punctuation) or similar

Choice to be made: is punctuation simply removed or is it replaced by a space? I
am inclined to replace it by a space but leave that choice open for now.

### remove_nonprinting(a_str) -> a_str: (or lists)

Same logic as remove_punctuation() but more though needed as non-printing
characters are routinely used to mark paragraph and section boundaries












