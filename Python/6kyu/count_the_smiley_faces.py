# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

# Example
# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

def count_smileys(arr):
    hash = {":" :  [")", "D", "-","~"], 
            ";" : [")", "D", "-","~"]
           }
    count = 0
    for face in arr:
        if face[0] in hash:
            if face[1] in hash[face[0]] and face[len(face)-1] in hash[face[0]]:
                count += 1
    return count

# top solution
from re import findall
def count_smileys(arr):
    # First, " ".join(arr) concatenates all the strings in the arr list into a single string with spaces between each element.
    # The concatenated string is then passed as the second argument to the findall function, which searches for all occurrences of the regular expression pattern r"[:;][-~]?[)D]".
    # The regular expression pattern r"[:;][-~]?[)D]" matches any string that begins with either a : or ;, followed by an optional nose represented by a - or ~, and ending with either ) or D.
    # findall returns a list of all matches found, and list() converts it into a list.
    # Finally, len() is used to count the number of elements in the list of matches found, and this value is returned as the output of the function.
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))