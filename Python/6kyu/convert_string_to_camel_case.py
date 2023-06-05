# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    # input = string that is separated by dashes or underscores
    # return = string with the text joined together and all words after the first on capitalized
    
    if not text:
        return ""
    
    result = text[0]

    for i in range(1,len(text)):
        if text[i] == "-" or text[i] == "_":
            continue
        elif text[i-1] == "-" or text[i-1] == "_":
            result += (text[i].upper())
        else:
            result += (text[i])
            
    return result

# top solution
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])