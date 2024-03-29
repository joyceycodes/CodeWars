# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    # input: a string with of only letters and spaces, at least one word
    # output: a string 
    # if len(word)>=5, reverse the word, else keep the same
    # split sentence into individual elements in an array, loop over the array and reverse selected words
    # join the elements in the array with a space
    
    sentence = sentence.split(' ')
    result = [word[::-1] if len(word) >= 5 else word for word in sentence]

    return " ".join(result)

# top solution
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])