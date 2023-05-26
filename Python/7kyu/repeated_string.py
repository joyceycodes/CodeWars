# HACKER RANK
# There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.

# Example
# The substring we consider is , the first  characters of the infinite string. There are  occurrences of a in the substring.

# Function Description
# Complete the repeatedString function in the editor below.
# repeatedString has the following parameter(s):
# s: a string to repeat
# n: the number of characters to consider

# Returns
# int: the frequency of a in the substring
# Input Format
# The first line contains a single string, .
# The second line contains an integer, .

# Constraints
# For  of the test cases, .
# Sample Input

# Sample Input 0
# aba
# 10
# Sample Output 0
# 7
# Explanation 0
# The first  letters of the infinite string are abaabaabaa. Because there are  a's, we return .

# Sample Input 1
# a
# 1000000000000

# Sample Output 1
# 1000000000000
# Explanation 1
# Because all of the first  letters of the infinite string are a, we return .

def repeatedString(s, n):
    # find how many 'a's are in s
    counter = s.count('a')
    
    # find how many repititions of s we'll need
    length = int(n//len(s))
    
    # find how many remainder chars and how many 'a's in that
    remaining = int(n % len(s))
    remaining_count = s[:remaining].count('a')
    
    return counter*length + remaining_count