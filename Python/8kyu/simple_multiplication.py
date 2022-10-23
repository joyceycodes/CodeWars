# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# my solution
def simple_multiplication(number):
    if number % 2 == 0:
        return number*8
    else: 
        return number*9

# top solution
def simple_multiplication(number):
    return number * 9 if number % 2 else number * 8