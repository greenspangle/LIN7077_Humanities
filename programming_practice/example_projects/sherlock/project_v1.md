# My Project
## iteration 1

See assignment 5 for my project definition and objectives.

In a nutshell, it is to explore the text of the novels of Arthur Conan Doyle.

## Introduction
I downloaded the text of 'a Study in Scarlet' from Project Gutenberg 
[www.gutenberg.org] and edited it to remove copyright and licence notices 
using a simple text editor.

* 23 lines of text from the beginning of the file
* 351 lines of text from the end of the book

The remaining text of the book is then a file of 4740 lines consisting of a 
total of 239,249 characters. (As measured by my text editor)

## Reading the file into Python
As the file is of very modes size, I decided to read it into a single string.
The alternative would be to read it into a list of strings, one strig for each 
line of the book, but that seemed to be introducing additional complexity for 
no good reason.

A sketch of the code to do this is:

```python
with open('scarlet.txt', mode='r', encoding='utf-8') as book_file:
    book = book_file.read()
    


```
