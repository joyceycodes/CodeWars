# Rules:
# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return 0.00

# You will only be given Natural Numbers as arguments.

# Examples:(Input --> Output)
# 1 --> 1 --> "1.00"
# 2 --> 1 + 1/4 --> "1.25"
# 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"

def series_sum(n):
    if n == 0:
        return "0.00"

    sum = 1
    den = 4
    
    for i in range(2,n+1):
        if i == 2:
            sum += 1/den
        else:
            den += 3
            sum += 1/den

    return "{:0.2f}".format(sum)

# top solution
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))