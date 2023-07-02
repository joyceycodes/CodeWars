import random
random.seed(1)  # Setting random number generator seed for repeatability

# REMINDER TO SELF, CHANGING NUM_DRONES FROM 10000 TO 10 FOR NOW
NUM_DRONES = 10
AIRSPACE_SIZE = 100  # Meters. # changed from 128000
CONFLICT_RADIUS = 30  # Meters. #changed from 500


def count_conflicts(drones, conflict_radius):
    # INPUT - drones = a list containing the [x,y] corrdinates of each drone
    # INPUT - conflict_radius = int, representing the distance in meters each drone must be from one another
    # RETURN - int, total number of drones that are in conflict (within the conflict radius of another drone)

    # distance between 2 drones = d = sqrt(x^2 + y^2)

    # if drone is in conflict, we don't need to revisit it

    conflicts = set()
    print(drones)
    for i in range(len(drones)):
        for j in range(i+1,len(drones)):
            x = abs(drones[i][0] - drones[j][0])
            y = abs(drones[i][1] - drones[j][1])
            d = ((x**2 ) + (y**2)) ** (1/2)
            print(drones[i] ,drones[j], d)
            if d < conflict_radius:
                conflicts.add(tuple(drones[i]))
                conflicts.add(tuple(drones[j]))


    return len(conflicts)
    

def gen_coord():
    # all drones will in the drones list will be within the airspace
    return int(random.random() * AIRSPACE_SIZE)

positions = [[gen_coord(), gen_coord()] for i in range(NUM_DRONES)]
conflicts = count_conflicts(positions, CONFLICT_RADIUS)
print("Drones in conflict: {}/{}".format(conflicts, len(positions)))