import random
random.seed(1)  # Setting random number generator seed for repeatability

# REMINDER TO SELF, CHANGING NUM_DRONES FROM 10000 TO 10 FOR NOW
NUM_DRONES = 10
AIRSPACE_SIZE = 100  # Meters. # changed from 128000
CONFLICT_RADIUS = 20  # Meters. #changed from 500


def count_conflicts(drones, conflict_radius):
    # INPUT - drones = a list containing the [x,y] corrdinates of each drone
    # INPUT - conflict_radius = int, representing the distance in meters each drone must be from one another
    # RETURN - int, total number of drones that are in conflict (within the conflict radius of another drone)

    # distance between 2 drones = d = sqrt(x^2 + y^2)

    # if drone is in conflict, we don't need to revisit it
    conflicted_drones = set()

    j = len(drones) - 1
    i = j - 1

    while j > 0 and len(drones) >= 2:
        x = abs(drones[j][0] - drones[i][0])
        y = abs(drones[j][1] - drones[i][1])
        distance = ((x**2 ) + (y**2)) 

        if distance < (conflict_radius ** 2):
            # adding to our list of conflicted_drones
            conflicted_drones.add(tuple(drones[j]))
            conflicted_drones.add(tuple(drones[i]))

            # swapping the elements so that drones[i] can be the second last item in the list
            drones[i],drones[j-1] = drones[j-1],drones[i]

            # popping the last two items (conflicting drones) off the list
            drones.pop()
            drones.pop()

            j = len(drones) - 1
            i = j - 1

        # popping off the last drone if it had no conflicts
        elif i == 0:
            drones.pop()
            j = len(drones) - 1
            i = j - 1

        else:
            i -= 1

    return len(conflicted_drones)  

    # for i in range(len(drones)):
    #     for j in range(i+1,len(drones)):
    #         x = abs(drones[i][0] - drones[j][0])
    #         y = abs(drones[i][1] - drones[j][1])
    #         d = ((x**2 ) + (y**2)) ** (1/2)
    #         print(drones[i] ,drones[j], d)
    #         count += 1
    #         if d < conflict_radius:
    #             conflicts.add(tuple(drones[i]))
    #             conflicts.add(tuple(drones[j]))
def gen_coord():
    # all drones will in the drones list will be within the airspace
    return int(random.random() * AIRSPACE_SIZE)

positions = [[gen_coord(), gen_coord()] for i in range(NUM_DRONES)]
conflicts = count_conflicts(positions, CONFLICT_RADIUS)
print("Drones in conflict: {}".format(conflicts))

# trying merge sort
# def partition(drones, conflict_radius, left=None, right=None):
#     pivot = drones[right]
#     star = left - 1

#     for i in range(left,right):
#         x = abs(drones[i][0] - drones[j][0])
#         y = abs(drones[i][1] - drones[j][1])
#         d = ((x**2 ) + (y**2)) ** (1/2)
#         print(d)
        


# def count_conflicts(drones, conflict_radius, left=None, right=None):
#     if left == None and right == None:
#         left = 0
#         right = len(drones) -1
    
#     if left >= right or left < 0:
#         return

#     p = partition(drones, conflict_radius, left, right)
#     count_conflicts(drones, left, p-1)
#     count_conflicts(drones, p+1, right)

    