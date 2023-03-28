# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

# For example:

# 1.08 --> 30
# Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

import math
def cockroach_speed(s):
    return math.floor(s * 27.778)

# top solution
def cockroach_speed(s):
    cm_per_km = 100000
    sec_per_hour = 3600
    return int(s * cm_per_km / sec_per_hour)