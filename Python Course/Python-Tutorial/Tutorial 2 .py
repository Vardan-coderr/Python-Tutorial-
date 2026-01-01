# In these Titorial we learn about Escape Sequence ,Comments and print staements on Python :-

# Comments in python :- Comments  are used for coders to understand the code easily and it is not excute in your program
# There are two types of comments in python:-
# 1. Single line comment :- it is used for single line comments and it is done by using (#)symbol 
# 2. Multi line comment :- it is used for multiple line comments and it is done by using (''' ''') or (""" """) symbol

# Example of Single line comment
# This is a single line comment
print("Hello World!") # This is also a single line comment

# Example of Multi line comment
'''
This is a multi line comment
This is also a multi line comment
This is also a multi line comment
'''


# Escape Sequence are used to give some special meaning to the characters :-

 # \n is use for new line in code (\n) and it is a Escape sequence 
print("Hey I am a Good Boy  \nand The Viewer Who see This code is also a Good boy")
#  \"  code \" this is use for double quote in code (\")
print("Hey I am a \"Good Boy\" and The Viewer Who see This code is also a  \"Good boy \"")
#  \'  code \' this is use for single quote in code (\')
print('Hey I am a \'Good Boy\' and The Viewer Who see This code is also a  \'Good boy \'')
# \\  code \\ this is use for backslash in code (\\)
print("Hey I am a \\Good Boy\\ and The Viewer Who see This code is also a  \\Good boy \\")
# \t  code \t this is use for tab space in code (\t)
print("Hey I am a \tGood Boy\t and The Viewer Who see This code is also a  \tGood boy \t")
# \r  code \r this is use for carriage return in code (\r)
print("Hey I am a \rGood Boy\r and The Viewer Who see This code is also a  \rGood boy \r")
# \b  code \b this is use for backspace in code (\b)
print("Hey I am a \bGood Boy\b and The Viewer Who see This code is also a  \bGood boy \b")
# \f  code \f this is use for form feed in code (\f)
print("Hey I am a \fGood Boy\f and The Viewer Who see This code is also a  \fGood")
# \v  code \v this is use for vertical tab in code (\v)
print("Hey I am a \vGood Boy\v and The Viewer Who see This code is also a  \vGood boy \v")


# More on Print statements in python :-

# The print() function is used to print the output on the screen
# Syntax of print() function is :- print(object(s), sep=separator, end=end, file=file, flush=flush)
# Here,
# object(s) :- it is the object to be printed
# sep=separator :- it is used to separate the objects
# end=end :- it is used to end the print statement
# file=file :- it is used to write the output to a file
# flush=flush :- it is used to flush the output buffer

# Example of print() function :-
print("Hello World!") # Here, "Hello World!" is the object to be printed

print("Hello", "World!", sep="-") # Here, "Hello" and "World!" are the objects to be printed and "-" is the separator

print("Hello", "World!", end=" ") # Here, "Hello" and "World!" are the objects to be printed and " " is the end

import sys
print("Hello", "World!", file=sys.stdout) # Here, "Hello" and "World!" are the objects to be printed and sys.stdout is the file
# Note :- To use file=sys.stdout you need to import sys module

print("Hello", "World!", flush=True) # Here, "Hello" and "World!" are the objects to be printed and True is the flush


