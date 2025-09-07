


## predict_next(word, filename)

The parameter word is a string with no punctuation or spaces. The `filename` is guaranteed to be the name of
a text file encoded as utf-8. Read the file and provided `word` occurs within it, return the word most
likely to follow `word` based upon the corpus of text within `filename`. If `word` is not present in
filename return `None`.

In this simple case you could just read the next word in `filename` to 'predict' it with 100% accuracy. The
purpose of this exercise is of course more general than that. Imagine that `filename` is a collection of all
the known writings of Arthur Conan Doyle. If we are presented with a new fragment of text purported to have
been written by ACD we could use this function to gain a primitive measure of how likely it is that it
really was written by ACD.

## pluralizer(a_str)

The parameter is guaranteed to be a word. Return the plural of that word.

**Test Data:** Banana, Leaf, Trolley, Lorry, Sheep, Church, Sausage, Monkey, Knife, Child, Match, Poppy

**Hints:**
Given the variability and irregular structure of natural language there is no perfect version of this
function and a balance needs to be struck between coverage and the ever-increasing complexity of the code.



# Difficult Questions
These last questions are more difficult. 

## get_all_words(a_str)   [ simplify this problem ]

The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file, replace all punctuation with a space and write the result to outfile encoded as utf-8. I will test your implementation using 244-0.txt so use that as your baseline for testing.

**Hints**\
This is trickier than it first seems as the answer depends entirely on what is defined as punctuation.
Symbols such as `! ? . ,` are not too problematic but apostrophes and single quotation marks can get confused, as can hyphenated words, words hyphenated for page wrap and hyphens used as a general purpose separator.

Rather than searching through a large outfile looking for 'punctuation' symbols that have slipped through, think about writing a function that puts the words in outfile into a set, then you have a much smaller collection to deal with