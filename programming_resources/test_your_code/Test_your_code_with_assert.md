# Testing Your Code

Untested code is unreliable code. It might work perfectly, but it probably won't.

There are many ways you can test your code:

* Desk-check the code and assume that it works
* Run the code in IDLE and do some ad-hoc testing
* Write a list of tests that cover all the functionality and run them manually
* Write a list of tests that cover all the functionality and write some code to run them automatically.

This testing code could be:

1. None-existent.
2. Tests output two columns: 'expected outcome' vs 'actual outcome'. Inspect that output manually for
   differences.
3. A sequence of try-except statements using `assert` statements that onluy output failed tests.
4. Built on a test framework such as `pytest`

## Testing with `print()` statements

This is easy to understand and implement but as you write more and more code it becomes progressively more
and more unwieldy. Each time you run your tests you have to manually check the output of dozens or even
hundreds, maybe thousands, of print statements looking for the one or two that are 'wrong'. Not only is this
mind-numbingly boring, as the number of tests grow it's increasingly likely that you will fail to spot the
erroneous printouts.

## Testing with `assert` statements

The 'assert' statement evaluates a boolean expression. If the expression evaluates to `True` it does
nothing, if it evaluates to `False` it throws an `AssertionError`. Which means that if all tests pass,
nothing happens! Using `assert` statements it's easy to test lots of cases without having to wade through
lots of output for no reason.

## An example of testing with assert

Imagine you have been asked to implement a function called `thermostat(temperature)` which
returns `'heat on'` if the temperature is less than 19, returns `'heat off'` if it's more than 24, and
returns `'stet'` otherwise.

For example:

| temperature | return value |
|:-----------:|:------------:|
|    `21`     |   `'stet'`   |
|    `16`     | `'heat on'`  |
|    `34`     | `'heat off'` |
|    `19`     |   `'stet'`   |
|    `24`     |   `'stet'`   |

This function can be tested with this collection of assert statements:

```python

def thermostat(temperature):
    pass


assert thermostat(21) == 'stet'
assert thermostat(16) == 'heat on'
assert thermostat(34) == 'heat off'
assert thermostat(19) == 'stet'
assert thermostat(24) == 'stet'
```

If when you run this nothing happens, then you code has passed all the tests.