# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

def number(lines):
    result = []
    for i in range(1,len(lines)+1):
        entry = str(i)
        entry += ': '
        entry += lines[i-1]
        result.append(entry)
    return result

# top solution
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]