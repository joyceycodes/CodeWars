# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    hash = {}
    for e in string:
        if e not in hash:
            hash[e] = 0
        hash[e]+=1
    return hash

# top solution
from collections import Counter

def count(string):
    return Counter(string)

def count(string):
    return {i: string.count(i) for i in string}