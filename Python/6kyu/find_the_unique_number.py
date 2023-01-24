# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# my solution
def find_uniq(arr):
    hashset= list(set(arr))
    if arr[0] == arr[1] == hashset[0]:
        return hashset[1]
    else:
        slice = arr[:3]
        if slice.count(hashset[0]) > 1:
            return hashset[1]
        else: 
            return hashset[0]

# top solution
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b