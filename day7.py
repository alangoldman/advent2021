import numpy as np
file = open("day7_input.txt", "r")
lines = file.readlines()
file.close()

crabs = np.array([int(l) for l in lines[0].split(',')])
#crabs = np.array([16,1,2,0,4,2,7,1,2,14]) # example

best = None
for i in range(max(crabs)+1):
    dists = np.abs(crabs-i)
    # fuel = np.sum(dists) # part a
    fuel = np.sum(dists*(dists+1)/2) # part b
    if best is None or fuel < best[1]:
        best = i, fuel
        
print(best)