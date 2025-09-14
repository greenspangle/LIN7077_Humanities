# Programming for the Humanities

# Weekly Lesson Topics

## Week 1: Getting Started

This week you will start learning the programming language Python,
AND
you should start thinking about what your programming project will be.

Your programming project can be about anything you want,
which is both exciting and probably more than a little daunting.
Nevertheless, by the end of week six,
you will need to have written a detailed project proposal
which you will deliver during weeks seven to twelve

It may seem too early to think about this now, but it is important to start now
so that you can refine your ideas for your project as we learn Python.

### Tasks for this week:

* Install Python on your computer
* Create an account at Anaconda.com
* Create an account at JetBrains.com
* Create an account at GitHub.com
* Write a Python program
* Save your program to a file

### Learning about Python:

* Syntax errors and debugging
* Values
* Variables
* Functions
* Objects and object types
    * Text: str()
    * Integer numbers: int()
    * Floating point numbers: float()
    * Truth values: bool()
* Operators
    * +, -, *, /, //, %
    * <, <=, ==, !=, >=, >

## Week 2: Functions

A function is a named block of code that performs a specific task.

* Name
* Parameters
* {'hidden' internal code}
* Return value

A function is a **REUSABLE** block of code that performs a specific task.

* Saving and reusing your own functions
* Reusing functions from the Python standard library
* Reusing functions from the python package index (pypi.org)

Testing that your functions do what you say they do!

* Informal testing
* The assert statement
* The unittest library
* The pytest library

## Week 3: Conditional execution

### Boolean logic

* The values `True` and `False`
* The operators `and`, `or`, and `not`
* Truth tables

### The conditional keywords

* `if`
* `else`
* `elif`

Testing & TDD (test driven development)

## Week 4: Collections, Iteration, & Recursion

### Collection Types

* String
* List
* Tuple
* Set
* Frozenset
* Dictionary
* and more …

Collections can be

* Ordered or Unordered
* Mutable or Immutable

### Iteration

Working through every item in a collection one item at a time.

Python has three keywords for this:

* `for`
* `while`
* `break`
* `continue`

### Analysis of collections

Count, mean, mode, median, skew, and many statistical measures

### Recursion

Functions that call themselves.

* Unfold, Fold, Map
* Ana- and Cata- morphisms

## Week 5: Files

Files are 'persistent'. That is, they continue to exist even after the computer storage
device has been shut off and restarted sometime later.

In general, a file is an ordered collection of binary bits,
but as we will only be dealing with text files,
we can consider them to be ordered collections of characters.

Files can be:

* Created
* Read
* Updated
* Deleted

CRUD for short.

The two built-in functions for files are:

* open()
* close()

For safety, it is good practice to use these only within the `with` statement.

## Week 6: Introducing your project

Be prepared to present your project proposal to the class.

It does not have to be the final polished version,
but it should be a good starting point, and it will be good for you to get feedback.

This week we will also review some of the tools you will (probably) need to write your project.

### Machine Learning
 TODO

### Natural Networks
 TODO

### IDEs

* PyCharm (JetBrains)
* Spyder
* IDLE
* Visual Studio Code

### Jupyter notebooks

* Mix code, text and graphics
* Editable
* Executable
* A readable document that makes your work look good

### Python Libraries

* Pandas
  A ‘data analysis and manipulation tool, built on Python’
* Numpy
  ‘The fundamental package for scientific computing with Python’
* MatPlotLib
  A plotting library for Python and its numerical extension NumPy
* Seaborn
  A high-level interface for drawing attractive and informative statistical graphics

## Week 7: Reading Week: Designing your project

Getting your data:

* gutenberg.org
* corpusdata.org
* talkbank.org
* Beautiful Soup library
* kaggle.com

### Using AI
Two things that AI can be very helpful with:
* Refining your project ideas
* Helping you write your code

Every software developer uses AI when working on a programming project, and so should you.

## Week 8: Agile Software Development

The Agile Manifesto was written in 2001 by seventeen 
independent-minded software practitioners. 
While the participants didn’t often agree, 
they did find consensus around four core values.


### The Agile Manifesto

https://agilemanifesto.org/ and https://agilealliance.org/

"We are uncovering better ways of developing software by doing it 
and helping others do it. Through this work we have come to value:



* **Individuals and interactions** over processes and tools
* **Working software** over comprehensive documentation
* **Customer collaboration** over contract negotiation

* **Responding to change** over following a plan

That is, while there is value in the items on the right,
we value the items on the left more."


TODO = everything after this point...

## Week 9: Data, Databases, SQL

Data
Structured
Unstructured
Databases
What is a database?
Why use a database?
Types of databases:
Relational, Hierarchical, Object, Unstructured, in-memory, distributed
Relational Databases
SQL – structured query language
The language of relational databases
SQL
DDL data definition language
DML data manipulation language

## Week 10: Project reviews and guidance

Ego-less software development
Respectful software development

Project proposal presentations
Set-up = 2 minutes
Presentation = 3 minutes
Q & A = 3 minutes
Wrap-up = 1 minute
Tear-down = 1 minute
Fail fast, learn fast, succeed early
Short iterations
Clear goals and deliverables
Categorise as: Must, Should, Maybe
Test early and often
Expose to critical review
Recast, and reiterate

## Week 11: Regular Expressions

What is a regular expression?

The RE library

Meta-characters
`. ^ $ * + ? { } [ ] \ | ( )`

`.` Any character except a newline\
`[ ]`  Character class\
`^` Compliment of class\
`\` Backslash\
`*` Zero or more times\
`+` One or more times\
`?` Once or zero times\
`{m, n}` At least m times and at most n times\
`|` Logical OR\
`^` At the beginning of a line\
`$`    At the end of a line\
`()`    Grouping\
`\A` At the start of a string\
`\Z` At the end of a string\
`\B` At a word boundary\
`\b` Inside a word\
`(?= …)` Positive lookahead assertion\
`(?! …)` Negative lookahead assertion\

## Week 12: IT topics it’s good to know about, especially for interviews and impressing potential employers

* GIT & GitHub
* Scikit-learn
* TensorFlow
* ST
* NLTK
* Java, JavaScript, C, C++, C#, verylonglist
* Compilers and interpreters
* Compiler compilers
* ANTLR, GNU Bison, JavaCC
* Defining and building languages
* Cloud technologies and services
* IaaS, PaaS, SaaS
* IoT – internet of things
* Big data, Hadoop
* Machine learning and artificial intelligence
* Training, production, drift
* Limitations
* Chatbots
* Sentiment analysis
* Security – cyber, physical, social
* people are always the weakest link
* Opportunities & Jobs

