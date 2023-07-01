def count_conflicts(drones, conflict_radius):
    for i in range(len(drones)):
        for j in range(i+1,len(drones)):
            print(i,j)
            
count_conflicts([1,2,3,4,5],10)