# Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.

def reverse_alternate(s):
    words = s.split()
    result = [words[i] if i%2==0 else words[i][::-1] for i in range(len(words))]
    return " ".join(result)