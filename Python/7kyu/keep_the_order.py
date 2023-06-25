# Your job here is to write a function (keepOrder in JS/CoffeeScript, keep_order in Ruby/Crystal/Python, keeporder in Julia), which takes a sorted array ary and a value val, and returns the lowest index where you could insert val to maintain the sorted-ness of the array. The input array will always be sorted in ascending order. It may contain duplicates.

# Do not modify the input.

# Some examples:
# keep_order([1, 2, 3, 4, 7], 5) #=> 4
#                       ^(index 4)
# keep_order([1, 2, 3, 4, 7], 0) #=> 0
#           ^(index 0)
# keep_order([1, 1, 2, 2, 2], 2) #=> 2
#                 ^(index 2)

def keep_order(ary, val):
    if not ary:
        return 0

    pointer = 0
    while pointer <= len(ary):
        if ary[pointer] > val or ary[pointer] == val:
            return pointer
        if pointer == len(ary)-1 and ary[pointer] < val:
            return pointer+1
        if ary[pointer] < val and val < ary[pointer+1]:
            return pointer+1
        pointer += 1

# top solution
def keep_order(ary, val):
    for i, x in enumerate(ary):
        if x >= val:
            return i
    return len(ary)