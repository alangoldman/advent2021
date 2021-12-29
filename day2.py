file = open("day2_input.txt", "r")
lines = file.readlines()
file.close()

moves = [l.strip().split(' ') for l in lines]

horizontal = 0
depth = 0
for move, s in moves:
    i = int(s)
    if move == "forward":
        horizontal += i
    elif move == "down":
        depth += i
    elif move == "up":
        depth -= i
        
print(horizontal, depth, horizontal*depth)

#part 2
horizontal = 0
depth = 0
aim = 0
for move, s in moves:
    i = int(s)
    if move == "forward":
        horizontal += i
        depth += aim*i
    elif move == "down":
        aim += i
    elif move == "up":
        aim -= i
        
print(horizontal, depth, horizontal*depth)