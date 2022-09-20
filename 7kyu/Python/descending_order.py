# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321


# my solution
def descending_order(num):
    # Bust a move right here
    list = []
    for item in str(num):
        list.append(item)
    
    descending = sorted(list, reverse=True)
    result = "".join(descending)
    return int(result)

# top solution
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))