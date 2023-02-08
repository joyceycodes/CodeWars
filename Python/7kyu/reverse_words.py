# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# top solution
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

def reverse_words(str):
  newStr = []
  for i in str.split(' '):
      newStr.append(i[::-1])
  return ' '.join(newStr)