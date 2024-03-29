# An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

# You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.

# Example
# find_missing([1, 3, 5, 9, 11]) == 7
# PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on paper using math, derive the algo that way. Have fun!

def find_missing(list):
    first = list[1]-list[0]
    second = list[2]-list[1]
    last = list[len(list)-1] - list[len(list)-2]
    if first == last:
        for i in range(0, len(list)-1):
            if list[i] + first != list[i+1]:
                return list[i] + first
    elif first == second:
        for i in range(0, len(list)-1):
            if list[i] + first != list[i+1]:
                return list[i] + first
    else:
        for i in range(0, len(list)-1):
            if list[i] + last != list[i+1]:
                return list[i] + last

def find_missing(sequence):
  interval = (sequence[-1] - sequence[0])/len(sequence)
  for previous, item in enumerate(sequence[1:]):
      if item - sequence[previous] != interval:
          return item - interval
