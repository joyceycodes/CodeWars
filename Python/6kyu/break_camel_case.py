# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# my solution
def solution(s):
    result = ''
    for letter in s:
        if letter.isupper():
            result += ' ' + letter
        else:
            result += letter
    return result

# top solution
def solution(s):
    return ' '.join(' ' + c if c.isupper() else c for c in s)