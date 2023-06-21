# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:


# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python

def snail(snail_map):
    # input - an array of arrays
    # return - a singular array of all the digits from the matrix in clockwise fashion
    next_dir = {"right":"down", "down":"left", "left":"up", "up":"right"}
    dir = "right"
    result = []
    while snail_map:
        if dir == "right":
            result += snail_map.pop(0)
        if dir == "down":
            for i in snail_map:
                result.append(i.pop())
        if dir == "left":
            result.extend(snail_map.pop(-1)[::-1])
        if dir == "up":
            for i in snail_map[::-1]:
                result.append(i.pop(0))
        dir = next_dir[dir]
    return result

# top solutions
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out

def snail(array):
    next_dir = {"right": "down", "down":"left", "left":"up", "up":"right"}
    dir = "right"
    snail = []
    while array:
        if dir == "right":
            snail.extend(array.pop(0))
        elif dir == "down":
            snail.extend([x.pop(-1) for x in array])
        elif dir == "left":
            snail.extend(list(reversed(array.pop(-1))))
        elif dir == "up":
            snail.extend([x.pop(0) for x in reversed(array)])    
        dir = next_dir[dir]
    return snail     