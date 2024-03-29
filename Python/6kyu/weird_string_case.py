# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

# The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

# Examples:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

def to_weird_case(words):
    result = []
    words = words.split(' ')
    for i in words:
        word = ""
        for j in range(len(i)):
            if j%2 == 0:
                word += i[j].upper()
            else:
                word += i[j].lower()
        result.append(word)
    return ' '.join(result)

def to_weird_case(words):
    res = ""
    i = 0
    for letter in words:
        if i % 2 == 0:
            res += letter.upper()
        else: 
            res += letter.lower()
        if letter == " ":
            i = 0
        else:
            i += 1
    return res