# Software Testing

Untested software is low quality software.

The only way we can be sure that software does what it is supposed to do is to test it.

**IMPORTANT:** Testing is NOT debugging

* Testing is finding faults in software
* Debugging is fixing faults in software
* It is the testers job to find as many faults as possible, it is the programmers job to fix those faults.

## How to test software?

Imagine you are the test manager (often called the QA manager) of a large software development house. It is your job to ensure that all
software released into production is bug-free and fully complies with the original specification. If faulty
software is released into production you will be held as **more** responsible for the error than the
programmer who wrote the code.

You will have the written specification for the software (usually a function) from the design team and the
code from the programmer which you need to test to confirm it fully complies with the specification. Of
course the programmer assures you they have 'thoroughly tested' their code and confirmed it 'fully complies'
with the specification.

What is the best way for you to test this software? Here are a few suggestions:

* You trust the programmer did a good job
* The programmer that wrote the code writes some ad-hoc tests to confirm it works and they show you the results
* Another programmer, who had nothing to do with writing the code, reads the specification and then writes
  and runs some tests and confirms it's working
* Both programmers sit down together and trace through the source code line-by-line to confirm that it is
  all correct, and then both confirm the code is good.

Something else? What would you do?

1. ? Stop. Think. Write.
2. ? Stop. Think. Write.
3. ? Stop. Think. Write.

In most situations there are an infinite number of possible tests you could run which means it
is not possible to check that every possible input produces the correct output. So your problem reduces
to:

1. What are the best tests?
1. What are the best values to test with?
2. How many tests are required to 'thoroughly test' the software
3. How can the tests be automated

Remember that it is _you_, not the programmer, who will be held primarily responsible if a software fault is subsequently found.

## Using `print()` or `==` or `assert` ?

All of these can be used to run a small numbers of tests but only one of them is a viable option for large numbers of tests.

For example, to test a thermostat() function that inputs a single numerical parameter and returns a string, you might choose to test it with the parameter value `11` knowing the result should
be `'heat on'`.

This test can be written in various ways:

``` 

print(thermostat(11), " : should print 'heat on'" )  # simple and obvious
# or
thermostat(11) == 'heat on'         # no output produced so not effective
# or
print(thermostat(11) == 'heat on')  # so have to wrap it in a print() anyway.
# or
assert thermostat(11) == 'heat on'  # if True does nothing, 
                                    # if False raises exception and stops execution
```

When there are more than a handful of tests the `print()` variations produce overwhelming amounts of text
that someone still has to read through and check every line - which is very boring and equally error-prone.
The quantity of output does not depend on if the tests are successful or not, the same amounts of text is
produced in both cases, and it all has to be read regardless.

With the `assert` statements the situation is very different. Only the failed tests have any effect. If all
test pass then _nothing_ happens.

The `assert` statement is almost always the best option for testing

## Test the function thermostat(temperature)

### The thermostat() Specification

The function parameter 'temperature' is any floating point number or integer.
The function returns a text string.
If the temperature is less that 19 return `'heat on'`, if it is more than 24 return `'heat on'`, and if it
is neither return  `'stet'`.

### Specify the tests you would run, and why?

1. assert thermostat(11) == 11  # because it was just discussed
1. ?
1. ?
1. ?
1. ?
1. ?

### The thermostat() test suite
Copy your version of thermostat() into a new script, save it, and run it

Now add the tests you have just designed at the end of the same python script. 

Write (at least some of) the tests three times; once as a print statement, once as an `==` test within a print statement, and once as an assert statement. Save it and run it. 

Now modify thermostat() to introduce a small error, perhaps by changing a `<` to a `<=` operator, and now run it again.

Which was the best at alerting you to the fact that an error existed?


## Test the function score_2(dice_1, dice_2))

### The score_2() specification

The parameters are guaranteed to be integers between 1 and 6 inclusive and represent the face values on the
throw of two six-sided dice. Calculate the score according to this rule:

* The score is the sum of both dice
* unless it is a 'double' (both dice the same) in which case add one of the dice to the score again
* unless it is 'double six' (both dice six) in which case add both dice to the score again
* unless the sum of the two dice is seven in which case double it
You to do this


### Specify the tests you would run, the expected result, and why?

1. ?
1. ?
1. ?
1. ?
1. ?

### The score_2() test suite
Copy your version of score_2() into a new script, save it, and run it

Now add the tests you have just designed at the end of the same python script. 

Write (at least some of) the tests three times; once as a print statement, once as an `==` test within a print statement, and once as an assert statement. Save it and run it. 

Now modify thermostat() to introduce a small error, perhaps by changing a `<` to a `<=` operator, and now run it again.

Which was the best at alerting you to the fact that an error existed?


## Test the function score_4(red1, red2, blue1, blue2))

You to do this. Design the tests, write them in a script, and run them.


## Test the function add_hms(hr1, min1, sec1, hr2, min2, sec2)

### Specification of add_hms() from design team

The function adds two hour, minute, seconds time durations.

All parameters are all guaranteed to be positive integers (zero or greater).

The function must return the sum of the two durations as a total time duration in hours minutes and seconds
with minutes and seconds both < 60.

### What tests to run? Why?

1. ?
2. ?
3. ?
4. ? 
### The add_hms() test suite
As before, copy your code into a new script and add the tests after that.
Then run it and test the test by introducing an error in the code.


## Testing Vocabulary
### Testing Frameworks
A library of functions designed for building, executing, and reporting the results of testing.  In the python standard library there are: [unittest](https://docs.python.org/3/library/unittest.html) and [doctest](https://docs.python.org/3/library/doctest.html). A very popular, very powerful, and easy to learn testing framework is [pytest](https://docs.pytest.org/en/7.2.x/). If you are doing a lot of testing start with Pytest.



### Boundary value tests
Many function have step changes in their behaviour at or near a particular value. For instance thermostat() changes its behaviour around the parameter value `19`. Just below `19` it answers `'heat on'` and just above it answers `'stet'` so `19` is a boundary value. The function should therefore be tested three times: at just below `19`, at just above `19` and at exactly `19`. 


### Path Testing
There are many possible execution paths through a function. The purpose of path testing is to ensure that every possible path is executed at least once during testing.

### TDD - Test Driven Development
The design team write the function specification but the next step after that is to write all the tests. This means that the programmer has the 'written' specification from the design team and the 'test' specification from the QA team. The programmer then writes the function but only passes it to QA for final testing when the programmer themselves has confirmed it passes all of the tests in the specification.

### White Box Testing
You have the code the programmer wrote, and you can read and inspect its internals to help design better tests.

### Black Box Testing
You have no knowledge of the code the programmer has written. You only have the specification.