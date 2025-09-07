# Functions 
Functions are fundamental to modern programming and is essential you become fully familiar with:

* Creating functions
* Using functions
* Re-using your own functions
* Using the Python Standard Library of functions
* Using function Libraries created by other programmers (later) 

# Section 1 - Getting Started
Creating, using and re-using your own functions.

## Creating Functions

Open a new file in IDLE, save it as f_s1.py, and create the following function
within it:

```python
def two():
    return 2
```

Run the program. Assuming there were no errors there should be no output at the
interactive prompt other than a simple "= RESTART: ...\f_s1.py"

At the interactive python prompt ```>>>``` enter:

```
two()
```

You should get the integer value 2 returned.

If you did then congratulations, your function worked.

If anything else happened then:

* READ THE ERROR MESSAGE.\
  Python error messages are written by the programmers with the intention of 
  helping fellow programmers like you - so read them!.\
  At first they can seem more cryptic than constructive, but you will soon get
  used to them and their ways of speaking to you.
* Edit your program to remove the error(s).
* Test that the new version works.

Now that you have one function working the rest is easy(!)\
Add three more functions to the same python script:

```
def times_2(an_object):
    the_result = an_object + an_object
    return the_result

def times_3(an_object):
    return an_object * 3

def first_last(a_string):
   return a_string[0] + a_string[-1]
```

Execute f_s1.py (press f5 in IDLE) and then at the interactive prompt 
'>>>' enter:

```
dir()
```

This built-in function lists names of the objects in memory.
At the end of the list you should see the names of the functions you have just
created.

Now test the functions ```times_2()``` and ```times_3()``` work.

Type in the name of the function at the python '>>>' prompt with a suitable
value within the parentheses and press 'return'.
Try these examples and check you get the correct result:

```
times_2(7)
times_2(77)
times_2('77')

times_3(7)
times_3(77)
times_3('77 sunset strip')

first_last('LIN6209')
first_last('Linguistics')
```

Test the functions with more values of your own.

## Functions are objects

Everything in Python is an object and that applies just as much to functions as
it does to everything else. This means that functions can be assigned to
variable names.

Add this code to your file:

```
mult_2 = times_2
mult_3 = times_3
```

And check that these names produce the same results.
At the '>>>' prompt try the following:

``` 
mult_2('abc')
times_2('abc')
# and 
mult_2('abc-xyz') == times_2('abc-xyz')
```

Also run ```dir()``` to check that all the names are present in memory.

## Functional composition

You have already done this when you used addition to compose the return vales of
multiple functions as deep within python the arithmetic operators are
implemented as functions.

More explicit examples are given below. Add the following code to f_s2:

```
def times_10(a_value):
    result = times_2(times_5(a_value))
    return result

def times_64(a_value):
    result = times_2(times_2(times_2(times_2(times_2(times_2())))))
    return result
```

## Functional de-composition

Functions can also be used to decompose a complex problem into a collection of
simpler ones.

For instance the problem "write a function that will convert a weight in
stones, pounds, and ounces to the equivalent number of ounces" could be
implemented as single function, but it's probably easier to split it into a
number of simpler functions. The simple functions are also more likely to be
re-usable in other problems.

```
# define some (reusable?) constants for imperial weight conversions
OZ_IN_LB = 16  # constant: ounces in a pound weight
LB_IN_ST = 14  # constant: pounds in a stone weight

def lb_to_oz(pounds):
    """accept pounds weight and return the equivalent weight in ounces"""
    ounces = pounds * OZ_IN_LB
    return ounces

def st_to_lb(stones):
    """accept any weight in stones and return the equivalent in pounds"""
    pounds = stones * LB_IN_ST
    return pounds

def st_lb_oz_to_oz(st, lb, oz):
    """accept any weight is stones, pounds and ounces 
    and convert it into an equivalent number of ounces"""
    st_as_oz = lb_to_oz(st_to_lb(st))
    lb_as_oz = lb_to_oz(lb)
    total_oz = st_as_oz + lb_as_oz + oz
    return total_oz
```

Obviously there are many other ways those functions could have been written, but
it's generally a very good idea to make the logic flow of your code transparent
and obvious, and decomposing a complex function into smaller and simpler parts
does that.
For instance writing all the code on one line is a nice intellectual challenge,
but it generally doesn't win you any friends with other programmers trying to
read your code.

# Section 2 - Re-using Functions

A key strength of functions is that once we have built a function
and confirmed it works correctly, then it can be used a limitless number of
times, safe in the knowledge that it is well tested and its functionality
is well-defined.

So lets re-use the functions we have just written in another python script.

