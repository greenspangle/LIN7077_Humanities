# LIN7077 additional Sequence questions for practice

## magic3()

This function takes no parameters and answers the integer 3 every time it is called. For example:

| Parameter Value | Return value |
|:---------------:|:------------:|
|                 |      3       |
|                 |      3       |

## magic5(a)

This function takes a single parameter and answers the integer 5 every time it is called. For example:

| Parameter Value | Return value |
|:---------------:|:------------:|
|       11        |      5       |
|        5        |      5       |
|     'fifty'     |      5       |

## magic7(a)

This function takes either one or zero parameters and answers the integer 7 every time it is called.

| Parameter Value | Return value |
|:---------------:|:------------:|
|                 |      7       |
|        5        |      7       |
|     'fifty'     |      7       |



## times_2(parameter)

This function takes a single argument and returns twice that value. The parameter is guaranteed to be either
an integer, a float or a string.

For example:

| arguments | return value |
|:---------:|:------------:|
|     7     |      14      |
|    7.0    |     14.0     |
|    'x'    |     'xx'     |
## cent_to_fahr(temp)

Converts a temperature in Celsius to Fahrenheit. 
One degree Celsius is 9/5 degrees fahrenheit.
Freezing point is 0C and 32F, and boiling point is 100C and 212F
For example:

| Centigrade | Fahrenheit |
|:----------:|:----------:|
|     0      |     32     |
|    100     |    212     |
|     30     |     86     |
|    40.3    |   104.54   |

## lucky_fun(lucky_int)

This function accepts an integer parameter `lucky_int` and returns a function.

The returned function accepts an integer parameter and answers boolean True if the
sequence of digits comprising `lucky_int` occurs within its given parameter. False otherwise.
For example:

        lucky_1 = lucky_fun(7)  # returns a function and assigns it to the varable name lucky_1
        lucky_1(11711)  # returns True
        lucky_1(11511)  # returns False
        lucky_1(0)  # returns False
    
        lucky_2 = lucky_fun(11)  # returns a function and assigns it to lucky_2
        lucky_2(11511)  # returns True 
        lucky_2(15151)  # returns False - no two 1's are adjacent 
        lucky_2(43-32)  # returns True

---
END of additional questions
---