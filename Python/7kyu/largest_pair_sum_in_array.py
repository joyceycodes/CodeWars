# Given a sequence of numbers, find the largest pair sum in the sequence.

# For example

# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.

def largest_pair_sum(numbers): 
    sorted_nums = sorted(numbers)
    return sorted_nums[-1] + sorted_nums[-2]

# top solution
def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])