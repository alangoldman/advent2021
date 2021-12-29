import numpy as np
file = open("day5_input.txt", "r")
lines = file.readlines()
file.close()

segements = [l.strip().split(' -> ') for l in lines]
points = []
max_x = 0
max_y = 0
for point1, point2 in segements:
    x1, y1 = point1.split(',')
    x2, y2 = point2.split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    max_x = max(max_x, x1, x2)
    max_y = max(max_y, y1, y2)
        
    points.append((x1, y1, x2, y2))

grid = np.zeros((max_y+1, max_x+1))    
for x1,y1,x2,y2 in points:
    if x1==x2:
        low, high = (y1, y2+1) if y1<y2 else (y2, y1+1)
        grid[low:high, x1] += 1
    elif y1==y2:
        low, high = (x1, x2+1) if x1<x2 else (x2, x1+1)
        grid[y1, low:high] += 1
    else:
        #continue
        #part 2
        i,j = x1,y1
        while i!=x2 and j!=y2:
            grid[j,i] += 1
            i += 1 if x2>x1 else -1
            j += 1 if y2>y1 else -1
        grid[y2,x2] += 1
        
print(len(grid[grid>=2]))