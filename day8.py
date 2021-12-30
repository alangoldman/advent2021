import numpy as np
file = open("day8_input.txt", "r")
lines = file.readlines()
file.close()

part1 = 0
part2 = 0
for line in lines:
    line = line.strip()
    patterns, output = line.split(' | ')
    patterns = patterns.split(' ')
    output = output.split(' ')

    matches = [None]*10
    segments = [None]*7

    matches[1] = set([p for p in patterns if len(p)==2][0])
    matches[4] = set([p for p in patterns if len(p)==4][0])
    matches[7] = set([p for p in patterns if len(p)==3][0])
    matches[8] = set([p for p in patterns if len(p)==7][0])

    appears = len([o for o in output if set(o) in matches])
    part1 += appears

    segments[0] = matches[7]-matches[1]
    for p in patterns:
        segments[6] = set(p)-matches[4]-matches[7]
        if len(segments[6])==1:
            matches[9] = set(p)
            break

    matches[9] = matches[4].union(matches[7].union(segments[6]))
    segments[4] = matches[8]-matches[9]
    patterns = [set(p) for p in patterns if set(p) not in matches]
    
    for p in patterns:
        s = matches[8]-set(p)    
        if len(s)==1:
            if len(matches[8]-set(p)-matches[1]) == 0:
                segments[2] = s
                matches[6] = set(p)
            else:
                segments[3] = s
                matches[0] = set(p)
    matches[3] = matches[7].union(segments[6].union(segments[3]))
    matches[0] = matches[8]-segments[3]
    matches[5] = matches[8]-segments[2]-segments[4]
    patterns = [set(p) for p in patterns if set(p) not in matches]
    matches[2] = patterns[0]

    display = ""
    for o in output:
        for i in range(len(matches)):
            if set(o) == matches[i]:
                display += str(i)
                break
                
    #print(display)
    part2 += int(display)

print(part1, part2)