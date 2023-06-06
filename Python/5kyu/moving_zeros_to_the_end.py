# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    #need to move all the zeros to the end
    zeros = lst.count(0)
    nums = [i for i in lst if i != 0]
    for i in range(zeros):
        nums.append(0)
    return nums

# top solution
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))