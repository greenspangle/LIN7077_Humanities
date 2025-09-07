# Making Decisions with `if`

Work your way through these practice exercises. Do modify and change these code
examples so that you get maximum benefit from your time.

## Is a statement `True` or is it `False`

At the interactive Python prompt execute these statements:

```
3 < 4 
```

```
3 > 4 
```

```
not 3 < 4 
```

You should get the boolean values `True`, `False`, and `False`.

As well as numbers you can use the relational operators to compare other types
of object such as strings:

```
'three' < 'four'
```

```
'four' < 'five'
```

```
'five' < 'six'
```

# The `if` statement

The structure of an `if` statement is:

```
if condition:
   body
```

The code in the `body` block executes ONLY when the `condition`
statement evaluates to `True`.

## Evaluating `if` statements interactively

You can type `if` statements directly into python and execute them.
Try these examples at the interactive prompt:

```
if True:
   'The body code of the if statement has executed'
```

The condition part of the `if` statement evaluates to `True`
hence the code in the body part of the `if` statement executes
and the string `'The condition statement is True'` is created
and echoed at the prompt.

Whereas in this example:

```
if False:
   'The body code of the if statement has executed'
```

The condition part of the `if` statement evaluates to `False`
hence the code in the body part of the `if` statement to create the string
`'The body code of the if statement has executed'` DOES NOT execute.

```
if 3 < 4:
    print("three is less than four")
``` 

and press return.
Python should print "three is less than four""

```
if not 3 < 4:
    print("three is not less than four")
``` 

What result did you get? Can you explain why?

## Using `if` statements in stored programs

Typing code into the python prompt is great for trying-things-out,
but usually you will want to save your work in a file, or better still,
generalise your code into a reusable function and save that in a file.

Create and test the following examples in a python file named if_examples.py:

```
if True:
   print('The condition statement is True')
```

The body code `print('The condition statement is True')` will execute
because the `if` condition is `True`

Whereas in this example:

```
if False:
   print('The condition statement is True')
```

The body code does not execute because the condition is `False`

Here are more examples

```
def my_max_v1(a, b):
    """my first version of the built-in max() function """
    # test if a is greater than b
    if a > b:
        return a
    # test if b is greater than or equal to a
    if b >= a:
        return b

def my_max_v2(a, b):
    """my second version of the built-in max() function
     Works just as well and, in general, is less prone to bugs"""
    if a > b:
        return a
    # if a is not greater than b, then b is at least as big as a
    return b  

def my_max_v3(a, b):
    """my third version of the built-in max() function _is_FAULTY_. 
    Can you spot what's wrong with it?"""
    if a > b:
        result = a
    result = b
    return result


my_max = my_max_v2  # I think v2 is the best choice
```

Execute if_examples.py then check the functions you wrote are now in
memory by using the built-in function dir().

Test these functions work in the way you expect with test cases such
as `my_max (3,4)`, `my_max('three','four')`, etc.

**Task:**

* Design, write and test a function `my_min(value1, value2)` that duplicates
  the functionality of the built_in function min().

Here are few more functions using 'if' to practice with:

``` 

def grade_v1(mark):
    """ Pass or Fail? """
    if mark > 60:
        return 'Pass'
    return 'Fail'

def brolly(a_str):
    """ take umbrella? """
    if 'rain' in a_str:
        return 'Take umbrella'

def weather(a_str):
    """ rain or shine? """
    if 'rain' in a_str:
        return 'Take umbrella'
    if 'sun' in a_str:
        return 'Take sunscreen'
    return 'Look outside and guess'

def exec_decision(task = 'lunch', deadline_today = True):
    """ executive decision maker with default values"""
    if deadline_today:
        return 'Do ' + task + ' now!'
    return 'put off until tomorrow'
```

The above functions are easy to copy & paste so check you know what each
statement is doing.

Execute your script then test your functions to make sure they work as
anticipated.

```
weather('rainclouds')
```

```
weather('cloudy with occasional showers')
```

```
exec_decision()
```

Is the result they give what you expected?

## More if examples

Here is a more realistic version of a grading function:

```
def grade_v2(mark):
    """ Answer grade for given mark """
    if mark > 80:
        return 'Excellent'
    if mark > 60:
        return 'Good'
    if mark > 40:
        return 'Pass'
    return 'Try harder next time'
```

