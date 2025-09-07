# The python turtle (fun)

Create a new python script and call it turtle1.py and add this fun piece
of code:

```python
from turtle import *

def sq(pen_color, fill_color):
    color(pen_color, pen_color)
    begin_fill()
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    end_fill()
```

Use IDLE to execute this program and test it works by calling the
function sq()
```
sq('blue', 'green')  # choose any standard color
```

There are many more methods for the turtle. You can create many turtles have all the turtles drawing at the same time. You can define your own functions to draw ready-made shapes and patterns (your initials perhaps).

There are many fun Turtle tutorials on the web.
