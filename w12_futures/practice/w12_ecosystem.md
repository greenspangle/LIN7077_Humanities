# The Python and IT ecosystems

## f strings

Introduced in Python 3.6 fstrings are a convenient (and efficient) way of formatting strings.
See https://docs.python.org/3/reference/lexical_analysis.html#index-25 for details.

Suppose your program uses an integer variable `age` which has a current value of 27, and you want to create
the string `'You are 27 years of age'`.

```python

age = 27
#  Rather that having to write something like
str_1 = 'You are ' + str(age) + ' years of age'
print('string 1 =', str_1)

# using an f string it's just
str_2 = f'You are {age} years of age'
print('string 2 =', str_2)

# you can even do calculations within the f string
str_3 = f'You have been able to vote for {age - 18} years'
print('string 3 =', str_3)
```

Try a few examples yourself:

```python

# A room is 3m wide and 5m broad 
width, breadth = 3, 5
# using an f string, create a string stating its dimensions and area

message_1 = f'The room is ?? metres wide, ??? meters across and has an area of ???? square metres'
print(message_1)


# working out my pay
# I work 15 hours at £12 per hour less £11 national insurance and tax at 20% on the remainder
hourly_rate, hours_worked, nat_ins, tax_rate = 12, 15, 11, 20

message_2 = f'This week I worked ?? hours at £?? per hour for a gross pay of £??.'
message_3 = 'My deductions were £?? for national insurance and ?? for tax leaving me with a net pay of £??'
print(message_2)
print(message_3)

# and try a couple of your own examples

```

## Documenting your programs

Ever tried using software without any instructions or help? Not always easy. Now imagine trying to
amend someone else's code without any documentation or information about how the code works, or what it
does, or even is supposed to be doing. Even less easy.

Documentation is important because **most developers spend most of their time fixing and enhancing other
peoples code**.

Code is difficult enough to read and understand at the best of times. Trying to find bugs in software of
anything more than trivial complexity is a serious intellectual exercise. If the code is unfamiliar and
poorly documented that can rapidly become a mind twisting experience. Fixing undocumented or, perhaps worse,
incorrectly documented code is in another league beyond that. It's often quicker to throw it away and write
it again from scratch rather than attempt to fix an impenetrable jungle of code.

At a minimum your code should be documented with:

* meaningful object names
* informative in-line comments
* docstrings

### Object Names

The name of an object should give the reader a good clue about what type of object it is and what data it
will contain or function it will perform.

```python

x, y, z = 0, 0, 0  # meaningless names = bad
height, width, depth = 0, 0, 0  # informative names = good

```

### In-line comments

Say what the code is doing without saying the trivially obvious, you are after all talking to another
programmer.

```python

cost, profit, tax = 17, 8, 5
price = cost + profit + tax  # add cost and profit and tax and assign to price = pointless verbiage!

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8.9]]
# matrix_1 is a list of lists. The outer list contains the rows of the matrix. The inner lists each contain the elements of a particular row.
flat = [element for row in matrix_1 for element in row]  # flatten the matrix into a single list of elements

```

### Docstrings

Ideally, your functions should contain an explanation of what they do.

```python

def magic7():
    """ This function takes no parameters and returns the integer value 7.
    
    This is the 'docstring' that provided users of this function helpful information.
    It is ALWAYS good practice to include one.
    blah blah dee dah dah blah
    """
    return 7


# execute the above in IDLE and then run
help(magic7)
# Voila! Your functions are now integrated into the Python help system :-) 

```

You should also develop the habit of placing a docstring as the first item in your modules, classes
and class methods - for exactly the same reasons. For example, run the following few lines of code in IDLE which use packages from the standard library

```python

# let's have a look at fractions
import fractions

help(fractions)
help(fractions.Fraction)
a=fractions.Fraction(3,8)
help(a)

# and perhaps
import string

help(string)

```

## Try - Except

For when things go wrong.

When Python encounters a problem it cannot fix it "raises an exception". This exception object cascades 
upwards through the code stack. If exception object is not "caught" before it gets to
the top of the call stack then the program crashes.

Possible reasons an exception may occur: user enters "wrong" sort of data (wrong leaves??), attempts to divide by zero, attempts
to read a file that does not exist, and so on.

```python

# Get user input: The simple but fragile version
def get_num_v1():
    a_float = float(input('input a number: '))
    return a_float

# run this function a few times to determine how well it works and how robust it is.

# when it asks you to 'input a number: ' what happens if you enter 'seven'?
```

Here's a better way of doing it:
```python

# Get user input: the robust version
def get_num_v2():
    input_ok = False  # keep asking the user for input until this is True
    while not input_ok:
        try:
            user_input = input('input a number')
            a_float = float(user_input)
            input_ok = True  # input is good so exit the while loop 
        except ValueError as err:
            #  caught a ValueError which means the user must have entered
            #  text that cannot be converted to a float number
            print(f'You entered {user_input} which is not a number. Try again...')
    return a_float

```

Another example with a potential divide by zero error

