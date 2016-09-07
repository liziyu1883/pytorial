"""Python Tutorial Chapter 1 to Chapter 4"""

"""number"""
power = 5 ** 2  # ** is the power operator, higher precedence than +/-
integer_division = 5 // 2  # // is the integer division operator; / will always return a float
complex_number = 3 + 6j  # Python has built in support for complex number, denoted by j or J
complex_number_a, complex_number_b = 2 + 4j, 7 + 8j  # multiple assignment
# in Python console, we can use the variable _ to indicate the last printed expression
# one should use _ as read only and never assign value to _ as it creates another local variable called _

"""string"""
string_quotes = 'String are represented inside single quotes, ' + "or double quotes. "
string_jump = 'It\'s okay to use \ to jump a single quotes. ' + "But let's use double quotes instead. "
print('I have a complex number read', complex_number)  # print connected by , will automatically lead to a space
raw_string = r'It\'ll be printed.'  # r'' makes a raw string that everything will be printed regardless of \
print("""\
Choose: Type    [OPTIONS]
         -g      group
         -r      ring
         -f      field\
        """)  # use triple quotes to create multiple line strings; the \ in first line prevent printing a new line
string_operator = 'nico' * 2 + 'ni' '~'  # * repeats string and two adjacent string add to each other
print(string_operator)
'''
strings are indexed: string_operator[0] = 'n', string_operator[-1] = '~' with negative index counting from right
string_operator[1:5] = 'icon' obtaining substring with character from 1 (included) to 5 (excluded) called slicing
string_operator[:5] + string_operator[5:] = 'niconiconi~'
indices are pointing between characters: 0 n 1 i 2 c 3 o 4 n 5 i 6 c 7 o 8 n 9 i 10 ~ 11
negative indices are 10 = -1, 9 = -2, etc.; slicing is obtaining the characters between the two indices
out-of-range slice indices are handled gracefully string_operator[10:50] = 'i~'
'''
# strings are immutable: assigning to an indexed position in the string results in an error
string_length = len(string_operator)

"""list"""
int_list = [1, 4, 9]  # indexed as strings
squares = int_list + [16, 25]
# lists are mutable - feel free assigning values to their entries
squares.append(36)  # add new item 36 to the end of the list
# we can change entries or clear strings by slicing
squares[1:3] = []  # changes squares to [1, 16, 25, 36]
squares[:] = []  # clear squares to []
list_length = len(squares)
int_nested = [int_list, int_list]  # creates a nested list [[1, 4, 9], [1, 4, 9]]

"""while"""
a, b = 0, 1
while b < 20:  # while loop executes as long as this is true
    print(b)
    a, b = b, a + b
else:
    print('end of series')  # executed when the while condition is false
# this gives the Fibonacci series

"""if"""
if power < 0:
    power = 0
    print('power of imaginary number')
elif power == 0:
    print('it\'s just zero')
elif power == 1:
    print('additional identity')
else:
    print('not interested')

# a blank line is required to indicate the completion of a block

"""for"""
# for loop works like an operator with a list as its domain
# x is a dummy variable representing a member of int_list; for loop execute in the index order of int_list
for x in int_list:
    if x > 2:
        print(x)
else:
    print('for-list exhausted')

# else of a for loop will execute until the exhaustion of the list

"""range()"""
inc = 0
for i in range(5):  # range(5) works as [0, 1, 2, 3, 4]
    inc += i

list_range = []
for i in range(5, 10):  # range(5,10) works as [5, 6, 7, 8, 9]
    list_range.append(i)

for i in range(10, 20, 3):  # range(min, max, step) works as [10, 13, 16, 19]
    list_range.append(i)

# to iterate over indices of a list/string, combine range() and len()
for i in range(len(int_list)):
    print(i + 1, int_list[i])

"""
note that, the result of print(range(5)) is range(0, 10) and obviously not a list
range() doesn't create a list but an object returning the successive items of a sequence when we iterate over it
we say range() is iterable and the for statement is an iterator
the function list() is also iterable and creates lists from iterable objects
"""
print(list(range(1, 30, 7)))

"""break"""
# breaks out of the smallest enclosing for or while loop
# inside a for/while-else structure, the else body won't be executed if the loop is terminated by break

"""continue"""
# continue the next iteration of the loop

"""pass"""
# pass statement is a void statement who does nothing, similar to a single ; in C++

"""function"""


