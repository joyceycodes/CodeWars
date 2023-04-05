# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

# For example: (Input --> Output)

# 10 --> 1
# 99 --> 18
# -32 --> 5
# Let's assume that all numbers in the input will be integer values.

def sum_digits(number):
    sum = 0
    for num in str(number):
        if num.isalnum():
            sum += int(num)
    return sum

def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))