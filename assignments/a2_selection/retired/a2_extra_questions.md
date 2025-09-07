



## grade(mark)

The parameter `mark` is guaranteed to be a number.
Return the grade according to the rule:

* 80 or more return 'A'
* less than 80 but 70 or more return 'B'
* less than 70 but 60 or more return 'C'
* less than 60 but 50 or more return 'D'
* less than 50 but 40 or more return 'E'
* otherwise return 'F'.

```def grade(mark):
    """The parameter mark is guaranteed to be a number.
    Return the grade according to the rule:
    80 or more return 'A',
    less than 80 but 70 or more return 'B',
    less than 70 but 60 or more return 'C',
    less than 60 but 50 or more return 'D',
    less than 50 but 40 or more return 'E',
    otherwise return 'F'."""
    if mark >= 80:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 50:
        return 'D'
    elif mark >= 40:
        return 'E'
    else:
        return 'F'
```




# grade(mark)
    @unittest.skipIf('grade' not in functions_implemented,
                     'grade() not implemented')
    def test_grade(self):
        # A grade
        self.assertEqual(grade(999), 'A')
        self.assertEqual(grade(99), 'A')
        self.assertEqual(grade(90), 'A')
        self.assertEqual(grade(89), 'A')
        self.assertEqual(grade(80), 'A')
        self.assertNotEqual(grade(79.999999), 'A')
        # B grade
        self.assertEqual(grade(79.9999999), 'B')
        self.assertEqual(grade(79), 'B')
        self.assertEqual(grade(70), 'B')
        # C grade
        self.assertEqual(grade(69.999999), 'C')
        self.assertEqual(grade(69), 'C')
        self.assertEqual(grade(60), 'C')
        # D grade
        self.assertEqual(grade(59.999999), 'D')
        self.assertEqual(grade(59), 'D')
        self.assertEqual(grade(50), 'D')
        # E grade
        self.assertEqual(grade(49.999999), 'E')
        self.assertEqual(grade(49), 'E')
        self.assertEqual(grade(40), 'E')
        # F grade
        self.assertEqual(grade(39.999999), 'F')
        self.assertEqual(grade(39), 'F')
        self.assertEqual(grade(30), 'F')
        self.assertEqual(grade(20), 'F')
        self.assertEqual(grade(10), 'F')
        self.assertEqual(grade(1), 'F')
        self.assertEqual(grade(0), 'F')
        self.assertEqual(grade(-1), 'F')

## thermostat(temperature)

If the temperature is less that 19 turn the heat on, if it's more than 24 turn the heat off, and if it's
neither, leave the heat setting as it is.
Return the string `'heat on'`, `'heat off'` or `'stet'` respectively.

For example:

| temperature | return value |
|:-----------:|:------------:|
|    `21`     |   `'stet'`   |
|    `16`     | `'heat on'`  |
|    `34`     | `'heat off'` |
|    `19`     |   `'stet'`   |
|    `24`     |   `'stet'`   |

**Hints:**

* A few `if` statements with possibly some `elif` and `else` should get the job done.

## fizzbuzz(an_int)

### Problem statement

The parameter is guaranteed to be an integer.

* If it is a multiple of 3 return ‘Fizz’.
* If it is a multiple of 5 return ‘Buzz’.
* If it is a multiple of 3 and 5 return ‘FizzBuzz’.
* If it is none of those return `an_int` as a string.

### implementation
```
def fizzbuzz(an_int):
    """The parameter is guaranteed to be a positive integer.
    If it is a multiple of 3 return ‘Fizz’.
    If it is a multiple of 5 return ‘Buzz’.
    If it is a multiple of 3 and 5 return ‘FizzBuzz’.
    If it is none of those return an_int as a string."""
    if an_int % 5 == 0 and an_int % 3 == 0:  # is divisible by 3 and by 5
        return 'FizzBuzz'
    elif an_int % 3 == 0:  # is only divisible by 3
        return 'Fizz'
    elif an_int % 5 == 0:  # is only divisible by 5
        return 'Buzz'
    else:  # is divisible by neither 3 nor 5
        return str(an_int)
```

