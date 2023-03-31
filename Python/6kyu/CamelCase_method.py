# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

# For instance:

# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord

def camel_case(s):
    words = s.split()
    result = ''
    for word in words:
        for i in range(len(word)):
            if i == 0:
                print(word[i])
                result += word[i].upper()
            else:
                result += word[i]
    return result

# top solution
def camel_case(string):
    return string.title().replace(" ", "")
    # title() method capitalizes every first letter of each word in a string