# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def make_readable(seconds):
    hours =( seconds // 60 ) // 60
    minutes = (seconds - ( hours*60*60 )) // 60
    seconds = seconds - ( hours*60*60 ) - (minutes*60)
    return ('{:02d}:{:02d}:{:02d}'.format(hours,minutes,seconds))

# top solution
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)