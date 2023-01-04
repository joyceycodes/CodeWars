# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# Notes
# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

# my solution
def duplicate_encode(word):
    hashmap = {}
    result = ''
    word = word.lower()
    for c in word:
        if c not in hashmap:
            hashmap[c] = 0
        hashmap[c] += 1
    for c in word:
        if hashmap[c] > 1:
            result += ')'
        else:
            result += '('
    return result

# top solution
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])