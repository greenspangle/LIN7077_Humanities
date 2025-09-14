# LIN70770 Programming for the Humanities <br/> Lesson 1 = Practice, Practice, Practice...

To successfully complete this module you **_MUST_** have a computer with Python 
and Jupyter installed. How to install Python and Jupyter is described below.

The key to learning any language is to use it.
Every day at every opportunity, read it, write it, think it, and speak it.

Practice, practice, practice. The more practice you do the easier this module 
will be.

Programming is a practical activity so don't just read the examples of code,
sit in front of your PC and get Python to execute it. 
Then experiment with your own variations of the code and confirm to yourself 
that ou really do understand what Python is doing.

The pattern of our weekly lectures will be that the first half is learning
and the second half is all practice.

There is no assignment this week but do not let that lull you into a false 
sense of security. There are six assignments for this module and the first five 
are issued in weeks 2, 3, 4, 5. and 6.

Today we will start by using Python interactively to establish some basics. 
Then we will move to using Jupyter notebooks for exploring and practicing 
Python.

So let's get started on building some vocabulary.


# A foretaste of Python on the web

Go to [Python.org](https://www.python.org/)

Once the Python home page has loaded you will see a window on the screen 
containing the text "# Python 3: Fibonacci series up to n"

* In the top right-hand corner of that window you will see a yellow square with 
  a small black chevron in it.
* Hover the cursor over that yellow square and you will see the message
  "Python Interactive Shell".
* Click on the yellow square to start the python interactive shell.
* When the shell has started you should see the interactive python prompt `>>>`
* Type `print("Hello World")` and press the return key
* Python should respond by displaying `Hello World`
    * If not check your typing and try again
* Congratulations. You have written your first Python Program

# Python at QMUL

The PCs in the PC Labs already have Python installed.

Logon to any computer in the PC Lab and at the DOS / Unix prompt type 'python' 
followed by the enter/return key.
Python will start and present you with its 'interactive shell prompt', 
indicated by three chevrons `>>>`, which indicates it is awaiting your 
instructions - so let's give it some! Type this:

```python
print('Hello World - again!')
```

Later in this lesson we will use IDLE (Interactive Development and Learning 
Environment) which you can start by
typing `idle` at the DOS / Unix prompt and then pressing enter/return.  
IDLE is used for writing larger and more complex programs. 
For now though we'll stick with using the interactive Python prompt `>>>`.

# Numbers and Arithmetic

Start Python and at the interactive shell prompt `>>>`
type this piece of Python code followed by the return/enter key:

```
2 + 2
```

The result should be:

```
4
```

Good to see that Python can do addition!

## Comments  # this is a comment
Professional python programmers add comments to their code to explain what it
is doing. The '#' symbol tells python to ignore everything that follows it on 
that line. 

Try the following snippets of code:
```
2 + 2  # the answer should be 4
```
```python
 # 2 + 2 # nothing happens! Python ignored everything after the first '#'
```

## The Arithmetic Operators: +, -, *, **, /, //, %

Practice using these operators with a variety of numbers until you are 
comfortable with the results you are getting:

```
2 + 3  # addition 
2 - 3  # subtraction
2 * 3  # multiplication
2 / 3  # division
4 / 2  # division always returns a 'floating point' number
```

A few more examples to try:

```
2 * - 2     # '-' is the 'unary negation operator'
2 ** 3      # exponentiation
11 / 2      # division you have already done
11 // 2     # can you work out what this operator is doing? 
11 % 2      # and this one?  Hint: they are compliments of each other
```

Try more examples using // and % until you understand what those operators do.
Read the documentation
at: [Python documentation: numeric-types-int-float-complex](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
to confirm your understanding.


# Python Jupyter at QMUL
Typing in your code at the interactive python prompt soon becomes tedious. So
let's take a look at using Jupyter notebooks to explore Python.

If you are in interactive Python type `exit()` press return.

At the DOS/Unix prompt type `jupyter` and press return. A lot of text will flow 
past on the screen and then Jupyter will start and present in WYSIWYG interface.

Every notebook consists of two types of cell. Markdown cells for comments and 
documentation, and Code cells for python code.

Execute the contents of a code cell by selecting it and then pressing the 'run'
icon.

To get Jupyter to display the result of some code you must us the print() 
function.

Here is more python to learn and execute in your notebook.

## BODMAS / BIDMAS / BEDMAS / PEMDAS etc

Brackets control the order in which operations are done. Try these examples:

Remember, you need to wrap these statements in print() functions if you want 
the Jupyter cell to display the result of the code.
```
2 - 3 + 4
(2 - 3) + 4
2 - (3 + 4)
```

And these:

```
11 // 2 * 2 + 11 % 2
11 // (2 * 2) + 11 % 2
(11 // 2 * 2 + 11) % 2
(2 ** 41 + 2 ** 43) // 1000 % 10  # can you explain result?
```

If the answers python gives you are not 'obvious' then try more examples until 
the results really are obvious.

## The Relational Operators: <, <=, ==, !=, >=, >

In words: less-than, less than or equal, equal, not equal, greater than or equal, and greater than.
Try them out with these examples:

```
5 > 4
5 < 4
4 < 5
5 == 5
4 == 6
4 != 6
5 < 4 == 4 > 5  # is the result of 5<4 equal to the result from 4>5?
5 < 4 != 4 > 5  # is the result of 5<4 not equal to the result from 4>5?
```

# Strings (text)

In Python, pieces of text are called 'strings'.

You can create a string by enclosing some characters within quotation marks.

You can use single quotation marks:

```
'this is a string'
```

Or double quotation marks:

```
"and this is another string"
```

When you want the same quote symbol inside a string as defines it, use the backslash escape character `'\'`.

```
'apple\'s'
```

```
'both \' and " appear within this string'
```

The backslash escape symbol '\' can also print tabs and newlines and other 
'special' characters. Consult the print() function documentation 
(at [www.python.org](https://www.python.org)) to learn more.

There are also two modifiers you can use to affect how a string is constructed.
These are a leading 'f' character and a leading 'r' character:

```
f"this is an 'f' or 'format' {'string ' * 5}."
# it can include expressions and varible names within it
```

```
r"this is a\n 'r' or 'raw' s\tring"     
# backslash '\' escape characters within the string are ignored
```

Evaluate the above two strings without the leading character and see the difference.

Just a couple more examples for now: (this code uses variables which we will study shortly)

```python
s = 'spam'
f_string = f'More {s} and {s} please!'
r_string = r"C:\Users\temp"
a_string = "C:\QMUL\temp"
print(s, f_string, r_string, a_string)
```

__Note:__ It's also possible to define a string using three double or three
single quotation marks. We will not use this feature during this course but, 
just for completeness, here are a couple of examples for you to try:

```
'''this is some text in quotes'''
```

```
"""this is some text in quotes"""
```


## The operators + and * work on strings

```
'Monty' + ' ' + 'Python'
# returns 'Monty Python'
'Spam' + ' and eggs' * 5
# returns 'Spam and eggs and eggs and eggs and eggs and eggs'
```

## The relational operators work on strings

As well as numbers, the relational operators can compare strings and many other 
types of objects. When comparing strings, Python will use alphabetical order, 
unless you ask it not to.

Try these:

```
'a' < 'b'
'a' <= 'b'
'a' != 'b'
'a' == 'a'
'a' != 'a'

'A' < 'a'
'Z' > 'a'
'A' != 'a'
```

Here's a more complex example; can you work out what's happening?

```
'a' < 'b' == 'c' < 'z'
```

# The operator in

This very useful operator tests if a given element is a member of a collection 
and answers `True` or `False` as appropriate.

```
'c' in 'abcdef'

'Monty' in 'Python'

'ME' in 'and now, for something completely different'.upper()
```

# Boolean Truth Values

Boolean logic will be studied in lessons 3 & 4, but for now it will be useful to know that there are only two Boolean
values: `True` and `False`.
Note that these names are spelt with leading capital letters so `true` and `false` are NOT the same thing at all.

You have already seen boolean values being returned when you were exploring the relational operators.

```
4 == 5  # returns False
```

You can use boolean values explicitly in expressions such as these:

```
(4 == 5) == False  # returns True (the brackets are important!)
```

Or even compare booleans to each other:

```
False == False  # returns True

False != True   # also returns True

True > False    # perhaps suprisingly, this also returns True (explained in lectures 3+4)
```

# Variables

Typing in literal values all the time is tedious and error-prone, and litters our programs with
so-called [Magic Numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)#Unnamed_numerical_constants "Wikipedia link").

Also, if the same literal number or string occurs in more than one place in our program
how do we know if the two or more occurrences of the same literal value refer to the same thing
or two or more separate things?

What we need is a way of being able to refer to a value or an expression by a name to avoid confusion over what it
refers to as well as avoiding the tedium of repeatedly re-typing what might be a complex expression multiple times.

We need variables.

> Definition: A variable is the name of an address (location) in memory that contains a value.

> All variable names MUST:
> 1. Begin with a lower case letter or an underscore. (variable names beginning with uppercase letters are reserved for
     Classes and Constants)
> 2. Contain no spaces
> 3. Contain only upper or lower case letters, the digits 0 to 9, and underscore within them.

## Creating Variables

Create a variable by giving it a name and assigning it a value:

```
a = 3
b = 5
```

The variables `a` and `b` now exist, and the values they refer to are 3 and 5 
respectively. The values can now be manipulated by referring to the variable 
names `a` and `b`.

You can find the names of all the variables in memory using the built-in 
function `locals()`.

```python
locals()
# displays a list of all the variable names in memory, with a and b at the end.
```

Here are more examples of syntactically correct statements defining variables:

```python
bananas = 5
cherries = bananas + 17
my_2nd_FAV_number = 1729  # Ramanujan's taxi number
false = True  # confusing but syntactically correct
```

## Using Variables

Using variables with meaningful names makes calculations and equations easier to understand:

```python
oranges_cost_each = 4
oranges_qty_bought = 4
oranges_total_cost = oranges_qty_bought * oranges_cost_each 
```

There are now three variables in memory with `oranges_total_cost` containing 
the total cost of the oranges just bought.

To display the value of a variable just type its name at the interactive prompt.
Python will respond with its value:

```
total_cost
```

In other situations, where the interactive prompt is not available, you can use 
the print() statement like this:

```
print(total_cost)
```

So let's continue our oranges example and imagine that oranges have increased 
from 4p to 6p each. Whats the total bill now? The quantity of oranges has not 
changed so no need to alter that variable. Just reassign `oranges_cost_each` a 
new value of 6 and then do the same calculation again:

```
oranges_cost_each = 6
oranges_total_cost = oranges_qty_bought * oranges_cost_each 
```

Be careful not to confuse the assignment statement ` = ` with the equality 
operator ` == ` as they are definitely not the same. To demonstrate this 
consider the following python statements which are syntactically correct python but obvious nonsense if interpreted mathematically:

```python
a = 1
a = a + 3
```

The meaning of these statements in Python is:

Statement `a = 1`

* Create the variable `a` and assign it the value 1

Statement `a = a + 3`

* Get the value from the memory location that the variable name `a` refers to
* Add 3 to that value
* Store the result of that calculation in the memory location the variable name 'a' refers to, thus overwriting and
  erasing the previous value in that memory location.

When writing programs do give your variables 'meaningful names'.
In other words, give every variable a name that gives the reader (generally you but often me)
a hint as to what the value it refers to represents. For example:

```python
pnds_in_kg = 2.2
weight_in_kg = 729  # weight in kilograms
weight_in_pnds = weight_in_kg * pnds_in_kg  # same weight in lbs
```

For 'throw away' and scratch snippets of code it doesn't matter but for anything you will keep or use again,
or share with other people (e.g. me!), using meaningful names will save you lots of time in your future coding life.
Even though you wrote the code, you tested it, and you got it to work, when you come back to your code 3 months later
(or 3 days!) you will struggle to remember which variables refer to what, what your code does, and what is wrong with
it:

# More about Strings

Remember this:

> Strings are immutable.

Tuck that fact away for now and we will come back to the implications of what 
it means later.

## Creating Strings

You already know how to create a string in python by using quotation marks: 
matching single quotes, matching double quotes, or matching triple quotes.

For example:

```python
single_quotes = 'spam'
double_quotes = "spam"
tri_single_quotes = '''spam'''
tri_double_quotes = """spam"""
```

Having created all these strings containing `spam` lets check them for equality.

```
single_quotes == double_quotes
```

And Python can even compare them all at once

```
single_quotes == double_quotes == tri_single_quotes == tri_double_quotes 
```

## The length of a string

Python has a built-in function called len() that answers the number of 
characters in a string:

```
len('apple pie')  # answers 9
```

## String Indexing

The individual characters of a string can be referenced (indexed) by their 
relative position from the start of the string. 
Remember though that __*computer scientists count from 0*__. 

Create a string variable and practice selecting individual characters from it.

```
a = 'apple'
```

### Counting from the first character at index position 0

```
a[0]  # answers 'a'
a[1]  # answers 'p'
a[4]  # answers 'e'
```

### Do not go past the last index!

```
a[5]  # raises an 'indexError' message
```

### You can also index from the end of the string by using negative numbers

```
a[-1]  # answers 'e'
a[-4]  # answers 'p'
a[-5]  # answers 'a'
```

### But once again, do not go off the end (the beginning!) of the string

```
a[-6]  # raises another 'indexError' message
```

## String Slicing

Taking the logic of indexing a step further, we can slice whole pieces out of the string:

```
a = 'apple'
a[2:4]  # answers 'pl'
a[1:-1]  # answers 'ppl
```

The first index number is the index of the starting position and the second 
number is the index of the character **after** the last character to be 
included in the slice.

You can also use different sized steps to move through the string:

```
a = 'abracadabra'
# start at the beginning, stop one before the end, step every 2nd character
a[0:-1:2] 

# if you just want to start at the beginning and go through to the end
# then you can omit the indices
a[::3]  # select every 3rd character. Answers 'aadr'

# iterate backwards, selecting every third character
a[::-3]  
```

Try a few more example until you feel confident.

## Reassembling strings using string operators

```
a = 'apple'
a[-2:] + a[:2]  # answers 'leap'
```

## Modifying a String (is not possible)

You might think you can do this:

```
a= 'apple pie'
a[2] = 'e'
#  or:
a[2] = a[4]
```

But you can't. Try it and see. Why?

Hint: Read the error message. What is it trying to tell you?
Meta Hint: ALWAYS read error messages!

Hint: Re-read the first sentence of this 'Strings' section and then re-read the 
error message Python gave you.

## String Methods

Every string in python is an object which means it contains both data and code.
The code associated with an object is called its methods.
We can call (execute / run) these methods using the template pattern:

> object_name.method_name(parameters)

Strings have lots of methods. See the Python string documentation at:
[docs.python.org/3/library/stdtypes.html#text-sequence-type-str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

A few examples should suffice to get you going under your own steam:

```
a = 'abracadabra'
a.upper()               # answers 'ABRACADABRA'
a.count('b')            # answers 2
a.isalpha()             # answers True
a.isdigit()             # answers False
a.replace('a', 'z')     # answers 'zbrzczdzbrz'
a.split('b')            # answers ['a', 'racada', 'ra']
a.title().swapcase()    # answers 'aBRACADABRA'
```

Check what is happening by reading the documentation. Try a few other methods 
with strings of your own.

It is very important that you become familiar with the string library.
At the very least, you should know enough to known that when a text processing 
problem arises then a string method to do "that" probably already exists.

# Python's Built-in functions

Python has some very handy functions 'built-in'.
Read the documentation at: [docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

You have already met and used these built-in functions:

```
int()
float()
str()
type()
bool()
len()
```

 There are many other built-in functions. Some are quite technical but the 
ones listed below are handy to know:

```
chr()          # the character of a unicode number, the inverse of ord()
format()       # formatting of strings - better to use an 'f' string
help()         # ask Python for help on something
id()           # every Python object has a unique ID number
input()        # get some input from the console, usually the user
max()          # answers the maximum parameter
min()          # answers the minimum paramater
ord()          # the unicode number of a character, the inverse of chr()
print()        # very handy when debugging!
reversed()     # Try this code:    '_'.join(reversed('spam'))
sorted()       # Try this code:    ''.join(sorted('spam'))
```
Get a list of the names/variables in the various python environments
```
vars(), locals(), globals(), dir()  # answer a list of the names/variables in the various python environments
```

No need to study each of these in detail, but you do need to know they exist for
those occasions when you need them. 
For now just try a simple example or two for each one.
That should be enough to ensure that in future you will 'know' that Python has 
that particular nugget of functionality 'built-in'.

## Interconverting between numbers and strings

Python has some handy built-in functions that convert between numbers and strings:

```
int('5')                # answers the integer number 5
float('5')              # answers the floating point number 5.0 (notice the decimal point)
str(5)                  # answers the string '5'
str(float(int('5')))    # answers the string '5.0'
```



# Some Practice problems for you to try

Use python to determine the following:

* Given two numbers determine the greater one
* Given five numbers determine the smallest one
* Given any integer determine if it is an even number

Create a variable and assign it a string value.

* Count how many characters the string has
* Slice out the 3rd character
* Slice out the 3rd from last character
* Slice the string into two new substrings:
    * one containing all the characters with an even index
    * one containing all the characters with an odd index
* Make the string all lower case
* Remove all spaces from the string
* Count the number of `'a'` characters in the string (answer is an integer value)
* Check if the character `'a'` occurs in the string (answer is a boolean value)
* Sort the characters of the string into ascending order
* Sort the characters of the string into descending order
* Reverse the characters in the string
* Split the string at every occurrence of the character `'a'`
* Replace every occurrence of the character `'n'` in the string with `'_\n_/n_'`

# Homework = Practice practice practice.

## Install Python on your laptop
Go to [Python.org](https://www.python.org) and download the Python installer. 
Install Python on your laptop and **TEST THAT IT WORKS!**

## Install Anaconda on your laptop
Go to [Anaconda.com](https://www.anaconda.com) and download the Anaconda 
installer. Install Anaconda on your laptop and **TEST THAT IT WORKS!**

### Go to [snakify.org](https://snakify.org/en/) and create an account.

You should be able to do all the exercises in the sections:

* Input, print and numbers
* Integer and float numbers
* Strings (except the last one 'delete every third character')


