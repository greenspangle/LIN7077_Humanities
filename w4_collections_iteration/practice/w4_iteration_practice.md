# Practice - Iteration

Collections are iterable. That means that the elements of a collection can be
processed one element at time until the collection is exhausted.
There are two ways in which a collection can be iterated.

2. Using a for loop
1. Using a while loop

Both have features that make them preferable or necessary in particular
circumstances:

**for**

* applicable to any collection, ordered and unordered
* order of processing is unknown and, possibly non-repeatable
* collection cannot be modified while iterating over it
* there is no notion of 'adjacency' between objects

**while**

* the collection must be ordered, and hence indexable
* order of item processing is under direct control
* items in the collection can be replaced with a new object
* items adjacent to the current item can be accessed and modified

The 'for' loop is generally the preferred option as it has a simpler syntax and
is easier to read.

The best of both can often be achieved using the range() function for ordered
collections.

# Iteration using 'for'

## The general form of a `for` loop

Lets illustrate that by creating an instance of the collection type we are most
familiar with, a string, and iterate through it using a `for` loop like this:

```
for each_letter in  'abracadabra':
    # do whatever needs to be done to that item
    print(each_item)
    # etc, etc, 
# end of indentation marks the end of the 'for' loop
```

## Examples:

### Example - counting vowels
Count the vowels and non-vowels in a string. 
First create some variables and initialise their values:

```
vowels, count_v, count_notv = 'aeiou', 0, 0
```
And then iterate through a string, examining one letter at a time.
```
for each_letter in 'abracadabra':
    if each_letter in vowels:
        count_v += 1
    else:
        count_notv += 1
# indentation ended so end of `for` loop
print(count_v, count_notv)
```

### Example - printing just the vowels in a string
Iterate through a string one letter at a time.
If the current letter is a vowel then print it.
```python
for a_letter in 'the quick brown fox jumps over the lazy dog':
    if a_letter in 'aeiou ':
        print(a_letter, end='')
    else:
        print('_', end='')
```

### Example - bumpy up down case
Uppercase, lowercase every alternate character.
```python
switch = True  # this will alternate between True and False
for a_letter in 'the quick brown fox jumps over the lazy dog':
    if switch:  # if switch is True
        print(a_letter.upper(), end='')
    else:  # if switch is False
        print(a_letter.lower(), end='')
    switch = not switch  # flip switch between True and False
```

### Example - adding up a list of numbers
Create a variable to hold the total cost and initialise it to zero.
```python
total = 0
```
Now iterate through the list adding the scores to total
```
for each_score in [20, 25, 17, 3]:
    total = total + each_score

print('My total score is', total)
```

# Iteration using 'while'

## The general form of a `while` loop

```
a_collection = list('abracadabra')
# while loop - generic outline
num_items = len(a_collection)  # get number of items in collection
count = 0  # create a pointer to the current item being processed
while count < num_items:
    # do whatever needs to be done to that item
    print(a_collection[count])
    # etc, etc, 
# end of while loop
```

## Examples:

### Example - counting from 0 upto a number

```
def counting(upto = 10):
    counter = 0
    while counter < upto:
        print(counter)
        counter = counter + 1    
    # end of indented block marks end of while loop
    return
```

### Example - Print just the vowels and spaces in a string:

```
def print_vowels(a_str):
    a_str = 'the quick brown fox jumps over the lazy dog'
    vowels = 'aeiou ' # note the space at end of string
    index = 0
    while index < len(a_str):
        if a_str[index] in vowels:
            print(a_str[index], end = '')
        else:
            print('_', end = '')    
        index = index + 1
```

### Example - Printing the characters of an alphabet:

```
def alphabet_v1():
    char_code = ord('a')
    stop = char_code + 26
    while char_code <= stop:
        print(chr(char_code), end = '')
        char_code = char_code + 1
```

### Example -

The while statement enables us to repeat a block of code until a condition is
satisfied. Try these examples:

```
    def counting(upto = 10):
        counter = 0
        # repeat this while block until 'upto' exceeds 'counter'
        while counter < upto:
            print(counter)
            counter = counter + 1
        return
    # end of indented code marks end of while loop
```

