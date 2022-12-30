# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

# my solution
def is_isogram(string):
    chars = {}
    
    for e in string.lower():
        if e not in chars:
            chars[e] = 0
        chars[e] += 1
    

    for i in chars.values():
        if i > 1:
            return False
    return True

# top solution: using sets. A set is a data type that stores a collection of data. Sets can not have duplicates values.
def is_isogram(string):
    return len(string) == len(set(string.lower()))