Execute it and test it works.

As things get more complicated, lots of separate `if . . . return` statements
become prone to bugs as it's easy to leave 'gaps' between the conditions. With
more actions associated with each condition it also gets more difficult to
maintain.

# The `else` statement

The 'else' statement catches the other option to the 'if' statement. Here's an
example

```
# A simple grading structure
def grade_v2(mark):
    """ Pass or Fail? """
    if mark > 40:
        grade =  'Pass'
    else:
        grade 'Fail'
    # more statements
    return grade
```

Here is an example that nests `if-else` statements:

```
def grade_v3(student_mark):
    """This structure makes sure there are no gaps between grades"""
    if student_mark > 90:
        grade = 'Starship Captain'
    else:
        if student_mark > 80:
            grade = 'Astronaut'
        else:
            if student_mark > 60:
                grade = 'Aeronaut'
            else:
                if student_mark > 40:
                    grade = 'Earthling'
                else:
                    grade = 'Oh deary, deary me'
    return grade
```

and another example:

```
def grade_v4(student_mark):
  """Using if-else. Imagine if there were ten grade options, or more.
  This nesting could get very deep and if combined with other conditions,
  very difficult to fathom."""
  if student_mark > 90:
    grade = 'A'
    classification = 'first'
  else:
    if student_mark > 80:
      grade = 'B'
      classification = 'second'
    else:
      if student_mark > 60:
        grade = 'C'
        classification = 'second'
      else:
        if student_mark > 40:
          grade = 'D'
          classification = 'third'
        else:
          grade = 'F'
          classification = 'oh deary, deary me'
  return grade, classification
```

# The `elif` statement

More grades mean's more `if-else` statements and deeper nesting of
successive `if`
clauses.

```
# elif simplifies things 
def grade_v5(student_mark):
    "Using if-elif-else the code is much neater and easier to read"""
    if student_mark > 90:
        grade = 'Starship Captain'
    elif student_mark > 80:
        grade = 'Astronaut'
    elif student_mark > 60:
        grade = 'Aeronaut'
    elif student_mark > 40:
        grade = 'Earthling'
    else:
        grade = 'Oh deary, deary me'
    return grade
```

# Boolean Algebra

The algebra of logic.

Boolean algebra has two values, `True` and `False`,
and three operators `and`, `or`, and `not`.

## Boolean Expressions

If `a` and `b` are two boolean values then:

* `a and b` is `True` if and only if  `a` is `True` and `b` is `True`
* `a and b` is `False` if `a` is `False` or `b` is `False` or both are `False`
* `a or b` is `True` if `a` is `True` or `b` is `True` or both are `True`
* `a or b` is `False` if and only if `a` is `False` and `b` is `False`
* `not a` is `True` if `a` is `False`
* `not a` is `False` if `a` is `True`

## Example Boolean expression

Evaluate these Boolean equations on paper and then confirm by executing them
interactively in IDLE:

`a = True         `

`b = True         `

`a and b          `

`a or b           `

`not a and b      `

`not a or b       `

`not not not not a`

`a and not a      `

`b and not b      `

`a or not a`      

`b or not b`


# complex `if` conditions

So far the conditions in `if` statements have been simple comparisons,
for instance `grade > 50`.

Boolean algebra allows us to combine these simple conditional statements using
boolean operators. For instance:

```
if today == 'saturday' or today == 'sunday':
    weekend = True
```


## Truth Tables

The behaviour of the boolean operators can be summarised in truth tables:

| AND |   a   |   b   | a and b |
|-----|:-----:|:-----:|:-------:|
|     | True  | True  |  True   |
|     | True  | False |  False  |
|     | False | True  |  False  |
|     | False | False |  False  |

| OR |   a   |   b   | a or b |
|----|:-----:|:-----:|:------:|
|    | True  | True  |  True  |
|    | True  | False |  True  |
|    | False | True  |  True  |
|    | False | False | False  |

| NOT |   a   | not a |
|-----|:-----:|:-----:|
|     | True  | False |
|     | False | True  |


Build the truth table for:
(a or not b) and (not b or not a) or (b and not a)

## Venn Diagrams

Venn diagrams can be helpful when trying to visualise Boolean expressions.
They are very handy tools when you need them.


That said though, it is good practice to design your code so that the Boolean
conditions are individually simple.
