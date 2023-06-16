# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string

def is_valid_IP(strng):

    strng = strng.split(".")
    if len(strng) != 4:
        return False

    for i in strng:
        try:
            if not i.isalnum():
                return False
            if len(i) > 1 and i[0] == "0":
                return False
            if int(i) not in range(0,256):
                return False
        except ValueError:
            return False
    return True

# top solution
def is_valid_IP(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))