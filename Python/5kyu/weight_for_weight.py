# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.

# Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 

# "100 180 90 56 65 74 68 86 99"
# When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:

# 180 is before 90 since, having the same "weight" (9), it comes before as a string.

# All numbers in the list are positive numbers and the list can be empty.

# Notes
# it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
# For C: The result is freed.

def order_weight(strng):
    strng = strng.split(" ")

    # a list of lists, [[weight (str), new_weight (int)]]
    weighted = []
    for i in strng:
        if i:
            weight = [i]
            new_weight = list(map(lambda x: int(x), [*i]))
            weight.append((sum(new_weight)))
            weighted.append(weight)

    # sorting the list by the weight (i[0]) which is a str
    weighted.sort(key=lambda x:x[0])

    # sorting the list again by the new_weight
    weighted.sort(key=lambda x:x[1])

    return " ".join([i[0] for i in weighted])

# top solution
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))

# another solution
def sum_string(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum

def order_weight(strng):
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))
    
    return result
