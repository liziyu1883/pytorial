"""Python Tutorial Chapter 5"""

from collections import deque  # Module 01
from math import pi  # Module 02

"""list"""
a, b = [2, 4, 6, 8], [1, 3, 5, 7]

a.append(10)  # add an item at the end of the list
print(a)

a.extend(b)  # appending a whole list at the end of a
print(a)

a.insert(2, 5)  # insert 5 to the position index 2 and move the previous item of position 2 to position 3; return None
print(a)

a.remove(5)  # remove the first item in the list whose value is 5; return None
print(a)

c = a.pop()  # remove the last item if no value assigned to pop() and return the removed value
print(a, c)

a.pop()  # if we do not assign a.pop() to some object, only the last item is removed
print(a)

c = a.pop(5)  # remove the item with index 5 and return the removed value
print(a, c)

a.clear()  # remove all items from the list
print(a)

a = [8, 4, 6, 2]

c = a.index(4)  # return the index of the first item whose value is 6; if not exist, return an error
print(a, c)

a.reverse()  # reverse the list
print(a)

a.sort(key=None, reverse=False)  # sort the items of the list in place; return None
print(a)

c = a.copy()  # return a copy of the list a
print(a, c)

del a[0]  # delete the 0th term of a without returning the value of the 0th term
print(a)

a.extend(c)
print(a)
del a[3:5]  # delete the 3rd and 4th terms
print(a)
del a[:]  # clear a
print(a)

del a  # this will remove the variable completely
# print(a) will raise an error saying name 'a' is not defined

"""
it's convenient to use lists as stacks: the last element added to the list will be the first element retrieved later
to add an item, use a.append(); to remove an item, use a.pop()
the (conventionally speaking) top of the stack is actually at the end of the list
it's also possible to use lists as queues: the first element added to the list will be the first one retrieved later
however, lists are not efficiently handled as queues
because each time retrieving something from the beginning, all the other elements have to be shifted by one
use collections.deque to fast appending and popping from both ends (using Module 01)
"""

prime = deque([0, 1, 2, 3, 5, 7, 11, 13, 17, 19])
prime.append(23)
b = [29, 31, 37]
prime.extend(b)
prime.popleft()  # pop the first item
prime.popleft()
print(prime)

# we can create a list by loops
squares = []
for i in range(1, 10):
    squares.append(i ** 2)
print(squares)

# but there's more concise methods
squares_concise = list(map(lambda x: x ** 2, range(1, 10)))
print(squares_concise)

# or equivalently
squares_more_concise = [x ** 2 for x in range(1, 10)]  # called a list comprehension
print(squares_more_concise)

# list comprehension has the form: [(expression) for/if clause], with each expression parenthesized like (x, y, z, ...)
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 4, 5] if x != y]  # all pairs (x,y) from two sets with different value
print(pairs)

# list comprehensions can contain complex expression (using Module 02)
pi_round = [str(round(pi, i)) for i in range(1, 8)]
print(pi_round)

matrix_row = [  # each sublist is a row of the matrix
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix_row)

matrix_column = [[row[i] for row in matrix_row] for i in range(4)]  # transpose matrix_row into a collection of columns
print(matrix_column)

matrix_column_zip = list(zip(*matrix_row))  # zip() function does the transpose with * unpacking the matrix
print(matrix_column_zip)  # note that [1, 5, 9] is written as a tuple (1, 5, 9) (instead of sublist) with zip()

"""tuple"""
# list and string are two examples of the sequence data type; tuple is also a sequence data type and is immutable
t = 12345, 67890, 'number', 'integer'  # t is then a tuple
print(t)

t_nested = t, (765, 432, 'another tuple')
print(t_nested)

# t[1] = 6789 raise an error as tuple is immutable
t_mutable_object = ([3, 7, 1], [4, 5, 6])  # but a tuple can contain other mutable objects
print(t_mutable_object)

t_empty = ()
t_singleton = 'hello',  # need a comma
a, b = t_mutable_object  # unpacking a tuple: the number of variables on the LHS must agree with the tuple on RHS

"""set"""
# set is a data type that is unordered with no duplicate elements
set_prime = {2, 3, 5, 7, 3, 11, 13, 17, 17, 19}
T_bool = 11 in set_prime  # returns True
F_bool = 12 in set_prime  # returns False
print(set_prime)  # repeated elements are combined

set_empty = set()  # cannot use set_empty = {} as it creates an empty dictionary

c = set('is_a_good_idea')
print(c)  # it will decompose a string into unique letters
d = set('not-trivial_idea')

diff_cd = c - d  # gives the letters that is in a but not in b
union_cd = c | d  # either in c or d
intersection_cd = c & d  # both in c and d
intersection_complementary_cd = c ^ d  # in c or d but not both
print(intersection_complementary_cd)

c = {x for x in 'not_a_good_idea' if x not in 'god'}

"""dictionary"""
# dictionaries are indexed by keys, which can be any immutable type like strings and numbers
# a dictionary is an unordered key:value pairs; this requires keys to be unique within one dictionary
# if we store value into an existing key, the old value will be forgotten

pokemon = {'Bulbasaur': 1, 'Ivysaur': 2, 'Venusaur': 3, 'Charmander': 4, 'Charmeleon': 5, 'Charizard': 6}
print(pokemon['Ivysaur'])
pokemon_names = list(pokemon.keys())  # all the keys in random order
pokemon_names_sorted = sorted(pokemon.keys())  # in sorted order
pokemon = dict([('Squirtle', 7), ('Wartortle', 8), ('Blastoise', 9)])  # can also be generated by dict()
dict_prime_power = {x: x ** 2 for x in (2, 3, 5, 7, 11)}  # dictionary comprehension
print(dict_prime_power)

# it's possible to retrieve the key and value at the same time using items()
for key, value in pokemon.items():
    print(key, value)

"""looping"""
# use enumerate() to a sequence will get the corresponding index and value
for index, value in enumerate(a):
    print(index, value)

# to loop over two or more sequences at the same time, we use the zip() function
















