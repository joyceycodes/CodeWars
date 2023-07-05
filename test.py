import random
import pprint
import collections

random.seed(1)  # Setting random number generator seed for repeatability

# REMINDER TO SELF, CHANGING NUM_DRONES FROM 10000 TO 10 FOR NOW
NUM_DRONES = 10
AIRSPACE_SIZE = 100  # Meters. # changed from 128000
CONFLICT_RADIUS = 20  # Meters. #changed from 500

pp = pprint.PrettyPrinter(indent=4)


def squared_distance(point1, point2):
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    return (dx**2 ) + (dy**2)

BT = collections.namedtuple("BT", ["value", "left", "right"])
"""
A Binary Tree (BT) with a node value, and left- and
right-subtrees.
"""

def build_kdtree(points, depth = 0):
    n = len(points)
    if n <= 0:
        return None
    
    axis = depth % 2 # there's only two axis, x and y
    sorted_points = sorted(points, key=lambda point:point[axis])

    return BT (
        value = sorted_points[n//2], # root of the tree/subtree
        left = build_kdtree(sorted_points[:n//2], depth + 1),
        right = build_kdtree(sorted_points[n//2 + 1:], depth + 1)
    )

NNRecord = collections.namedtuple("NNRecord", ["point", "distance"])
"""
Used to keep track of the current best guess during a nearest
neighbor search.
"""

def find_nearest_neighbor(*, tree, point):
    """Find the nearest neighbor in a k-d tree for a given
    point.
    """
    k = len(point)

    best = None

    def search(*, tree, depth):
        """Recursively search through the k-d tree to find the
        nearest neighbor.
        """
        nonlocal best

        if tree is None:
            return
        
        distance = squared_distance(tree.value, point)
        if best is None or distance < best.distance:
            best = NNRecord(point=tree.value, distance=distance)
        
        axis = depth % k
        diff = point[axis] - tree.value[axis]
        if diff <= 0:
            close, away = tree.left, tree.right
        else:
            close, away = tree.right, tree.left
        
        search(tree=close, depth=depth+1)
        if diff**2 < best.distance:
            search(tree=away, depth=depth+1)
    
    search(tree=tree, depth=0)
    print(best.point)
    return best.point
    
# def count_conflicts(drones, conflict_radius):
#     conflicted_drones = set()
#     for point in drones:
#         nearest_neighbor = find_nearest_neighbor(tree=tree, point=point)
#         print(nearest_neighbor)
#         print(point)
#         if squared_distance(point, nearest_neighbor) < conflict_radius:
#             conflicted_drones.add(point)
#             conflicted_drones.add(nearest_neighbor)
#     return len(conflicted_drones)

    # j = len(drones) - 1
    # i = j - 1

    # while j > 0 and len(drones) >= 2:
    #     x = abs(drones[j][0] - drones[i][0])
    #     y = abs(drones[j][1] - drones[i][1])
    #     distance = ((x**2 ) + (y**2)) 

    #     if distance < (conflict_radius ** 2):
    #         # adding to our list of conflicted_drones
    #         conflicted_drones.add(tuple(drones[j]))
    #         conflicted_drones.add(tuple(drones[i]))

    #         # swapping the elements so that drones[i] can be the second last item in the list
    #         drones[i],drones[j-1] = drones[j-1],drones[i]

    #         # popping the last two items (conflicting drones) off the list
    #         drones.pop()
    #         drones.pop()

    #         j = len(drones) - 1
    #         i = j - 1

    #     # popping off the last drone if it had no conflicts
    #     elif i == 0:
    #         drones.pop()
    #         j = len(drones) - 1
    #         i = j - 1

    #     else:
    #         i -= 1


    # for i in range(len(drones)):
    #     for j in range(i+1,len(drones)):
    #         x = abs(drones[i][0] - drones[j][0])
    #         y = abs(drones[i][1] - drones[j][1])
    #         d = ((x**2 ) + (y**2)) ** (1/2)
    #         print(drones[i] ,drones[j], d)
    #         if d < conflict_radius:
    #             conflicted_drones.add(tuple(drones[i]))
    #             conflicted_drones.add(tuple(drones[j]))
    # print(conflicted_drones)
    return len(conflicted_drones)  

def gen_coord():
    # all drones will in the drones list will be within the airspace
    return int(random.random() * AIRSPACE_SIZE)

positions = [[gen_coord(), gen_coord()] for i in range(NUM_DRONES)]
# pp.pprint(build_kdtree(positions))
tree = build_kdtree(positions)
# conflicts = count_conflicts(positions, CONFLICT_RADIUS)
# print("Drones in conflict: {}".format(conflicts))

print(find_nearest_neighbor(tree=tree, point=[9,2]))
# print(len(NNRecord))

    