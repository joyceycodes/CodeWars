# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)


# my solution
def multiply(num):
    product = 1
    for n in str(num):
        product *= int(n)
    return product

def persistence(n):
    count = 1
    product = 1
    for num in str(n):
        product *= int(num)
        
    if len(str(n)) == 1:
        return 0
    
    while len(str(product)) > 1:
        product = multiply(product)
        count += 1
        
    return count


# top solution
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count