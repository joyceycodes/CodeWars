# You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

# Find max(abs(length(x) − length(y)))

# If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

# Example:
# a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# mxdiflg(a1, a2) --> 13
# Bash note:
# input : 2 strings with substrings separated by ,
# output: number as a string

def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    
    max1 = len(a1[0])
    min1 = len(a1[0])
    for i in a1:
        if len(i) > max1:
            max1 = len(i)
        if len(i) < min1:
            min1 = len(i)   
            
    max2 = len(a2[0])
    min2 = len(a2[0])
    for i in a2:
        if len(i) > max2:
            max2 = len(i)
        if len(i) < min2:
            min2 = len(i)   
    
    return max(abs(max1 - min2), abs(max2 - min1))

# top solution
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1