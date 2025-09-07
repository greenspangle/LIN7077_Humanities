## stemmer(a_str)

The parameter is guaranteed to be a word. A string with no spaces.

Industry Industries Industrial Industrious industrialise Industrialist Industrialising Industrialised
Industrialisation Deindustrialised Post-industrial Reindustrialised Unindustrialised

## get_all_words(infile, outfile)

The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file, replace all
punctuation with a space and write the result to outfile encoded as utf-8. I will test your implementation
using 244-0.txt so use that as your baseline for testing.

**Hints**\
This is trickier than it first seems as the answer depends entirely on what is defined as punctuation.
Symbols such as `! ? . ,` are not too problematic but apostrophes and single quotation marks can get
confused, as can hyphenated words, words hyphenated for page wrap and hyphens used as a general purpose
separator.

Rather than searching through a large outfile looking for 'punctuation' symbols that have slipped through,
think about writing a function that puts the words in outfile into a set, then you have a much smaller
collection to deal with

## get_all_non_ascii(filename)

The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and return the set
of all non-ASCII characters present in the file. A non-ASCII character is one for which ord(character)
returns a value of outside the range 0-127 decimal.
