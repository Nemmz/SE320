"""
Author: Isaac Jarrells
Filename: infinitegenerator.py
Date: January 21, 2025
Purpose: To use generators to produce number sequences.
Sources:
https://www.learnpython.org/en/Generators
"""


from typing import Generator

"""
# Generates an indefinite or definte sequence of the Fibonacci Sequence Numbers
# depending on user input.
"""
def gen_fibonacci(limit: int = None) -> Generator[int, None, None]:

    int_1, int_2 = 0, 1 # starting values of fibonacci
    if limit is None:
        while True:     # indefinite condition
            yield int_1 # return first value before adjusting value
            int_1, int_2 = int_2, int_1 + int_2  # fibonacci formula
    else:
        for n in range(limit): #definte condition
            yield int_1
            int_1, int_2 = int_2, int_1 + int_2
"""
# Generates an indefinite or definte sequence of the Binary Bit Values
# depending on user input.
"""
def gen_binary(limit: int = None) -> Generator[int, None, None]:
    if limit is None:
        count = 0 # n variable
        while True: # indefinite condition
            int_binary = 2 ** count  # exponent of 2^n
            yield int_binary  # return the value
            count += 1  # increment the n variable
    else: # definite condition
        for n in range(limit):
            int_binary = 2 ** n
            yield int_binary


# Fibonacci Sequence
assert list(gen_fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert list(gen_fibonacci(-1)) == []
assert list(gen_fibonacci(0)) == []
assert list(gen_fibonacci(1)) == [0]
assert list(gen_fibonacci(2)) == [0, 1]

# Binary Bit Values Sequence
assert list(gen_binary(10)) == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
assert list(gen_binary(-1)) == []
assert list(gen_binary(0)) == []
assert list(gen_binary(1)) == [1]
assert list(gen_binary(2)) == [1, 2]
