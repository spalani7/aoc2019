import numpy as np
import math
import sys

input1 = (236491, 713787)

part2 = False

count = 0
for i in range(*input1):
    flag = True
    fflag = True
    strI = str(i)
    prev_char = strI[0]
    num_repeated = {}

    for c in strI:
        num_repeated[c] = 1
        
    for c in strI[1:]:
        if c < prev_char:
            flag = False
            break
        if c == prev_char:
            num_repeated[c] += 1
        prev_char = c
    
    if part2:
        if 2 not in num_repeated.values():
            fflag = False
    else:
        fflag = False
        for i in num_repeated.values():
            if i >=2:
                fflag = True
        
    if flag and fflag:
        count += 1

print(count)

# part 1 solution: 1169
# part 2 solution: 757
