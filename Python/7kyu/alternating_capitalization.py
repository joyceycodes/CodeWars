# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

# The input will be a lowercase string with no spaces.

def capitalize(s):
    upper_even = ''.join([s[i].upper() if i % 2 == 0 else s[i] for i in range(len(s))])
    upper_odd = ''.join([s[i].upper() if i % 2 == 1 else s[i] for i in range(len(s))])
    
    return [upper_even, upper_odd]

# top solutions
def capitalize(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]

def capitalize(s):
    result = ['','']
    for i,c in enumerate(s):
        result[0] += c.lower() if i % 2 else c.upper()
        result[1] += c.upper() if i % 2 else c.lower()
    return result