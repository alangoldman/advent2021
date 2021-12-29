import numpy as np
file = open("day6_input.txt", "r")
lines = file.readlines()
file.close()

fish = np.array([int(l.strip()) for l in lines[0].split(',')])
#fish = np.array([3,4,3,1,2]) # example
 
for day in range(256):
    fish = np.append(fish, np.ones((len(fish[fish==0])))*9)
    fish[fish==0] = 7
    fish -= 1
    #print(day+1, len(fish), fish)
print(len(fish))