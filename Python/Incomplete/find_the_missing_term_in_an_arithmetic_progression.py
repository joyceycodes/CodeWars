# https://www.codewars.com/kata/52de553ebb55d1fca3000371/

def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)