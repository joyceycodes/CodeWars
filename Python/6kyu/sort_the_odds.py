# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

# top solution
def sort_array(arr):
    # getting all the odd numbers out of the list in reverse sort order
    odds = sorted((x for x in arr if x%2 != 0), reverse=True)

    # if the item in arr is odd, we'll add the last item from the odds list (smallest), else we'll add the even number
    return [x if x%2==0 else odds.pop() for x in arr]