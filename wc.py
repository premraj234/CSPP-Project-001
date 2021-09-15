"""Implementing the wc shell command in python."""

"""The import statement the import sys imports the library sys from the module along with the functions and methods of the library system"""
import sys

"""... from the lib.helper module we are importing the built in functions cat and readfile of the lib-helper module into our source code"""
from lib.helper import wc, readfile

"""text is a variable assigned with a non type value""" 
TEXT = None

"""ARG_CNT is a variable is assigned with int value len(sys.argv) - 1.len() takes one argument as input and returns lenght of given input"""
ARG_CNT = len(sys.argv) - 1

"""if statement is used to check the condition and execute it if the condition is true if ARG_CNT value is 0 then it reads the input using standard input function"""
if ARG_CNT == 0:
    TEXT = sys.stdin.read()

"""the below if statement checks the condition of ARG_CNT is equals to 1 if it is satisfied it executes the the first line sys.argv[1] it returns the filename and stores data"""
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
"""Because there are multiple arguments in the response, a character space is added between them"""
response = wc(TEXT)
print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]))