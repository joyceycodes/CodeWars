# Given a Divisor and a Bound , Find the largest integer N , Such That ,

# Conditions :
# N is divisible by divisor

# N is less than or equal to bound

# N is greater than 0.

# Notes
# The parameters (divisor, bound) passed to the function are only positive values .


def max_multiple(divisor, bound):
    while bound % divisor != 0:
        bound -= 1
    return bound

# top solution
def max_multiple(divisor, bound):
    return bound - (bound % divisor)