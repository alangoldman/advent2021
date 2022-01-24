import numpy as np
file = open("day12_input.txt", "r")
lines = file.readlines()
file.close()

adj = {}

for line in lines:
    line = line.strip()
    first, second = line.split('-')
    if first not in adj:
        adj[first] = set()
    if second not in adj:
        adj[second] = set()
    adj[first].add(second)
    adj[second].add(first)
    
closed = set()
path = ['start']

def dfs(node): 
    #print(node, closed)
    count = 0
    if node == node.lower():
        closed.add(node)
    if node == 'end':
        count += 1
        print('Path!', count, path)
    for child in adj[node]:
        if child not in closed:
            path.append(child)
            count += dfs(child)
            path.pop()

    # backtracking
    if node == node.lower():
        closed.remove(node)
    return count

print(dfs('start'))