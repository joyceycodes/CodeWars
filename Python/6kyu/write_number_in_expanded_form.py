# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    result = []
    length = len(str(num))-1
    for i,e in enumerate(str(num)):
        if e != '0':
            num = e+ (length) * '0'
            result.append(num)
        length -= 1
    return ' + '.join(result)

# top solution
def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')