### unittest 
  @unittest.skipIf('fizzbuzz' not in functions_implemented,
                     'fizzbuzz() not implemented')
    def test_fizzbuzz(self):
        # Fizz
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(33), 'Fizz')
        self.assertEqual(fizzbuzz(33033), 'Fizz')

        # Buzz
        self.assertEqual(fizzbuzz(10), 'Buzz')
        self.assertEqual(fizzbuzz(50), 'Buzz')
        self.assertEqual(fizzbuzz(75085), 'Buzz')

        # FizzBuzz
        self.assertEqual(fizzbuzz(30), 'FizzBuzz')
        self.assertEqual(fizzbuzz(304560), 'FizzBuzz')

        # neither
        self.assertEqual(fizzbuzz(1), '1')
        self.assertEqual(fizzbuzz(7), '7')
        self.assertEqual(fizzbuzz(131), '131')



## score_2(dice_1, dice_2)

The parameters are guaranteed to be integers between 1 and 6 inclusive and represent the face values on the
throw of two six-sided dice. Calculate the score according to this rule:

* The score is the sum of both dice
* unless it is a 'double' (both dice the same) in which case add one of the dice to the score again
* unless it is 'double six' (both dice six) in which case add both dice to the score again
* unless the sum of the two dice is seven in which case double it

For example:

| parameter values | return value |
|:----------------:|:------------:|
|      `1, 5`      |     `6`      |
|      `5, 1`      |     `6`      |
|      `3, 4`      |     `14`     |
|      `5, 2`      |     `14`     |
|      `2, 2`      |     `6`      |
|      `6, 6`      |     `24`     |

**Hints:**

* A few `if` statements with possibly some `elif` and `else`, should get the job done.


## score_4(red1, red2, blue1, blue2)

The parameters are guaranteed to be integers between 1 and 6 inclusive. They represent the face values on
the throw of four six-sided dice, two coloured red and two coloured blue. Calculate the score according to
the rule:

* The score is the face value of the lowest of all four dice
* Unless the sum of any one red dice and any one blue dice is seven in which case score 7
* Unless the sum of any one red dice and any one blue dice is seven, and the sum of the remaining red and
  blue dice is also seven, in which case score 14
* Unless the four dice are any permutation of (3,3,4,4), in which case score 21

For example:

| parameter values |   return value    |
|:----------------:|:-----------------:|
|   `1, 5, 6, 6`   |        `7`        |
|   `3, 2, 3, 3`   |        `2`        |
|   `2, 6, 1, 5`   |       `14`        |
|   `1, 1, 2, 6`   |        `7`        |
|   `1, 2, 3, 4`   |        `1`        |
|   `3, 3, 3, 4`   |        `7`        |
|   `3, 3, 4, 4`   |       `21`        |
|   `4, 3, 3, 4`   |       `21`        |

**Hints:**

* Same again: `if`, `elif` and `else`. Just be careful you cover all the options and test them.




## add_old_uk_v2(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2)

This is the same as the `add_old_uk()` function specified in assignment #1 except with the additional features that:

* Negative amounts such as `add_old_uk_v2(0, -15, 11, -1, 7, -3)` are dealt with correctly
* The returned `(pounds, shillings, pennies)` value is either entirely negative or entirely positive. A return value
  of`(0, -15, 11)` would be incorrect, the correct representation is `(0, -14, -1)`
* In line with normal convention, positive zero and negative zero are represented by the same symbol, `0`
* The last three parameters have default values of zero.

Now that you have the 'if' statement in your programming arsenal this should be achievable

__**EXTRA challenge**__
This is a bit tricky but it is possible to build this function WITHOUT using an `if` statement.

**Hint (if not using `if`):**
The built-in function abs() accepts a number and returns the absolute value of that number. In other words, regardless
of whether it is give a positive or negative valued parameter, it always returns the positive value




## add_hms_v2(hr1, min1, sec1, hr2, min2, sec2)
Now that add_old_uk() copes with negatives, do the same with add_hms()
====================================




