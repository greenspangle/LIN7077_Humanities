# Practice Worksheet for Collections

## Text Strings

Text objects in Python are called 'strings' and can be created in any one of several ways:

|          how          |           example            |
|:---------------------:|:----------------------------:|
|     single quotes     |   `'this is a str object'`   |
|     double quotes     |   `"this is a str object"`   |
| triple single quotes  | `'''this is a str object'''` |
| triple double quotes  | `"""this is a str object"""` |
| the built-in function |      `str(any_object)`       |

Try the following statements in IDLE:

Strings are indexable.

``` python 

    >>> a = 'abracadabra'
    >>> a[0]
    'a'
    >>> a[1]
    'b'
    >>> a[3:]
    'acadabra'
    >>> a[2:5]
    'rac'
    >>> a[3:-3]
    'acada'
    >>> a[::2]
    'arcdba'
    >>> a[::-2]
    'abdcra'
```

Strings can be tested for substrings using the 'in' operator and for the number of characters they contain
using the builtin function len():

``` python

    >>> 'cad' in a
    True
    >>> 'dac' in a[::-1]
    True
    >>> len(a)
    11
    >>> len(a[1:-2:3])
    3
```

Strings have many methods:

``` python

    >>> a.capitalize()
    'Abracadabra'
    >>> a.center(20, '~')
    '~~~~abracadabra~~~~~'
    >>> a.count('b') == a.count('r')
    True
    >>> a.find('r')
    2
    >>> a.isalpha()
    True
    >>> a.isidentifier()
    True
    >>> a.isdecimal()
    False
    >>> a.partition('d')
    ('abraca', 'd', 'abra')
    >>> a.replace('a', 'A', 2)
    'AbrAcadabra'
    >>> a.split('a')
    ['', 'br', 'c', 'd', 'br', '']
    >>> a.swapcase().capitalize()
    'Abracadabra'
    >>> a.capitalize().swapcase()
    'aBRACADABRA'
```

## Tuples

Tuple objects can be created in several ways:

|       how        |        example         |
|:----------------:|:----------------------:|
|     tuple()      | `tuple('an iterable')` |
|     brackets     |          `()`          |
| a trailing comma |          `2,`          |
|      commas      |      `2, 5, 7, 3`      |

Try the following statements in IDLE and explain the results:

 ``` python
 
    >>> t1 = tuple('abracadabra')
    >>> t2 = tuple('shazam')
    
    >>> t1
    ('a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a')
    
    >>> t1 + t2
    ('a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a', 's', 'h', 'a', 'z', 'a', 'm')
    
    >>> t1[1]
    'b'
    
    >>> t1[3:] *3
    ('z', 'a', 'm', 'z', 'a', 'm', 'z', 'a', 'm')
    
    >>> t1[-1::-2]
    ('a', 'b', 'd', 'c', 'r', 'a')
    
    >>> len(t1)
    11
    
    >>> t2[3] not in t1
    True
    
    >>> max(t1) > max(t2)
    False
    
    >>> type(())
    <class 'tuple'>
 ```

## Lists

List objects can be created in several ways:

|                         how                          |                        example                         |
|:----------------------------------------------------:|:------------------------------------------------------:|
|                   square brackets                    |                 `[]` # the empty list                  |
| square brackets, separating <br/>  items with commas |                   `[a]`, `[a, b, c]`                   |
|                        list()                        | `list()  # the empty list` <br/> `list('an iterable')` |
|                 a list comprehension                 |                `[x for x in iterable]`                 |

Try the following statements in IDLE:

``` python

    >>> lst01 = []
    >>> lst02 = list()
    >>> lst03 = list('')
    >>> lst01 == (lst01 == lst02) and (lst02 == lst03) and (lst01 == lst03) 
    True 
     
    >>> lst1 = list('abracadabra')
    >>> lst2 = list('Shazam')
    >>> len(lst1) > len(lst2)
    True
    
    >>> lst1+lst2
    ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a', 'S', 'h', 'a', 'z', 'a', 'm']
    
    >>> lst2[:2] +lst2[3:4] * 7 
    ['S', 'h', 'z', 'z', 'z', 'z', 'z', 'z', 'z']
    >>> lst2[:2] +lst2[3] * 7  # DOES NOT WORK, - WHY
    Traceback . . . type error . . .
    
    >>> lst1[6] = 'D'
    >>> ''.join(lst1)
    'abracaDabra'
    
    >>> lst1copy = lst1.copy()
    >>> lst1copy.insert(1, 'X')
    >>> ''.join(lst1copy)
    'aXbracaDabra'
	
    >>> lst1copy.reverse(), ''.join(lst1copy)
    (None, 'aXbracaDabra')
    
    >>> lst1.count('a')
    5
	
	>>> a=[3,2,1]
	>>> a.sort()
	>>> a
	[1, 2, 3]
```

