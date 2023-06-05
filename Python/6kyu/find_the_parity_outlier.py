# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(integers):
    # input = a list of ints that contain an outlier that is even or odd
    # return the outlier
    
    # get a list of 0s and 1s for even and odds
    even_odd = [0 if i%2==0 else 1 for i in integers ]
    
    if even_odd.count(1) == 1:
        return integers[even_odd.index(1)]
    else:
        return integers[even_odd.index(0)]

# top solution
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]