## The ```import``` statement

Create a new python file called f_s2.py in the same folder as f_s1.py
and add the following code:

```
import f_s1  # just the file name, not the .py file extension
# the import statement makes all the functions in f_s1.py visible in this file

def times_5(a_value):
    result = f_s1.times_2(a_value) + f_s1.times_3(a_value)
    return result

def times_8(a_value):
    result = f_s1.times_2(f_s1.times_2(f_s1.times_2(a_value)))
    return result
```

Save the file and run it.

Use the built-in  ```dir()``` to confirm that the library of functions f_s1.py
is in memory.

Use  ```dir(f_s1)``` to confirm that the functions in f_s1.py
are in memory.

Then check they work correctly.

The program in f_s2.py can use the functions in f_s1.py,
provided the name of the function provided their names are prefixed with the
name of the library they were imported from which is f_s1 in this case.
Using the library prefix avoids name clashes which would happen if f_s1 and f_s2
both contained a function with the same name.

# Section 3 - Parameters and arguments

Open a new python file named f_s3.py and add this code:

```
def parms_v1(num1, num2, num3):
    """ there are three parameters """
    return num1 + (num2 * num3)

def parms_v2(num1, num2, num3 = 5):
    """ Third parameter has a default value """
    return num1 + (num2 * num3)
  
# functions are objects hence can be assigned to a variable name
parms = parms_v2
```

Run the file f_s3.py and then test that params_v1() and params_v2() work as
anticipated.
For instance, try executing each of these statements at ```>>>``` :

```
parms_v1(4,5,6)
parms_v2(0, 17, 2)
parms_v2(4,5)
parms_v2(1, num3 = 3, num2 = 11)
parms_v2(num2 = 17, num3 = 2, num1 = 0)

# also try referencing parms_v2 using the name parms:
parms(4,5)
parms(1, num3 = 3, num2 = 11)
parms(num2 = 17, num3 = 2, num1 = 0)
```

Check the values returned to be sure you understand what is happening.

## parameters can be any type of object

Parameter values can be any type of object, even other functions.

```
def parms_v3(an_int = 2, a_str = 'default', a_function = len):
    return a_function(a_str * an_int)
```

In this example the default value of the parameter a_function is the built-in
function len().

Create and save this function in a new python file called params.py

Then execute these calls to the function to confirm it is working correctly:

```
parms_v3(5, '5', int)
parms_v3(5, '5', float)
parms_v3(5)
parms_v3()
```

Try these and explain the results:

```
parms_v3(a_str = 'six', a_function = str, an_int = 9)

parms_v3('six', 6, id)  # throws error, why?
```

Explain the results you get.

# Section 4 - return values

## A function may contain none, one or many return statements

There can be any number of return statements in a function definition.
When the first return statement in the function body is executed then:

* no further code in the function body is executed
* the return values are returned
* the flow of code execution returns to the code that called the function

Try this:

``` 
def two_returns()
    return 'first'
    return 'second'
```

## A return statement can have none, one or many return values

If a return statement returns more than one value, separate them with commas.

Create and save these functions in a python file named f_s4.py

```
def return_single():
    return 'single string value returned'

def return_many():
    return 'as', 'many', 'values', 'as', 'is', 'needed'
```

Execute and test them to confirm your understanding.

## A function always returns a value

If there is no return statement in the function definition or the return
statement is empty then the special value ```None``` is returned.

Create and save these functions in f_s4.py

```
def return_missing():
    pass  # the python statement that 'does nothing'

def return_empty():
    return
```

Execute the python script and test that the functions work.

Determine the type of the values returned by these functions using the built-in
function type()

```
type(return_missing())
type(return_empty())
type(return_single())
type(return_many())
```

Explain the following statements and the values they return:

```
len(return_single())
return_single()[7:12]
len(return_many())
return_many()[2][3]
```

## Functions can return any type of object

This means that functions can create and return other functions.

Add this function to f_s4.py:

```
def nul_points():
    def inner_function():
        return 'zero points'
    return inner_function
```

Execute f_s4.py and then execute the following statements at the interactive
python prompt ```>>>``` and explain the results.

```
f = nul_points()
type(f)    # type of f
type(f())  # type of f()
f()
```

# Section 5 - importing and reusing code

A key strength of functions is that once we have built a function
and confirmed it works correctly, then it can be used a limitless number of
times, safe in the knowledge that it is well tested and its functionality
is well-defined.

So lets re-use the functions we have previously written and tested in another
python script

## The ```import``` statement

Create a new python file called f_s5.py and import the module f_s1.py you
created earlier with the statement:

