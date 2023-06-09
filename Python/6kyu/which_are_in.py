# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

def in_array(array1, array2):
    print(array1)
    print(array2)
    r = set()
    for i in array1:
        for j in array2:
            if i in j:
                r.add(i)
    r = list(r)
    r.sort()
    return r