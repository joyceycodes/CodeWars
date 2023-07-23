# Find the greatest common divisor of two positive integers. The integers can be large, so you need to find a clever solution.

# The inputs x and y are always greater or equal to 1, so the greatest common divisor will always be an integer that is also greater or equal to 1.

# 7kyu
def mygcd(x,y):
    while y:
        x,y=y,x%y
    return x

def mygcd(x,y):
    if x%y ==0:
        return y
    else:
        return mygcd(y,x%y)