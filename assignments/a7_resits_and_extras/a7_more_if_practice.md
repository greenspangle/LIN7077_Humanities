# LIN7077 Selection (if) additional practice questions

## thermostat(temperature)

If the temperature is less that 19 turn the heat on, If it’s more than 24 turn the heat off. If it’s
neither, leave the heat setting as it is. Return the string `'on'`, `'off'` or `'stet'` respectively.
For example:

| temperature | return value |
|:-----------:|:------------:|
|     21      |   	'stet'    |
|     16      |     'on'     |
|     34      |    'off'     |
|     19      |    'stet'    |
|     24      |    'stet'    |

**Hints**

* A few if statements with possibly some elif and else, should get the job done.

## score_2a(dice_1, dice_2)

The parameters are guaranteed to be integers between 1 and 6 inclusive and represent the face values on the
throw of two six-sided dice. Calculate the score according to this rule:

* The score is the sum of both dice unless it is a 'double' (both dice the same) in which case add one of
  the dice to the score again, unless it is 'double six' in which case both dice to the score again.

For example:

| parameter values | return value |
|:----------------:|:------------:|
|      `1, 5`      |     `6`      |
|      `5, 1`      |     `6`      |
|      `3, 4`      |     `7`      |
|      `1, 1`      |     `3`      |
|      `2, 2`      |     `6`      |
|      `6, 6`      |     `24`     |

**Hints:**\
A few `if` statements with possibly some `elif` and `else`, should get the job done.

## score_2b(dice_1, dice_2)

Unchanged from score_2a() except that if the sum of both dice is seven, double it.

For example:

| parameter values | return value |
|:----------------:|:------------:|
|      `1, 5`      |     `6`      |
|      `5, 1`      |     `6`      |
|      `3, 4`      |     `14`     |
|      `5, 2`      |     `14`     |
|      `1, 1`      |     `3`      |
|      `2, 2`      |     `6`      |
|      `6, 6`      |     `24`     |

**Hints:**\
Same again: `if`,  `elif` and `else` statements. This is just another condition to consider.

## score_4a(red1, red2, blue1, blue2)

The parameters are guaranteed to be integers between 1 and 6 inclusive.
They represent the face values on the throw of four six-sided dice, two coloured red and two coloured blue.
Calculate the score according to the rule:

* The score is the sum of both red dice.
* If the sum of the red dice is seven add the lowest blue dice to the score.
* If the two red dice are the same but not both six, add the highest blue dice to the score.
* If the two red dice are both six then add both blue dice to the score.

  For example:

| red dice | blue dice | return value |
|:--------:|:---------:|:------------:|
|  `1, 5`  |  `6, 6`   |     `6`      |
|  `3, 2`  |  `4, 3`   |     `5`      |
|  `2, 5`  |  `2, 6`   |     `9`      |
|  `1, 1`  |  `2, 6`   |     `10`     |
|  `6, 6`  |  `3, 2`   |     `17`     |

**Hints:**\
Same again: `if`, `elif` and `else`. Just be careful you cover all the options and test them.

## score_4b(red1, red2, blue1, blue2)

The parameters are guaranteed to be integers between 1 and 6 inclusive. They represent the face values on
the throw of four six-sided dice, two coloured red and two coloured blue. Calculate the score according to
the rule:

**TBA**

* If the sum of any one red dice and any one blue dice is seven, score 7.
* If the sum of any one red dice and any one blue dice is seven, and the sum of the remaining red and blue
  dice is also seven, score 21.
* Otherwise, score the face value of the lowest of all four dice.\
  For example:

| red dice | blue dice | return value |
|:--------:|:---------:|:------------:|
|  `1, 5`  |  `6, 6`   |     `7`      |
|  `3, 2`  |  `3, 3`   |     `2`      |
|  `2, 6`  |  `1, 5`   |     `21`     |
|  `1, 1`  |  `2, 6`   |     `7`      |
|  `6, 6`  |  `6, 6`   |     `6`      |

**Hints:**

* Same again: `if`, `elif` and `else`.
* Just be careful you cover all the options and test them.

## score_4c(red1, red2, blue1, blue2)

The parameters are guaranteed to be integers between 1 and 6 inclusive and represent the face values on the
throw of four six-sided dice. Two coloured red and two coloured blue.  
Calculate the score according to the rule:

* The score is the face value of the lowest of all four dice
* Unless the sum of any one red dice and any one blue dice is seven in which case score 7
* Unless the sum of any one red dice and any one blue dice is seven, and the sum of the remaining red and
  blue dice is also seven, in which case score 14
* Unless the four dice are any permutation of (3,3,4,4), in which case score 21

