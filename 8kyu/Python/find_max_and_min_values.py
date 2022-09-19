# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.

# my solution
def minimum(arr):
    #your code here...
    min = arr[0]
    for num in arr:
        if num < min:
            min = num
    return min

def maximum(arr):
    #...and here
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max


# top solution
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)