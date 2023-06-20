# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def scramble(s1, s2):
    # input - 2 strings, all the letters from s2 must be in s1
    # return - boolean 
    hash1 = {}
    for i in s1:
        if i not in hash1:
            hash1[i] = 0
        hash1[i] +=1
    
    hash2 = {}
    for i in s2:
        if i not in hash2:
            hash2[i] = 0
        hash2[i] +=1
    
    for k,v in hash2.items():
        if k in hash1.keys():
            if v > hash1[k]:
                return False
        else:
            return False
    return True

def scramble(s1, s2):
    # input - 2 strings, all the letters from s2 must be in s1
    # return - boolean 
    hash1 = {}
    for i in s1:
        if i not in hash1:
            hash1[i] = 0
        hash1[i] +=1
    

    for i in s2:
        if i in hash1.keys():
            if hash1[i] == 0:
                return False
            hash1[i] -= 1
        else:
            return False
    return True

from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    # set subtraction removes all the elements in both operands from the first set that is being subtracted from
    return len(Counter(s2)- Counter(s1)) == 0