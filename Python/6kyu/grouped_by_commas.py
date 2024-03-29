# Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

# Assume: 0 <= n < 2147483647

# Examples
#        1  ->           "1"
#       10  ->          "10"
#      100  ->         "100"
#     1000  ->       "1,000"
#    10000  ->      "10,000"
#   100000  ->     "100,000"
#  1000000  ->   "1,000,000"
# 35235235  ->  "35,235,235"

def group_by_commas(n):
    result = ""
    for i,e in enumerate(str(n)[::-1]):
        if i%3==0 and i != 0:
            result += ","
            result += e
        else:
            result += e
    return result[::-1]
            
def group_by_commas(n):
    return '{:,}'.format(n)