def fib(n):  # def function(formal_parameter1, formal_parameter2, ...)
    """We want to print a Fibonacci series up to n."""
    # the previous line is the documentation string of the function fib()
    a, b = 0, 1  # defines two local variable stored in the local symbol table of fib()
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()  # this prints an empty line
    # looks like we do not have a return statement but every function returns a value; fib() returns None


fib(2000)  # calling fib() function
print(fib(500))  # executes fib(1000) and returns None

"""
we can only call but cannot assign a global variable within a function (unless named in a global statement)
when calling a variable, say b in fib(), first find it in the local symbol table fib(),
then the local symbol table of any mother function of fib(), then the global symbol table
the actual parameters (arguments), n = 2000 for example, are saved in the local symbol table when it is called
arguments are passed using call by value (value an object reference, not the value of the object)
when a function calls another function, a new local symbol table is created for that call
function name is a type recognized by the interpreter as a user-defined function
"""
f = fib  # we can assign function name like this
f(2000)  # this is exactly fib(2000)


def fib_list(n):
    """Return a list of Fibonacci series up to n."""
    ans = []
    a, b = 0, 1
    while a < n:
        ans.append(a)
        a, b = b, a + b
    return ans


f_list = fib_list(500)  # call the function
print(f_list)

"""
a method is a function belongs to an object and is written obj.method
different types have different methods that can have the same name without causing ambiguity
ans.append(a) calls a method of the list object ans, equivalent to ans = ans + [a]
"""

"""function argument"""
power = 4


def ask_ok(prompt, retry=power, reminder='Please try again!'):  # no space around = when assigning default value
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retry -= retry
        if retry < 0:
            raise ValueError('invalid user response')
        print(reminder)


power = 9
"""
in the function ask_ok, only the argument prompt is mandatory with the other two arguments having default value
however we can call anything if we don't want the default value like ask_ok('OK to delete all?', 5, 'yes/no only!')
the default values are evaluated at the point of function definition in the defining scope, and evaluated only once
so further change of power = 9 is not recognized by the function; the function only knows retry=4
however, if the default value is mutable, the value may change every time when we call the function
this can be prevented; see https://docs.python.org/3/tutorial/controlflow.html#default-argument-values for details
a function can also be called by keyword arguments like ask_ok(prompt='OK or not', retry=2)
however, mixing of keyword and non-keyword arguments is not allowed; we cannot have ask_ok(prompt='OK or not', 2)
"""


def menu(kind, *ent, **sides):  # *ent is a tuple, **sides is a dictionary containing all arguments apart from kind
    print('The kind is', kind + '. ')
    print('-' * 20, ' entree ', '-' * 19)
    for entree in ent:
        print(entree)
    print('-' * 20, ' sides ', '-' * 20)
    keys = sorted(sides.keys())  # we have to sort them first and print otherwise the order is undefined
    for sid in keys:
        print(sid, ":", sides[sid])


menu('Panda Express', 'Honey Walnut Shrimp', 'Shanghai Steak', s1='Veg Roll', s2='Chicken Roll', s3='Crab Rangoon')

# now consider the situation that the argument is already a list with each entries an argument
# we have to unpacking argument list by * operator and a dictionary by ** operator
args = [3, 6]
print(list(range(*args)))  # this is equivalent to print(list(range(3, 6))), * unpacking the list


def meal(kind, entree, side):
    print('This is a meal from', kind, 'with', entree, 'and', side + '. ')


dic_menu = {'kind': 'Panda Express', 'entree': 'shrimp', 'side': 'rangoon'}
meal(**dic_menu)  # ** unpacking the dictionary

"""lambda"""


def increment(n):
    return lambda x: x + n


f = increment(42)
# small handling function can be represented by lambda, by the form lambda x: f(x), with f(x) an expression of x
print(f(0), f(1), f(10), f(100))
# it's also possible to use lambda to return a function passing a small function as an argument

"""documentation string"""
# the first line of the documentation string should always be a short concise summary of the object's purpose
# the first line usually don't contain the object's name or type; it should start with capital letter and end with a .
# if there are more lines, the second line should be blank to separate the summary and the body

"""function annotation"""


# optional metadata about types; stored in __annotation__ attribute of the function as a dictionary
# have no effect on any other part of the function


def demo(ham: str, eggs: str = 'organic_eggs') -> str:  # function(parameter: type_annotation=default_value) -> type
    print('Annotation:', demo.__annotations__)
    print('Argument:', ham, eggs)
    return print(ham + ' and ' + eggs)


demo('spam')

"""coding style"""
# name classes as CamelCase and functions/methods as lower_case_with_underscore
# always use self as the name for the first method argument
