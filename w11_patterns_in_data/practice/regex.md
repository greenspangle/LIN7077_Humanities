# Regular Expressions
Start with MS Word 'search & replace' as that is a close model and easier to get started with

## Using regular expressions in MS Word

MS Word has the standard 'search and replace' features you might expect to find an any word processor, but
it also has and 'advanced' option that is much more capable.

### Given any piece of text find the occurrences of:

1. The occurrences of the text ‘and’
2. The text ‘s_s’ where _ is a vowel
3. Every digit that is followed by a letter
4. Words that begin with ‘s’ and end with ‘t’
5. Words that contain two adjacent vowels
6. Find every word that ends with a question mark
7. Words that begin with a letter, three digits,a dash ‘-’, and then two digits e.g. A123-45
8. Find ‘fruit’ and transpose it with the immediately following word

**Test with this text:**  
The quick? sassy brown fox and the lazy dog sat and looked at each? ?other and the dog barked A456-11 and
789bcd! 321?BBD!! and foxy said fruit and nuts to you? while the band played on and on until they agreed a
settlement

For hints & tips
see [wordmvp.com/FAQs/General/UsingWildcards](https://wordmvp.com/FAQs/General/UsingWildcards.htm)  
Answers at the end of this document

## Searching strings with the re library

```python

import re
a_str = 'foo123bar'
re.search('123', a_str) 
# <re.match object; span=(3, 6), match='123’>
a_str[3:6]
# ‘123’

# using metacharacters
re.search('[0-9][0-9][0-9]', a_str) 

# or, even better
re.search('[0-9]{3}', a_str)

# ints must be consecutive, run the same code with a_str = t
t= 'a12ccccc34a' 

```

### Greedy and Lazy Quantifiers

```

<.*>
# this regular expression will consume everything from the first ‘<‘ to the last ‘>’

<.*?>
# this one will consume everything from the first ‘<‘ to the first following ‘>’ 

```

### More problems to try in [pythex.org](https://pythex.org/)
Create a suitable piece of text to work with and then search for the following:

1. A vowel
2. A lower case letter followed by an upper case letter
3. A capital letter followed by at least 2 lower case letters
4. The letter sequence any vowel, any letter, any vowel
5. A valid Python variable name
6. A binary number (consecutive zero’s and one’s)
7. A hexadecimal number (digits are 0123456789abcdefABCDEF)
8. The letter sequence ‘a’, followed by any letter, followed by ‘a’
9. An email address

### Compiling Regular Expressions
Execute this code in the interactive python shell? 

```python

import re
p = re.compile('abc')
p.search('zzzabcqqq')
# <re.Match object; span=(3, 6), match='abc'>

```


# Answers to MS Word Q

### Given any piece of text find the occurrences .....
The search strings are:

1. and
2. s\[aeiou]s
3. \[0-9]\[a-z,A-Z]
4. <s*t\>
5. \[aeiou]\[aeiou]
6. <\[a-z]{1,}\\?
7. <\[a-z,A-Z]\[0-9]{3}-\[0-9]{2}>
8. Answer in two parts:
    1. Find string: (<fruit\>)[ ](<*\>)
    2. Replace string: \2 \1


