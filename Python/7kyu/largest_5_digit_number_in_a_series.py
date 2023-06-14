# In the following 6 digit number:

# 283910
# 91 is the greatest sequence of 2 consecutive digits.

# In the following 10 digit number:

# 1234567890
# 67890 is the greatest sequence of 5 consecutive digits.

# Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number given. The number will be passed in as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.

def solution(digits):
    # find the greatest sequence of 5 digits
    # find the max num in digits and see if there's enough for a sequence
    max_seq = int(str(digits[:5]))
    current = max_seq
    str_digits = str(digits)
    for i in range(1,len(digits)-4):
        current = str_digits[i:i+5]
        if int(current) > max_seq:
            max_seq = int(current)
    return max_seq

# top solution
def solution(digits):
    numlist = [int(digits[i:i+5]) for i in range(0,len(digits)-4)]
    return max(numlist)