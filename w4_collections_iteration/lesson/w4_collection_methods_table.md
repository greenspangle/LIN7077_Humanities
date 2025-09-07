# Collection &#8644; Collection

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



| <br/>&#8667;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To <br/>&#10507; From |                  String                  |                Tuple                 |                List                |     Range     |               Set                |    Dictionary    |
|:----------------------------------------------------------------|:----------------------------------------:|:------------------------------------:|:----------------------------------:|:-------------:|:--------------------------------:|:----------------:|
| String s                                                        |                    X                     |               tuple(s)               |                list                | range(len(s)) |              set(s)              | dict.fromkeys(s) |
| Tuple t                                                         |                ''.join(t)                |                  X                   |              list(t)               | range(len(t)) |              set(t)              | dict.fromkeys(t) |
| List                                                            |                ''.join(u)                |               tuple(u)               |                 X                  | range(len(u)) |              set(u)              | dict.fromkeys(u) |
| Range r                                                         |                ''.join(r)                |               tuple(r)               |              list(r)               |       X       |              set(r)              | dict.fromkeys(r) |
| Set s                                                           |                ''.join(s)                |               tuple(u)               |               list()               | range(len())  |                X                 | dict.fromkeys()  |
| Dictionary d                                                    | ''.join(d.keys())<br/>''.join(d.values() | tuple(d.keys())<br/>tuple(d.values() | list(d.keys())<br/>list(d.values() | range(len())  | set(d.keys())<br/>set(d.values() |        X         |
