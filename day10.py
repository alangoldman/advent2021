import numpy as np
file = open("day10_input.txt", "r")
lines = file.readlines()
file.close()

# corrupt = closes with wrong character
# incomplete = skip for now
close_map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
score_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
score_map2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = list()
for line in lines:
    line = line.strip()
    stack = list()
    corrupted = False
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        else:
            last = stack.pop()
            if c != close_map[last]:
                print(f'Expected {close_map[last]}, but found {c} instead.')
                corrupted = True
                #score += score_map[c]
                break

    if not corrupted and len(stack) != 0:
        print('Incomplete')
        complete = ''
        while len(stack) > 0:
            complete += close_map[stack.pop()]
        score = 0
        for c in complete:
            score = score * 5 + score_map2[c]
        print(complete, score)
        scores.append(score)
        
scores.sort()
print(scores[int(len(scores)/2)])