LIN7077 extra practice with collections and iteration


## runup(a_str)

The parameter a_str is guaranteed to be a string made entirely of lowercase alpha characters [a...z] .
Answer the starting position and length of the longest substring of `a_str` that is in alphabetical order. ('a' then 'b' and so on all the way to 'z')
If there are multiple such substrings, report the first. If a_str is empty return (-1, 0).

For example:

| parameter values | substring  | return value |
|:----------------:|:----------:|:------------:|
|       `''`       |    `''`    |   `-1, 0`    |
|      `'z'`       |   `'z'`    |    `0, 1`    |
|    `'ababcb'`    |  `'abc'`   |    `2, 3`    |
|  `'testresult'`  |  `'est'`   |    `1, 3`    |
|  `'ababcccdab'`  | `'abcccd'` |    `2, 6`    |
| `'abracadabra'`  |  `'abr'`   |    `0, 3`    |

**Hints:**
* There are many ways to solve this problem.
* It is often very helpful when trying to solve these more difficult problems to first try and think how it might be solved with 'paper & pencil'.
* Doing a 'paper & pencil' walk-through of a human-speak solution (yes I actually did do that) shows that just one iteration through the list is all that is needed but there are several things to keep track of at the same time:
  * the start index of the longest substring found so farl
  * the end index (or length) of the ongest substring found so far
  * the start index of the current substring
  * the index of the current character being examined
* Your algorithm may be different and that would be fine but I strongly urge you to do a walkthrough on paper before even thinking of touching the computer

## mergen_short()

Interleave the successive characters of **any number** of strings of **any length** into a single string and return the result. 
Interleaving is halted when the shortest string is exhausted.

For example:

|             parameter values             |    return value     |
|:----------------------------------------:|:-------------------:|
|               `'', '', ''`               |        `''`         |
|           `'abc',  'd',  'ef'`           |       `'ade'`       |
| `'abc_', 'defg', 'hjkmn', 'pqr', 'stuv'` | `'adhpsbejqtcfkru'` |

**Hints:** The problem has many similarities to the previous `mergeX()` problems but this time there can be any number of parameter strings, and they can all be different lengths. 

So some immediate problems to solve are:
1. How do functions that take any number of parameters work?
2. How to stop the iteration when the shortest string is exhausted?
3. How to merge an arbitrary number of strings?

Functions that take an arbitrary number of argument parameters are described in the Python tutorial at [4.8.4. Arbitrary Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists) and at [w3schools](https://www.w3schools.com/python/python_functions.asp) (a little way down the page). The short explanation is that the function definition should look like:

```python
def f_name(*args):
    # code
    return 
```

The strings will then be available within the function body as the elements of a list called `args`. So this
function will have an outline structure like this:

```python
def merge_short(*args):  # 'args' is traditional, it can be any variable name
    for each_arg in args:
        # do stuff
        pass
    # do more stuff . . . code goes here . . . 
    return 'result and stuff'
```

## mergen_long()

Interleave the successive characters of **any number** of strings of **any length** into a single string and return the result. As individual strings become exhausted, continue interleaving with the remaining strings until all are exhausted.

For example:

|             parameter values             |       return value       |
|:----------------------------------------:|:------------------------:|
|               `'', '', ''`               |           `''`           |
|           `'abc',  'd',  'ef'`           |        `'adebfc'`        |
| `'abc_', 'defg', 'hjkmn', 'pqr', 'stuv'` | `'adhpsbejqtcfkru_gmvn'` |

**Hints:**
* Much of the structure of the function mergen_long()is similar to mergen_short() but with an additional check before a character is added to the result.
* The value of the variable `index` used to access elements of the strings will start at zero and successively increment to the last element of the longest string. Because some strings may be shorter than the longest string, we need to check that `[index]` is not beyond the end of the string before attempting to access any string. 


# Difficult Questions
These last questions are more difficult. 

## get_all_words(a_str)

The parameter is guaranteed to be 

## pluralizer(a_str)

The parameter is guaranteed to be a word. A string with no spaces. Return the plural of that word.

**Test Data:**
Banana, Leaf, Trolley, Lorry, Sheep, Church, Sausage, Monkey, Knife, Child, Match, Poppy
