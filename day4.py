import numpy as np
file = open("day4_input.txt", "r")
lines = file.readlines()
file.close()

numbers = [int(l) for l in lines[0].strip().split(',')]
boards = []
i=2
while i<len(lines):
    board = np.zeros((5,5))
    for j in range(5):
        line = lines[i].strip()
        if line == "":
            i += 1
            line = lines[i].strip()
        nums = [l.strip() for l in line.split(' ') if l.strip()]
        board[j,:] = nums
        i += 1
    boards.append(board)
    
marked = [np.zeros((5,5), dtype=bool) for i in range(len(boards))]

def solved(b):
    for i in range(5):
        if np.all(b[i] == True):
            return True
        if np.all(b[:,i] == True):
            return True
    return False

def score(m, b, n):
    s = 0
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if not m[i,j]:
                s += b[i,j]
    return s*n

done = np.zeros((len(boards), 1)) #part 2
for num in numbers:
    for i in range(len(boards)):
        if done[i] == 1:
            continue
        for idx in np.argwhere(boards[i]==num):
            marked[i][idx[0], idx[1]] = True
        if solved(marked[i]):
            done[i] = 1
            print(i, score(marked[i], boards[i], num))
    if np.sum(done) == len(boards):
        break
