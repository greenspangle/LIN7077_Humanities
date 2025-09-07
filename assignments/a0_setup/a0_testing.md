# Testing, Testing, Testing, ...

Whenever you write code, you **must** test it.

Untested code is almost certainly buggy code.

## Your code does not execute"
If Python cannot run your code, an error message will be printed at the console:

1. Read the message!
2. Python programmers wrote these error messages to help other programmers,
   i.e. to help you!
3. A Python error message is like a russian doll that unwraps itself as you
   read down the page.
   This means the root cause of the error is often at the bottom of the
   message, which means it can often be helpful to read error messages from
   the bottom up.

3. Fix your code and test again

Repeat the above until there are no errors


## Testing with `print()` statements

You can use the `print()` statements such as `print(magic_number(678))`
and read the results but that is laborious and error-prone.

Thorough testing means lots of `print()` statements that all has to be read
and compared to the expected result.

## Testing with `assert()` statements.

See https://www.w3schools.com/python/ref_keyword_assert.asp for examples.

1. If the assert statement evaluates to `True` then nothing happens
2. If the assert statement evaluates to `False` 


) to
Once you have written your function, you can add assert statements (
 your answer
script e.g. `assert magic_number(678) == True` and
`assert magic_number(456) == False`


## Testing with the `unittest` test framework

In a few weeks, when you are more fluent in Python, we will use 'unittest'
from the standard library,.