```
import f_s1   # just the file name, not the .py file extension
```

After running that code in IDLE then evaluate these two expressions:

```
dir()  # the name 'f_s1' is visible
dir(f_s1)  # lists objects in 'f_s1'.
```

Now add the following code to f_s5.py:

```
import f_s1  # just the file name, not the .py file extension
# the import statement makes all the functions in f_s1.py visible in this file

def times_5(a_value):
    result = f_s1.times_2(a_value) + f_s1.times_3(a_value)
    return result

def times_8(a_value):
    result = f_s1.times_2(f_s1.times_2(f_s1.times_2(a_value)))
    return result
```

Save the file and run it.

Use the built-in  ```dir()``` to confirm that the
new functions are in memory and then check they work correctly.

The program in f_s5.py can re-use the functions in f_s1.py,
provided the name of the function provided their names are prefixed with the
name of the library they were imported from which is f_s1 in this case.
Using the library prefix avoids name clashes which would happen if f_s1
and f_s5 both contained a function with the same name.

We can now use these imported objects (functions in this case) in this module,
starter2.py:

```
def times_4(a_value):
    """demonstrate use of imported function"""
    part_1 = f_s1.times2(a_value)
    part_2 = f_s1.times2(a_value)
    return part_1 + part_2

def times_7(a_value):
    pass # you do this

def times_11(a_value):
    pass # you do this
    
def times_144(a_value)
    pass  # you do this
```

Test that your functions work.

## The ```from X import Y``` Statement

This is a variant of the import statement that will import the objects named
in 'Y' from the library 'X' and make them available in the current script
without the need to use any prefix.

Make a copy of f_s5.py and edit to this:

```
from f_s1 import times_2, times_3
# the import from statement makes named functions visible in this file

def times_5(a_value):
    result = times_2(a_value) + times_3(a_value)
    return result

def times_8(a_value):
    result = times_2(a_value) + times_3(a_value) + times_3(a_value) + 
    return result
```

Save the file and run it then use  ```dir()``` to check that the new functions
are in memory and that they work.

## Importing from the standard library

As well re-using your own code you can also import and reuse the enormous amount
of software in the standard library.

Create a file called f_dice.py and use the random library to create the function
dice() which simulates throwing a many sided dice:

```
import random  # from the standard library
def dice(sides=6):
    return random.randint(1,sides)
```

Create a new python script called dice.py and write and test the dice()
function.

Call dice() several times to confirm it only returns integer values between 1 and 6

```
dice()
dice()
dice()
```

Call dice(10) several times to confirm it only returns integers between 1 and 10
```
dice(10)
dice(10)
dice(10)
dice(10)
dice(10)
```

The Random library contains many useful functions. 
In the IDLE interactive shell execute these statements

```
import random
fruits = 'apple pear orange mango melon grape'

random.choice(fruits.split())
random.choice(fruits.split())
random.choice(fruits.split())
random.choice(fruits.split())
```

Explain what is going on.

## Fun with Turtles

Create a new python script and call it turtle1.py and add this fun piece of
code:

```
from turtle import *  # imports everything
def sq(pencolor, fillcolor):
    color(pencolor, fillcolor)
    begin_fill()
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    end_fill()
```

Execute this program and test it works by calling the function sq() at the ```>>>``` prompt:

```
sq('blue', 'green')  # choose any standard color
```

Modify sq() by adding third parameter called ```side``` for the length of the side of the square.

Test your new version of sq().

Modify sq() again by giving all three parameters default values.

Test that this works, perhaps try these statements:
```
sq()
sq(side=50)
sq(fillcolor='pink', side = 77, pencolor='magenta')
```


There are many fun Turtle tutorials on the web.

---

# Practice makes Perfect

The more programming practice you do h better at practice you become.

Go to www.w3schools.com and work through the python functions tutorial.

By now you should be familiar with the content within the following
sections of W3Schools:

[comments](https://www.w3schools.com/python/python_comments.asp)\
[variables](https://www.w3schools.com/python/python_variables.asp)\
[numbers](https://www.w3schools.com/python/python_numbers.asp)\
[type casting](https://www.w3schools.com/python/python_casting.asp)\
[strings](https://www.w3schools.com/python/python_strings.asp)\
[booleans](https://www.w3schools.com/python/python_booleans.asp)\
[operators](https://www.w3schools.com/python/python_operators.asp)\
[functions](https://www.w3schools.com/python/python_functions.asp)

# Even More Practice

There are many other learning and practice resources on the web.
Examples are www.freecodecamp.org and www.realpython.com 
