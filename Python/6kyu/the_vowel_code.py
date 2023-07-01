# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

# For example, decode("h3 th2r2") would return "hi there".

# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

def encode(st):
    dict = {"a": "1", "e":"2", "i":"3", "o":"4", "u":"5"}
    result = ""
    for i in st:
        if i in dict:
            result += dict[i]
        else:
            result += i
    return result
    
def decode(st):
    dict = {"1": "a", "2":"e", "3":"i", "4":"o", "5":"u"}
    result = ""
    for i in st:
        if i in dict:
            result += dict[i]
        else:
            result += i
    return result

# top solution
def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)

# using enumerate
def encode(st):
    for i, v in enumerate("aeiou", start=1):
        st = st.replace(v,str(i))
    return st
    
def decode(st):
    for i, v in enumerate("aeiou", start=1):
        st = st.replace(str(i),v)
    return st