| red dice | blue dice | return value |
|:--------:|:---------:|:------------:|
|  `1, 5`  |  `6, 6`   |     `7`      |
|  `3, 2`  |  `3, 3`   |     `2`      |
|  `2, 6`  |  `1, 5`   |     `14`     |
|  `1, 1`  |  `2, 6`   |     `7`      |
|  `1, 2`  |  `3, 4`   |     `1`      |
|  `3, 3`  |  `3, 4`   |     `7`      |
|  `3, 3`  |  `4, 4`   |     `21`     |
|  `4, 3`  |  `3, 4`   |     `21`     |

**Hints**  
Same again: if, elif and else. Just be careful you cover all the options and test them.

## tax_due(income)

The parameter `income` is guaranteed to be a positive number.
Calculate the income tax due according to this table:

| Band               | Taxable income      | Tax rate |
|--------------------|---------------------|:--------:|
| Personal Allowance | Up to £12,570       |    0%    |
| Basic rate         | £12,571 to £50,270  |   20%    |
| Higher rate        | £50,271 to £150,000 |   40%    |
| Additional rate    | over £150,000       |   45%    |

(You can find the exact rules at
HMRC [https://www.gov.uk/income-tax-rates](https://www.gov.uk/income-tax-rates)

For example:

|  income  | tax due |
|:--------:|:-------:|
|   `0`    |   `0`   |
| `12,570` |   `0`   |
| `12,571` |  `0.2`  |
| `50,271` | `8,000` |

Design, build and test the following functions:
Submit your python script with the filename 'w6_yourID.py'.\

**Hints:**\
A few `if` statements with possibly some `elif` and `else`, should get the job done.

## isa_vowel(a_char)

If the parameter `a_char` is one of 'a', 'e', 'i', 'o' or 'u' then return `True`, else return `False`.

## weekday(an_int):

The parameter is guaranteed to be an integer.

If the days of the week are numbered 1 for Monday, 2 for Tuesday, through to 7 for Sunday. Answer the day of
the week that `an_int` corresponds to. If an_int is less that 1 or greater than 7 answer `'Noday'`

| an_int | return value |
|:------:|:------------:|
|  `1`   |  `'Monday'`  |
|  `2`   | `'Tuesday'`  |
|  `1`   | `'Saturday'` |
|  `1`   |  `'Sunday'`  |
|  `-1`  |  `'Nonday'`  |
|  `8`   |  `'Nonday'`  |

## monthname(an_int)

The parameter is guaranteed to be an integer.

If the months of the year are numbered 1 for January, 2 for February, through to 12 for December. Answer the
month of the year that `an_int` corresponds to. If an_int is less that 1 or greater than 12
answer `'Nomonthber'`.

| an_int | return value |
|:------:|:------------:|
|  `1`   | `'January'`  |
|  `2`   | `'February'` |
|  `12`  | `'December'` |
|  `-1`  |  `'Nonday'`  |
|  `13`  |  `'Nonday'`  |

## char_type(a_char)

The parameter is guaranteed to be a string containing a single character. If the character is one of the
numberic digits [0..9] answer `'digit'`. If it is a character in [a-z][A..Z] answer `'alpha'` otherwise
answer `'special'`.

| a_char | return value |
|:------:|:------------:|
| `'1'`  |  `'digit'`   |
|  `a`   |  `'alpha'`   |
|  `;`   | `'special'`  |

## grade(mark)

The parameter `mark` is guaranteed to be a number.

Determine the candidates `grade` according to the rule: 80 or more is `'A'`, less than 80 but 70 or more
is `'B'`, less than 70 but 60 or more is `'C'`, less than 60 but 50 or more is `'D'`, less than 50 but 40 or
more is `'E'`, otherwise the grade is `'F'`.

Also determine the `classification`. Grades A and B are `'Pass with merit'`, grades C, D, E are `'Pass'` and
F is `'Fail'`

Return the candidates `grade` and `classification`.

For example:

|   mark   |         returns          |
|:--------:|:------------------------:|
|   `-3`   |       `'F', Fail'`       |
|   `10`   |       `'F', Fail'`       |
| `39.999` |       `'F', Fail'`       |
| `39.999` |      `'F', 'Fail'`       |
|   `40`   |      `'E', 'Pass'`       |
| `49.999` |      `'E', 'Pass'`       |
|   `50`   |      `'D', 'Pass'`       |
| `59.999` |      `'D', 'Pass'`       |
|   `60`   |      `'C', 'Pass'`       |
| `69.999` |      `'C', 'Pass'`       |
|   `70`   | `'B', 'Pass with merit'` |
| `79.999` | `'B', 'Pass with merit'` |
|   `80`   | `'A', 'Pass with merit'` |
| `89.999` | `'A', 'Pass with merit'` |
|   `90`   | `'A', 'Pass with merit'` |
|  `123`   | `'A', 'Pass with merit'` |