### Example - Print just the vowels and spaces in a string:

```
    def print_vowels(a_str):
        a_str = 'the quick brown fox jumps over the lazy dog'
        vowels = 'aeiou '  # note the space at end of string
        index = 0		
        # repeat while index is less than string length
        while index < len(a_str):
            if a_str[index] in vowels:
                print(a_str[index], end = ' ')
            else:
                print('_', end = '')
            index = index + 1]
```

### Example - Printing the characters of the ASCII alphabet:

``` 
    def alphabet_v1():
        char_code = ord('a')  # gets the code for 'a'
        stop = char_code + 26  # the cosecutive letters of the alphabet
        while char_code <= stop:
            print(chr(char_code), end = '')
            char_code = char_code + 1
```

# Practice Problems for you to solve

Write a function that takes an integer `an_int` as it's parameter and returns
the following values:

1. A list of the squares of all the integer numbers from 0 to `an_int`
2. A list of all the squares that are less than `an_int`

Write functions that accept a string and returns the following:

1. The count of the number of vowels
2. The count of the number of spaces
3. The count of the number of upper case letters
4. Encode and return the string using the caesar cipher (replace every letter
   with the letter three places further up the alphabet, loop back to 'a'
   after 'z' if necessary)
5. Return the number of double-letter pairs there are in the string e.g. 'ee'
   or 'ss' or 'll'
6. The number of times two consecutive vowels occur
7. The number of times two consecutive consonants occur

# A short diversion to Unicode. www.unicode.org

Unicode is a very successful attempt to
represent [every character of every language](https://www.unicode.org/charts/)
in a form that can be represented and
manipulated in a computer. It also now
includes [emoji](https://www.unicode.org/emoji/charts/emoji-list.html).

The examples below print the character sets for Arabic, Bengali, and Ancient
Egyptian Hieroglyphs. You can
find the codes for many other character sets at www.unicode.org/charts/ . NOTE:
the code numbers for the
Unicode characters is
a [HEXADECIMAL](https://en.wikipedia.org/wiki/Hexadecimal) (base 16) number and
not a
more familiar denary (base 10) number. That is a number to base 16 rather than
the usual base 10. Python
understands hexadecimal numbers provided they are prefixed by '0x'. That means
that the hexadecimal number
9e (158 denary, 10011110 binary) is written 0x9e in Python.

``` 
def chars_arabic():
    print('Arabic character set (unicode 0600 - 06ff)')
    code = 0x0600
    stop = 0x06ff
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()
```

```
def chars_bengali():
    print('Bengali character set (unicode 0980 - 09FF) ')
    code = 0x0980
    stop = 0x09ff
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()

```

```
def chars_hieroglyphs():
    print('Egyptian Hieroglyphs character set (unicode  Range: 13000 - 1342F , 1072 characters)')
    code = 0x13000
    stop = 0x1342F
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()
```

Find a character set for your language of choice and write a 'while' routine to
print them out.
Not every character set will have the been installed on Your PC will almost
certainly not have all the
fonts for all thee unicode character sets installed. If the font is missing you
will probably get a list of
small empty rectangles printing instead.  
See the Unicode documentation at www.unicode.org/charts

And other character sets:

```
def alphabet_v2(start_code, stop_code):
    """Get start_code & stop_code from unicode.org/charts. 
    Numbers are hexadecimal so precede number with 0x 
    e.g. alphabet_v2(0x00ff"""
    counter = start_code
    while counter <= stop_code:
        print(chr(counter), end = '')
        counter = counter + 1
    # end of indented code marks end of while loop
    return
```

Try re-writing some of these while loops a for loops. For example:

```
def chars_hieroglyphs():
    print('Egyptian Hieroglyphs character set (unicode  Range: 13000 - 1342F , 1072 characters)')
    code = 0x13000
    stop = 0x1342F
    for code in range(0x13000, 0x1342F):
        print(chr(code), end=' ')
        if code % 32 == 0:
            print()
```

