# Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
# Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
# Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
# Matches should be case-insensitive, and the words in the result should be lowercased.
# Ties may be broken arbitrarily.
# If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
# Examples:
# top_3_words("In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.")
# # => ["a", "of", "on"]

# top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# # => ["e", "ddd", "aa"]

# top_3_words("  //wont won't won't")
# # => ["won't", "wont"]
# Bonus points (not really, but just for fun):
# Avoid creating an array whose memory footprint is roughly as big as the input text.
# Avoid sorting the entire array of unique words.

def top_3_words(text):
    dict = {}
    new_text=""
    for i in text:
        if i.isalpha() or i == "'":
            new_text += i
        else:
            new_text += " "
    new_text = new_text.lower().split(" ")

    for i in new_text:
        word = ""
        alpha = False
        for j in i:
            if j.isalpha():
                alpha = True
                word += j
            if j == "'":
                word += j
        if word not in dict and word != "" and alpha:
            dict[word] = 0
        try:    
            dict[word] += 1
        except:
            continue

    result = sorted(dict.items(), reverse=True, key=lambda x:x[1])
    result = [i[0] for i in result]
    return result[:3]

import re
from collections import Counter

def top_3_words(text):
    words = re.findall(r"[a-z']*[a-z]+[a-z']*", text.lower())
    top_3 = Counter(words).most_common(3)
    return [tup[0] for tup in top_3]

# [a-z']*: This part matches zero or more occurrences of lowercase letters (a-z) or apostrophes ('). This allows for words that may contain apostrophes like "don't" or "I'm". Matches words that may start with an apostrophe.

# [a-z]+: This part matches one or more occurrences of lowercase letters. It ensures that at least one lowercase letter is present in the matched word.

# [a-z']*: This part is similar to the first part and matches zero or more occurrences of lowercase letters or apostrophes. It allows for words that end with an apostrophe, such as "didn't".