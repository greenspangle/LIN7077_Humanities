# Practicing Software Re-use
First let's think about reusing your own software

In your first assessed assignment you created the function called `magic7()` that takes no parameters and always returns the integer `7`. You are now working on another project and realise that you need a function that does exactly what `magic7()` does. Thinking about it you realise you have two options:

1. Copy & paste the function definition from your assignment into your current script
1. Somehow make the `magic7()` function that you have already written and tested available within the current script

Well obviously the answer is going to be the second option but how to do that? The answer is with the **import** statement.

## Reusing your own scripts
You can get started on doing this by copying the assignment script that you wrote to the same _folder_ as your current script. You can then import it into your current script like this:

```python

# let's say your assignment script is called 'answers_99.py'
# you can import its contents with this statement

import answers_99
print(answers_99.magic7())  # this should print the integer 7

# as that assignement script also contains the function add_old_uk()
# it is also available for you to use

print(answers_99.add_old_uk(123,345,567,789,890, 901))  # -> (932, 59, 28)
```

There are a few variations on the import statement:

```python

# you can give the imported script a shorter name
import answers_99 as a99
print(a99.magic7())
``` 
and if you only need one of the functions
```python

# import individual functions with their original name
from answers_99 import magic7
print(magic7())
```

and, if you need to, you can rename the imported function
```python

# import individual functions and rename him
from answers_99 import magic7 as m7
print(m7())
```

## Reusing Modules from the Standard Library
Some parts of the standard library modules are already imported into your Python environment. Things like strings, lists, sets and dictionaries. 

Most of the standard library is NOT available in your Python environment until you explicitly import it. For instance, if you want to use the `random` module to generate some random numbers you have to import it like this:

```python

# This program prints 5 random integers between 1 and 6 inclusive
import random
for _ in range(5):  # the underscore is a placeholder 
                    # as we don't need the numbers that range generates
                    # we just want to loop 5 times
    print(random.randint(1,6))  # prints a random integer between 1 and 6 inclusive
```

### A few problems to try
1. Print 10 random integers between 1 and 6 inclusive
2. Create a list of 10 random integers between 1 and 6 inclusive
1. Create a list of 100 random numbers between 0 and 9 inclusive
2. Shuffle the list [1,2,3,4,5,6] five times, printing the list after each shuffle
3. Select and print 5 random letters from the string 'abcdefghijklmnopqrstuvwxyz'
4. Select 3 random letters from 'abcdefghijklmnopqrstuvwxyz', 3 from  'abcdefghijklmnopqrstuvwxyz'.upper(), two from '0123456789'. Shuffle them together and print the result 
1. Do the same again but this time the result must begin with a lowercase letter (so that it is a legal variable name)
4. A password must contain at least `a` uppercase letters, `b` lowercase, `c` digits and d symbol. Write a function that takes four integer parameters and outputes a legal password. 
5. Write a test script that will test the password you just created


