import numpy as np
file = open("day6_input.txt", "r")
lines = file.readlines()
file.close()

fish_n = np.array([int(l.strip()) for l in lines[0].split(',')])
#fish_n = np.array([3,4,3,1,2]) # example

fish = {}
for i in range(11):
    fish[i] = len(fish_n[fish_n==i])

for day in range(256):
    fish[9] += fish[0]
    fish[7] += fish[0]
    fish[0] = 0
    for i in range(10):
        fish[i] = fish[i+1]
    #print(day+1, sum(fish.values()), fish)
print(sum(fish.values()))