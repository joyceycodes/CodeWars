# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    return [my_list[i] for i in range(len(my_list)) if i % 2 ==0]

# top solution
def remove_every_other(my_list):
    return my_list[::2]