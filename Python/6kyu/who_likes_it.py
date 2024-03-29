# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

# my solution
def likes(names):
    length = len(names)
    
    if length == 0:
        return "no one likes this"
    
    elif length == 3:
        return names[0] + ", " + names[1] + " and " + names[2]+ " like this"
    
    elif length == 2:
        return names[0] + " and " + names[1]+ " like this"
    
    elif length == 1:
        return names[0] + " likes this"

    else:
        length = length - 2
        return names[0] + ", " + names[1] + " and " + str(length) + " others like this"


# top solution
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
    # uses min() function to select which string in the dictionary to format
    # uses format() method to input the names or others into the string's placeholder {}