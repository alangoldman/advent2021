import numpy as np
file = open("day11_input.txt", "r")
lines = file.readlines()
file.close()

grid = np.array([[int(c) for c in line.strip()] for line in lines])

step = 0
while True:
    step += 1
    count = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            grid[i, j] += 1

    flash = True
    while flash:
        flash = False
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if (grid[i, j] <= 9):
                    continue
                grid[i, j] = 0
                flash = True
                count += 1
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
                    x = i+di
                    y = j+dj
                    if x >= 0 and y >= 0 and x < grid.shape[0] and y < grid.shape[1] and grid[x, y] > 0:
                        grid[x, y] += 1
    if count == 100:
        print(step)
        break