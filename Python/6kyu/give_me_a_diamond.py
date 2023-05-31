# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

# Task
# You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

# Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

# Examples
# A size 3 diamond:

#  *
# ***
#  *
# ...which would appear as a string of " *\n***\n *\n"

# A size 5 diamond:

#   *
#  ***
# *****
#  ***
#   *
# ...that is:

# "  *\n ***\n*****\n ***\n  *\n"

def diamond(n):
    # Make some diamonds!
    result = ""
    
    if n < 0 or n % 2 == 0:
        return None
    
    # there will be n lines for a n sized diamond (we'll need to loop n times)
    # we need to add spaces, *, and \n for every line
    # i* 2 - 1 to get the odd amount of stars
    for i in range(1,(n//2)+2):
        row =''
        row += ' ' * (((n+1)//2)-i)
        row += '*' * abs((i*2) -1)
        row += '\n'
        print(int(n/2), row)
        result += row
        
    for i in range(n//2,0,-1):
        row =''
        row += ' ' * (((n+1)//2)-i)
        row += '*' * ((i*2) -1)
        row += '\n'
        print(i,row)
        result += row

    return result

# top solution
def diamond(n):

    if n < 0 or n % 2 == 0:
        return None
    
    result = "*" * n + "\n"
    spaces = 1
    n = n - 2
    while n > 0:
        current = " " * spaces + "*" * n + "\n"
        spaces = spaces + 1
        n = n - 2
        result = current + result + current
    
    return result