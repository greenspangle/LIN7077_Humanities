# Practice - Reading & Writing Text Files

Python can read and write text files and binary files (images, video, audio,
etc.,).
We will only be studying text files which are python's default.

When practicing file processing do also make use of web learning resources such
as [realpython's - guide to reading and writing files](https://realpython.com/read-write-files-python/) , [w3schools file handling](https://www.w3schools.com/python/python_file_handling.asp),
and of course the documentation
at [python.org](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).

## Writing Text Files

### write()

**Warning:** Opening a file for `'write'` will **DELETE** the contents of the
file if it already exists. Even if you write nothing to the file, its
existing contents will be deleted.

Here is some sample code to create and write a string of text to a file. Write a
Python script containing this code and save it to a convenient location in your
file system. The file this code will create will be written to the same folder
so make sure you know where that is.

```python
with open('myfile1.txt', 'w') as my_f:
    my_f.write('write this text to my file')
```

Now run the script and look in the folder where you saved it. There should be a
new file there called 'myfile1.txt'. Open it with notepad or textedit and read
the contents. It should be 'write this text to my file'.

Change the code and run it again to see the changes.

```python

with open('myfile1.txt', 'w') as my_f:
    my_f.write('some different text written to myfile1.txt')
```

The file 'myfile1.txt' now contains the text 'some different text written to
myfile1.txt'. The original contents have been deleted.

Let's create another file and write more text to our file:

```python
with open('myfile2.txt', 'w') as my_f:
    my_f.write('This is myfile2.txt')
    my_f.write('1 more text added to my file')
    my_f.write('2 more text added to my file')
    my_f.write('3 more text added to my file')
    my_f.write('4 more text added to my file')
```

Run the code, find the file in file explorer, and open it.
You will see that although you wrote five separate `write()` statements,
everything is on one line!

To write the individual strings to separate lines it is necessary to add an
explicit newline character to each string. The newline character is `'\n'`.

```python
with open('myfile3.txt', 'w') as my_f:
    my_f.write('This is myfile3.txt\n')
    my_f.write('1 more text added to my file\n')
    my_f.write('2 more text added to my file\n')
    my_f.write('3 more text added to my file\n')
    my_f.write('4 more text added to my file\n')
```

The file 'myfile3.txt' does contain multiple lines.

You can see all of Pythons escape sequences at:
[Python escape sequences](https://docs.python.org/3/reference/lexical_analysis.html#index-23)

## Appending to a file

The append option adds text to the end of the file.

```python
with open('myfile1.txt', 'a') as my_f:
    my_f.write('appended this text to the the end of my file\n')
```

Open the file in notepad or textedit toconfirm that the text has been added.

### writelines()

Writes the contents of a collection to a file.
Let's use it to append multiple lines to the file 'myfile1.txt'.

```python
list_of_str = ['5 moretext\n', '6 moretext\n', '7 moretext\n', '8 moretext\n']
with open('myfile1.txt', 'a') as my_f:
    my_f.writelines(list_of_str)
```

Open the file and read it to confirm the code executed correctly.

## Reading Text Files

### read()

Reads the whole file into a single string.

Create this script in the same folder as the text file we just created:

```python
with open('myfile1.txt', 'r') as my_f:
    contents = my_f.read()
    print('Contents is an object of type:', type(contents))
    print(contents)
```

### readlines()

Reads the file, a line at a time, into a list.

```python
with open('myfile1.txt', 'r') as my_f:
    contents = my_f.readlines()
    print(contents[2])  # print the line of the file
    for each_line in contents:
        print(each_line)
```

### for each_line in file:

There is also a convenient 'pythonic' way of reading a file a line at a time
using a for loop:

```python
with open('myfile1.txt', 'r') as my_f:
    for each_line in my_f:
        print('variable eachline is an object of type:', type(each_line))
        print(each_line)
```

## File Path Names

So far all the files we have written, or read, or appended to, have been in the
same folder as the script.
If we want to write the file to a different folder things get more complicated.

Unfortunately a statement such as:

```python
with open(r'\temp\pythonstuff\myfile1.txt', 'w') as my_f:
    my_f.write('write this text to my file')
```

Does not work and produces the syntax error:

```
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    with open(r'\temp\mystuff\myfile.txt', 'w') as my_f:
FileNotFoundError: [Errno 2] 
       No such file or directory: '\\temp\\mystuff\\myfile.txt'
```

To fix this we need to use the OS module from the standard library:

```python
import os

file_path = os.path.join(os.sep, "temp", "sub1", "sub2", "example1.txt")
print(file_path)
```

This module copes with the differences between operating systems. Windows uses
the backslash "\" as a file separator, Unix and MacOS use the forward slash "/".
This module automatically detects the OS and uses the correct separator.
That means that the same code will work on all operating systems.

```python
import os

file_path = os.path.join(os.sep, "temp", "sub1", "sub2", "example1.txt")
print(file_path)
with open(file_path, 'w') as my_f:
    my_f.write('write this text to my file')
```

## Summary Table

This table summarises the most used file methods for reading and writing text
files:

| Method       | What it does                                                                        |
|--------------|-------------------------------------------------------------------------------------|
| read()       | reads the whole file all at once <br/> regardless of how big it is                  |
| readline()   | reads a single line                                                                 |
| readlines()  | reads the whole file into a list<br/> every line of the file is an item in the list |
| write()      | writes a string to the file                                                         |
| writelines() | writes a list of strings to the file                                                |

# A short diversion to Unicode.

[www.unicode.org](www.unicode.org)

Unicode is a very successful attempt to
represent [every character of every language](https://www.unicode.org/charts/)
in a form that can be manipulated in a computer. It also now
includes [emojis](https://www.unicode.org/emoji/charts/emoji-list.html).

For an introduction see the lesson
at [https://realpython.com/python-encodings-guide/](https://realpython.com/python-encodings-guide/)

The examples below print the character sets for Arabic, Bengali, and Ancient
Egyptian Hieroglyphs. You can find the codes for many other character sets
at [unicode.org/charts/](https://unicode.org/charts/) .

NOTE: the code numbers for the Unicode characters is
a [HEXADECIMAL](https://en.wikipedia.org/wiki/Hexadecimal) number. That is a
number to base 16 rather than the usual base 10. The 16 digits of hexadecimal
are '0123456789ABCDEF'. Python understands hexadecimal numbers provided they are
prefixed by `0x`. That means that the hexadecimal number `9E` (158 denary,
10011110 binary) is written `0x9E` in Python.

The Unicode Arabic character set:

```python 
def chars_arabic():
    """Print the Arabic character set (unicode 0600-06ff)"""
    print('\n\nThe Arabic character set:')
    code = 0x0600
    stop = 0x06ff
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()
```

The Unicode Bengali character set:

```python
def chars_bengali():
    """Print the Bengali character set (unicode 0980—09FF)"""
    print('\n\nThe Bengali character set')
    code = 0x0980
    stop = 0x09ff
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()
```

The Unicode Egyptian Hieroglyphs character set:

```python
def chars_hieroglyphs():
    """print the Egyptian Hieroglyphs character set (unicode 13000—1342F)"""
    print('\n\nThe Egyptian Hieroglyphs')
    code = 0x13000
    stop = 0x1342F
    while code < stop:
        print(chr(code), end=' ')
        code = code + 1
        if code % 32 == 0:
            print()
```

Find a character set for your language of choice and write a 'while' routine to
print them out.

Not every Unicode character set will have the been installed on your PC. If the
font is missing you will probably get a list of small empty rectangles printing
instead.

See the Unicode documentation for all the glorious details.

## Reading & Writing Unicode

The files we have been creating, writing to and reading from are encoded in a
way that is specific the OS we are using. This is convenient but if we intend
the files to be universally interchangeable we need to be specific about how the
file is encoded. Unless there is a special reason not to, this means using
Unicode.

Most text files intended for general purposed use are encoded using Unicode '
utf-8'. When reading and writing utf-8 files we need to
specify `encoding = 'utf-8'` option in the file open statement. Here is an
example:

```python
# Read the whole file
with open('filename.extension', mode='w', encoding='utf-8') as f:
    f.write('write this text to the file')
```

Open the above file in python, print out the first few dozen lines. Do you
recognise the text?

