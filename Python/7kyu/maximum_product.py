# Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.

# Notes
# Array/list size is at least 2.

# Array/list numbers could be a mixture of positives, negatives also zeroes .

# Input >> Output Examples
# adjacentElementsProduct([1, 2, 3]); ==> return 6
# Explanation:
# The maximum product obtained from multiplying 2 * 3 = 6, and they're adjacent numbers in the array.

def adjacent_element_product(array):
    max_num = float('-inf')
    for i in range(0,len(array)-1,1):
        max_num = max(max_num, array[i]*array[i+1])
    return max_num

# top solution
def adjacent_element_product(array):
    return max( a*b for a, b in zip(array, array[1:]) )
