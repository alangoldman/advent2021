import numpy as np
file = open("day9_input.txt", "r")
lines = file.readlines()
file.close()

m = ['9'+l.strip()+'9' for l in lines]
m = ["9"*len(m[0])] + m + ["9"*len(m[0])]

low_points = []
part1 = 0
for i in range(1, len(m)-1):
    for j in range(1, len(m[0])-1):
        height = m[i][j]
        lowpoint = True
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            x = i+di
            y = j+dj
            if m[x][y] <= height:
                lowpoint = False
        if lowpoint:
            part1 += 1+int(height)

basin_count = 0
basins = [[None]*len(m[0]) for i in range(len(m))]

def flood_fill(i, j, n):
    area = 0
    queue = [(i, j)]
    while len(queue) > 0:
        i, j = queue.pop(0)
        if basins[i][j] is not None:
            continue
        basins[i][j] = n
        area += 1
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            x = i+di
            y = j+dj
            if basins[x][y] is None and m[x][y] != '9':
                queue.append((x, y))
    return area

basin_areas = []
for i in range(1, len(m)-1):
    for j in range(1, len(m[0])-1):
        if basins[i][j] is not None:
            continue
        if m[i][j] == '9':
            continue
        # flood fill
        area = flood_fill(i, j, basin_count)
        basin_areas.append(area)
        basin_count += 1

best = sorted(basin_areas, reverse=True)[0:3]
print(best[0]*best[1]*best[2])