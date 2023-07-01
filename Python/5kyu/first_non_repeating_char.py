# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(s):
    # find the count of each letter
    # loop over the values and have a list of all the letters with a value of 1, if list if empty, return None
    # return index of list[0]

    count = {} # dict that holds onto the element and index if it's unique
    for i,e in enumerate(s.lower()):
        if e not in count:
            count[e] = i
        else:
            count[e] = ""
    
    unique = []
    for k,v in count.items():
        if v != "":
            unique.append(v)

    if len(unique) == 0:
        return ""
    else:
        return s[unique[0]]

# top solution
def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""