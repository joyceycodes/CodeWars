# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

# my solution. I was under the assumption that the lower() would not work on a string with numbers, but it does! It just wouldn't work on ints
def duplicate_count(text):
    hashmap = {}
    count = 0
    lowered = ''
    
    for char in text:
        if isinstance(char, str):
            lowered += char.lower()
        else:
            lowered += char

    for char in lowered:
        if char not in hashmap:
            hashmap[char]=0
        hashmap[char]+=1
        
    for num in hashmap.values():
        if num > 1:
            count += 1

    return count


# top solution
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])