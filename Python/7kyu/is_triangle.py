# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

# my solution
def is_triangle(a, b, c):
    sides = [a,b,c]
    sides.sort()
    if a > 0 and b > 0 and c > 0:
        if sides[0] + sides[1] > sides[2]:
            return True
        else:
            return False
    else:
        return False


# top solution
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