```python

def reciprocal(a_num):
    """Answer the reciprocal of the parameter a_num.
    
    If the parameter is zero then return zero.
    All other incorrect inputs will return 27
    """
    try:
        inverse = 1 / a_num
    except ZeroDivisionError as z_err:
        print(f'Caught the exception    {z_err}    and will now deal with it')
        # Normally reciprocal of zero is undefined
        # This function will return zero
        inverse = 0
    except Exception as z_err:
        print(f'Caught the exception    {z_err}    and will now deal with it')
        # for all other exceptions return 27
        inverse = 27
    return inverse

```

Your application does not have to deal with the exception as soon as it is raised, as long as the exception
is caught somewhere, your application will be robust.

## Classes

Defining your own objects

Numbers, lists, sets, strings are different types of objects. Each of these object types has many methods particular to
themselves and the may treat the same operator symbol differently. For exmple the operator ‘+’ behaves differently for numbers and strings.

You can create your own types of objects by defining a Class for each different type.

Starting with a simple example lets define a Class called Door that manufactures door objects. Every door can be a different height and colour.

```python

# Define a class that returns door objects
class Door1():
    def __init__(self, color='beige', height=2000.0):
        self.__color = color
        self.__height = height

    def set_color(self, color):
        self.__color = color

    def set_height(self, height):
        self.__height = height

    def __str__(self):
        # this is a special dunder function
        # given a door object it returns a string
        return f'This door is colored{self.__color} door and is {self.__height} high'


# and create a few doors
door_1 = Door1('red', 2)
door_2 = Door1('blue', 2.2)
print(door_1, '\n', door_2)
# make the red door polkadot
door_1.set_color('polkadot')
# and check it has changed
print(door_1, '\n', door_2)


# Door attributes and methods beginning with double underscores are PRIVATE
# they exist only with the object and cannot be accessed from outside the object.
# There is a way around this restriction, but it is VERY BAD PRACTICE to do so!

# print(door_1.__height)  # this code will throw an exception!!!

```

We can improve the class Door so that doors have a width and thickness as well as a height. We might also decide that they have an inside face as well as an outside face which can, if we want, be painted different colours:

```python

# Define a class that returns door objects with two faces and edges
class Door2():
    # instantiate a door object
    def __init__(self, color='beige', height=2000, width=900, thickness=35):
        self.__inside_color = color
        self.__outside_color = color
        self.__height = height
        self.__width = width
        self.__thickness = thickness

    # set attribute values
    def set_color(self, color):
        self.__inside_color = color
        self.__inside_color = color

    def set_inside_color(self, color):
        self.__inside_color = color

    def set_outside_color(self, color):
        self.__outside_color = color

    def set_height(self, height):
        self.__height = height

    def set_width(self, height):
        self.__height = height

    def set_thickness(self, height):
        self.__height = height

    # get attribute values
    def get_color(self):
        return self.__inside_color, self.__outside_color

    def get_inside_color(self):
        return self.__inside_color

    def get_outside_color(self):
        return self.__outside_color

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    @property  # convert method to a property
    def get_thickness(self):
        return self.__thickness

    def get_area(self):
        face_area = self.__height * self.__width * 2
        edge_area = (self.__height + self.__width) * 2 * self.__thickness
        return face_area + edge_area

    def __str__(self):
        return f'This door is colored {self.get_inside_color()} inside and {self.__outside_color} outside and and has a surface are of {self.get_area()} square millimeters'


# and create a few doors
red_door = Door2('red', 2)
blue_door = Door2('blue', 2.2)
print(red_door, '\n', blue_door)
# make the red door scarlet
red_door.set_outside_color('polkadot')
# and check it has changed
print(red_door, '\n', blue_door)

```

## Scripts, Modules and Packages
Save this code in a script named 'module1.py'
```python

def f1(a_str = ''):
    return f'This is function f1 in module1 being called with its parameter value = {a_str}'
```

and save this code in a script named 'module2.py'

```python

import module1
def f2(a_str = 'spam'):
    return f'This is function f2 in module2 with a parameter value of "{a_str}" calling function f1() in module1 with a parameter value of "{a_str}". The result returned is: {module1.f1(a_str)}'
```




## Testing & Debugging

```python

def seven(anything):
    return 7


assert seven(7) == 7
assert seven(17) == 7
assert seven(717) == 8
assert seven(1) == 7

```



## PyPi, PIP and Virtual Environments
Virtual environments enable you to have lots of different python installations on your PC that are completely isolated from each other. 
### Creating an Anaconda (virtual) Environment
1. Open Anaconda on your PC
1. Click on the 'Environments' tab on the left-hand side of the screen
2. Click on the 'create' icon at the bottom of the screen
3. Name your environment (with a python-friendly name of course), make sure the 'Python' box is selected, and click the 'create' button
4. Once it is created the packages installed in it are listed on the right-hand-side of the screen. 
5. Using the search facility find and istall the package 'Flask' which is "A simple framework for complex web application "
6. With your current knowledge of Python plus a modicum of HTMl you can create yourself a great looking website to demonstrate your expertise as a web developer.



## SQL

Try the examples at [sqlzoo.net](https://sqlzoo.net/wiki/SQL_Tutorial)
and [W3schools](https://www.w3schools.com/sql/default.asp)

## Version Control

Git and GitHub are my preferences, there are others


## Try Compute-it! by toxicode - one of my favourites
[compute-it.toxicode.fr/](https://compute-it.toxicode.fr/) kids love it :-)

