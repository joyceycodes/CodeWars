# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(strng):
    if not strng:
        return "1"

    if strng[-1].isdigit() == False:
        return strng + '1'
    
    digit = ""
    for i in strng[::-1]:
        if i.isdigit():
            digit += i
        if i.isdigit() == False:
            break

    digit_length = len(digit[::-1])
    new_num = str(int((digit[::-1]))+1)

    diff = digit_length - len(new_num)
    return (strng[:len(strng)-digit_length] + diff*"0" +  new_num)

# top solution
def increment_string(strng):
    
    # strip the numbers from the right
    stripped = strng.rstrip('1234567890')
    
    # get the part of strng that was stripped
    ints = strng[len(stripped):]
    
    if len(ints) == 0:
        return strng + '1'
    else:
        # find the length of ints
        length = len(ints)
    
        # add 1 to ints
        new_ints = 1 + int(ints)
    
        # pad new_ints with zeroes on the left
        new_ints = str(new_ints).zfill(length)
    
        return stripped + new_ints