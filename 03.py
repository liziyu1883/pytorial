"""Python Tutorial Chapter 6 to Chapter 7"""

import fibo  # Module 01
import builtins  # Module 02

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
    print(repr(x).rjust(3), repr(x*x).rjust(4), end=' ')
    print(repr(x*x*x).rjust(5))

# str.format() can assign values to placeholder {} in a string; numbers in {} indicates locus in str.format()
print('We are the {} who say "{}!"'.format('lions', 'Roar'))
print('We are the {1} who say "{0}!"'.format('Ni', 'knights'))
print('{name} used her spell card {sc}!'.format(name='Marisa', sc='Master Spark'))






