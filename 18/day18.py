#%%
import numpy as np
import math
import sys
from collections import defaultdict

#%%
input_file = "./day18.in1"
with open(input_file, 'r') as f:
    input_lines = f.readlines()

input_lines = [list(x.strip('\n')) for x in input_lines]
data = np.array(input_lines)
# print(data)

mv_ptr = np.where(data=='@')
mv_ptr = np.array(mv_ptr).reshape(2)
# print(data[tuple(mv_ptr)])

def search_paths(mv_ptr):
    global data
    path_list = []
    for k in [[0,1], [0, -1], [1, 0], [-1, 0]]:
        ind = tuple(mv_ptr + np.array(k))
        if data[ind] == '.':
            path_list.append(ind)

    return path_list

print(search_paths(mv_ptr))
    
        

# %%
