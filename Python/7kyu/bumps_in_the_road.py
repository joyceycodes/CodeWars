# Your car is old, it breaks easily. The shock absorbers are gone and you think it can handle about 15 more bumps before it dies totally.

# Unfortunately for you, your drive is very bumpy! Given a string showing either flat road (_) or bumps (n). If you are able to reach home safely by encountering 15 bumps or less, return Woohoo!, otherwise return Car Dead

def bumps(road):
    bumps = 0
    for i in road:
        if i == 'n':
            bumps += 1
    return "Car Dead" if bumps > 15 else "Woohoo!"

# top solution
def bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"