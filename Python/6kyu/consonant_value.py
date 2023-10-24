# Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

# For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

# -- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.
# solve("zodiacs") = 26

# For the word "strength", solve("strength") = 57
# -- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

def solve(s):
    # loop over s
    # add to value until we get to a value
    # update max_value only when it's a new high
    max_value = 0
    value = 0
    for i in s:
        if i not in 'aeiou':
            value += ord(i)-96
        else:
            max_value = max(value, max_value)
            value = 0
    return max(value, max_value)
            
# top solution using regex
import re

def solve(s):
    return max(sum(ord(c)-96 for c in subs) for subs in re.split('[aeiou]+', s))