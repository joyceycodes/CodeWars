# If　a = 1, b = 2, c = 3 ... z = 26

# Then l + o + v + e = 54

# and f + r + i + e + n + d + s + h + i + p = 108

# So friendship is twice as strong as love :-)

# Your task is to write a function which calculates the value of a word based off the sum of the alphabet positions of its characters.

# The input will always be made of only lowercase letters and will never be empty.

def words_to_marks(s):
    letters = [0,"a","b","c","d","e","f","g","h","i",'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    sum = 0
    for i in s.lower():
        sum += letters.index(i)
    return sum

# top solutions
def words_to_marks(s):
  return sum(ord(c)-96 for c in s)

def words_to_marks(s):
    return sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s)