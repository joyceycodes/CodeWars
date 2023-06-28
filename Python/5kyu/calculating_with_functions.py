# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def zero(func=None): return func(0) if func else 0
def one(func=None): return func(1) if func else 1
def two(func=None): return func(2) if func else 2
def three(func=None): return func(3) if func else 3
def four(func=None): return func(4) if func else 4
def five(func=None): return func(5) if func else 5
def six(func=None): return func(6) if func else 6
def seven(func=None): return func(7) if func else 7
def eight(func=None): return func(8) if func else 8
def nine(func=None): return func(9) if func else 9

def plus(digit): return lambda x: x + digit
def minus(digit): return lambda x: x - digit
def times(digit): return lambda x: x * digit
def divided_by(digit): return lambda x: x // digit