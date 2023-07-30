def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)

print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))