## Ranges

## Ranges

https://docs.python.org/3/library/stdtypes.html#ranges

Range objects can be created in two ways:

|      how      |                   example                    |
|:-------------:|:--------------------------------------------:|
|    {items}    |       `{'ant', 'bee', 'caterpillar'}`        |
| set(iterable) | `set('Shazam')` <br/> `set(range(1, 20, 3))` |

Find the examples in the Python documentation and execute them in IDLE


Range objects are created using the range function and iterating through the elements of the range using a `'for'` loop.

```python

r7 = range(7)
for i in r7:
    print(i)
    
# or more concisely

for i in range(7):
    print(i)

# Note that a range() object can only be iterated once.
# trying to do so a second time will cause an exception
```

Find the examples in the Python documentation and on w3schools and execute them in IDLE

## Sets

Set objects can be created in two ways:

|      how      |                   example                    |
|:-------------:|:--------------------------------------------:|
|    {items}    |       `{'ant', 'bee', 'caterpillar'}`        |
| set(iterable) | `set('Shazam')` <br/> `set(range(1, 20, 3))` |

Find the examples in the Python documentation and execute them in IDLE. In particular do familiarise yourself with the set operations. For example, create the sets `a = set(range(1, 100, 5'))`, `b = set(range(1, 100, 3'))` and `c = set(range(1, 100, 5'))` and create some set unions, set intersections and some compliments

## Dictionary

Read the python documentation at https://docs.python.org/3/library/stdtypes.html#dict and practice creating some dictionaries and exploring the dictionary methods.

I need to say more than that!



# Transforming Collections

Transforming one type of collection into another.

* To create a `range(i)` collection, `i` must be an integer. In these examples I have used the number of
  items in the source collection as the required integer.
* Some of these transformations result in information loss: `range()` reduces everything to a sequence of integers, `set()`
removes any duplicates, and dictionary transformations force a two-dimensional structure into one dimension.

| To <br/>From |                    String                    |                  Tuple                   |                  List                  |      Range      |                 Set                  |     Dictionary     |
|:-------------|:--------------------------------------------:|:----------------------------------------:|:--------------------------------------:|:---------------:|:------------------------------------:|:------------------:|
| String s     |                      X                       |                `tuple(s)`                |               `list(s)`                | `range(len(s))` |               `set(s)`               | `dict.fromkeys(s)` |
| Tuple t      |                 `''.join(t)`                 |                    X                     |               `list(t)`                | `range(len(t))` |               `set(t)`               | `dict.fromkeys(t)` |
| List u       |                 `''.join(u)`                 |                `tuple(u)`                |                   X                    | `range(len(u))` |               `set(u)`               | `dict.fromkeys(u)` |
| Range r      |                 `''.join(r)`                 |                `tuple(r)`                |               `list(r)`                |        X        |               `set(r)`               | `dict.fromkeys(r)` |
| Set s        |                 `''.join(s)`                 |                `tuple(u)`                |                `list()`                | `range(len())`  |                  X                   | `dict.fromkeys()`  |
| Dictionary d | `''.join(d.keys())`<br/>`''.join(d.values()` | `tuple(d.keys())`<br/>`tuple(d.values()` | `list(d.keys())`<br/>`list(d.values()` | `range(len())`  | `set(d.keys())`<br/>`set(d.values()` |         X          |




# Practice, Practice, Practice
The more, the better.

## Range
https://www.w3schools.com/python/ref_func_range.asp
https://snakify.org/en/lessons/for_loop_range/

## Lists
https://www.w3schools.com/python/python_lists.asp  
https://snakify.org/en/lessons/lists/  
https://snakify.org/en/lessons/two_dimensional_lists_arrays/  

## Tuples
https://www.w3schools.com/python/python_tuples.asp  

## Sets
https://www.w3schools.com/python/python_sets.asp  
https://snakify.org/en/lessons/sets/  

## Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp  
https://snakify.org/en/lessons/dictionaries_dicts/  





