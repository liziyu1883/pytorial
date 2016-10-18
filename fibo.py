"""Fibonacci numbers module"""


def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


"""to run fibo.py as an independent script in console"""
if __name__ == "__main__":  # only executes when the name is __main__, won't run if imported as a module
    import sys

    fib(int(sys.argv[1]))
