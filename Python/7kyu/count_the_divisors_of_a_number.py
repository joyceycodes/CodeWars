# Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000.

# Examples (input --> output)
# 4 --> 3 (1, 2, 4)
# 5 --> 2 (1, 5)
# 12 --> 6 (1, 2, 3, 4, 6, 12)
# 30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)
# Note you should only return a number, the count of divisors. The numbers between parentheses are shown only for you to see which numbers are counted in each case.

# using a for loop will time out for large datasets
# using list comprehension is always faster than using a for loop and appending
def divisors(n):
    return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0]);