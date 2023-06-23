# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas
# The code would be called like so:

# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"

def strip_comments(strng, markers):
    strng = strng.split('\n')

    result = []
    for i in strng:
        comment = 0
        line = i
        for j in range(len(i)):
            if i[j] in markers:
                comment = j
                line = i[:comment]
                break
        result.append(line.rstrip())

    return ("\n".join(result))

def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)