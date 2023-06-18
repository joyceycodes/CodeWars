# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    def hexadecimal(n):
        hex = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        whole = int(n/16)
        remainder = (n % 16)
        color = ''
        if whole > 9:
            color += hex[whole]
        else:
            color += str(whole)
        if remainder > 9:
            color += hex[remainder]
        else:
            color += str(remainder)
        return color
    
    if r >= 256:
        red = "FF"
    elif r < 0:
        red = "00"
    else:    
        red = hexadecimal(r)
        
    if g >= 256:
        green = "FF"
    elif g < 0:
        green = "00"
    else:    
        green = hexadecimal(g) 
    if b >= 256:
        blue = "FF"
    elif b < 0:
        blue = "00"
    else:
        blue = hexadecimal(b)
    return red + green + blue

# top solution
# helper function to make sure the num is between 0 - 255
def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num

# the format() function :X formats the value to hex with an upper case letter
# the 02 makes sure that it returns 2 digits instead of 1, so "01" instead of "1"
def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))