"""Python Tutorial Chapter 6 to Chapter 8"""

import fibo  # Module 01
import builtins  # Module 02
import math  # Module 03

"""module"""

"""
module is a file containing definitions and statements
statements in the module will only execute at the first time the module name is in an import statement
thus statements in a module are intended to initialization
within a module, the module's name, as a string, is available as the value of the global variable __name__
we imported Module 01 at beginning, which calculates the Fibonacci numbers
"""

fibo.fib(1000)
print(fibo.fib2(100))
print(fibo.__name__)
fib = fibo.fib  # it's possible to store a function conveniently from a module
fib(500)

"""
to import a module, alternatively, we can use from fibo import fib, fib2
or from fibo import *, which imports all names except names beginning with _
we can run a module as an independent script: see fibo.py for details
once there is an import statement, Python searches built-in module first, then name.py in the directories of sys.path
sys.path contains: script directory, PYTHONPATH, installation-dependent default; can be modified
to speed up loading, Python caches the complied module in __pycache__ under module.version.pyc
Python doesn't check cache when the module is loaded in the command line or the module doesn't have a source
"""

"""sys"""
# import sys  # Module 02
# sys.ps1, sys.ps2 modifies the two strings of primary and secondary prompt in interaction mode
# sys.path.append() gives one more path for storing module

"""dir()"""
print(dir(fibo))  # gives all the names a module defines
print(dir(builtins))  # to print all built-in modules, import Module 02 first

"""package"""
# package is a collection of modules; dotted name: A.B means a sub-module named B in a package named A
# the __init__.py defines a list __all__ that contains module names being imported when calling: from XX import *
# __path__ gives a predefined path before running the module that might be modified

"""string formatting"""
# we can use str() or repr() to convert anything into a string; str() is for human reading and repr() is for computers
# repr() of a string contains quotes and backslashes
print('Azuki\n')
print(str('Azuki\n'))
print(repr('Azuki\n'))

# we can use methods str.rjust() str.ljust() and str.center() to format a string
print('  x   x^2   x^3')
for x in range(1, 11):
    print(repr(x).rjust(3), repr(x * x).rjust(4), end=' ')
    print(repr(x * x * x).rjust(5))

# str.format() can assign values to placeholder {} in a string; numbers in {} indicates locus in str.format()
print('We are the {} who say "{}!"'.format('lions', 'Roar'))
print('We are the {1} who say "{0}!"'.format('Ni', 'knights'))
print('{name} used her spell card {sc}!'.format(name='Marisa', sc='Master Spark'))
# we can convert the text value by !a, !s and !r; each corresponding to ascii(), str(), repr()
spell_marisa = 'Master Spark'
print('Kirisame Marisa used {!a}.'.format(spell_marisa))
# we can use : to call for additional format; Module 03 is used here to show the number pi to 5 digits after decimal
print('PI = {0:.5f}'.format(math.pi))

# put an inter after : will give a minimum number of characters wide, which makes tables pretty
spell = {'Final Spark': 1000, 'Hourai Doll': 800, 'Philosopher\'s Stone': 600}
for name, power in spell.items():
    print('{0:25} ==> {1:10d}'.format(name, power))  # d in the second format means increasing order

"""file"""

"""
open() returns a file object; open(filename, mode)
filename is the string containing the filename
mode: 'r' reading only; 'w' writing only; 'a' appending only; 'r+' both reading and writing;
mode will be 'r' if omitted
files are mostly opened in text mode, with line ending converted to \n; possible to open files in binary mode
fr.read() will return the entire contents of the file
fr.readline() will return a single line; it returns an empty string at the end of file
to read all lines use list(fr) or fr.readlines()
"""

fr = open('frexp', 'r')  # fr is an example file object of a reading only file

fr.readline()  # read the first line silently
fr.readline()  # read the second line silently
print('\n' + fr.readline(), end='')  # read the third line and print
#  we can even loop through the file objects
for line in fr:
    print(line, end='\n')

fw = open('fwexp', 'w')  # fw is an example file object of a writing only file

"""
fw.write(string) writes the contents of a string to the file, returning the number of characters written
objects other than string must be converted by str() before writing
fw.tell() gives the number of bytes from beginning if in binary mode
use fw.seek(offset, from_what) to go to a specific position;
offset is regarding to a reference point with 0 the reference position and +/- a number to another position
from_what=0 means reference at beginning; =1 reference means at current position; =2 means at the end of the file
in text mode, only seek from beginning is allowed except seek(0,2); only valid offset values are returned from f.tell()
"""

fw.write('It\'s the first line of a test. \n')
print(fw.tell())  # since we are in text mode instead of binary mode, fw.tell() tells nothing

# always close the files after using them
fr.close()
fw.close()

# it's convenient to use the with keyword when handling with files as it automatically close the file after handling
with open('frexp', 'r') as f:
    read_data = f.read()

print(read_data)

# JSON = JavaScript Object Notation can be used to serializing/de-serializing a a file/data

"""exception"""
# error detected during execution; example: 1/0, undefined identifier, '2'+2
