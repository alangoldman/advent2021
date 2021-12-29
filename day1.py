file = open("day1_input.txt", "r")
lines = file.readlines()
file.close()

data = [int(l) for l in lines]

increased = 0
last = None
for depth in data:
    if last is not None and depth > last:
        increased += 1
    last = depth

print(increased)

#part 2

increased = 0
window = []
windows = []
last = None
for depth in data:
    window.append(depth)
    if len(window) < 3:    
        continue
    windows.append(sum(window))
    window.pop(0)

for w in windows:
    if last is not None and w > last:
        increased += 1
    last = w

print(increased)