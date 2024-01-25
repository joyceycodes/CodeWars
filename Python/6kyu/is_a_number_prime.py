# Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
# NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.

# correct solution
from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):    
        if num%i == 0:
            return False
        i += 1
    return True 

# def is_prime(num):
#     if num <= 1:
#         return False
    
#     if num % 2 == 0 and num > 2:
#         return False
#     elif num % 3 == 0 and num > 3:
#         return False
#     elif num % 5 == 0 and num > 5:
#         return False
#     elif num % 7 == 0 and num > 7:
#         return False
#     else: 
#         return True
  

print(is_prime(747760303)) #false

print(is_prime(1759185811)) #false

# reviewed 1/24/24