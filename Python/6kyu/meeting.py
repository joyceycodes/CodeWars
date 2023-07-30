# John has invited some friends. His list is:

# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
# Could you make a program that

# makes this string uppercase
# gives it sorted in alphabetical order by last name.
# When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

# So the result of function meeting(s) will be:

# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
# It can happen that in two distinct families with the same family name two people have the same first name too.

# Notes
# You can see another examples in the "Sample tests".

def meeting(s):
    full_names = s.split(';')
    
    names = []
    for name in full_names:
        split_name = name.upper().split(":")
        split_name[1], split_name[0] = split_name[0], split_name[1]
        names.append(split_name)

    sorted_by_first_name = sorted(names, key = lambda x: x[1] )
    sorted_by_last_name = sorted(sorted_by_first_name, key = lambda x: x[0])

    return "".join(["({last_name}, {first_name})".format(first_name=name[1], last_name = name[0]) for name in sorted_by_last_name])
        
# top solution
def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))