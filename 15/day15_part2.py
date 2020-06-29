#%%
from datetime import datetime
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from time import sleep

get_ipython().run_line_magic('matplotlib', 'notebook')

data2 = np.load("/Users/spalani/OneDrive - Analog Devices, Inc/git_proj/aoc2019/spalani/15/outtile_map_droid_part1.npy")

fig,ax = plt.subplots(1,1)
image = Image.fromarray(data2.astype('uint8')).convert('RGB')
im = ax.imshow(image)

data3 = np.copy(data2)
droid_ptr = [5, 3]
data3[droid_ptr[0], droid_ptr[1]] = 220

def spread_oxygen():
    global data3, droid_ptr, im, fig, minutes_cnt, updated_already
    fill = [(0, droid_ptr)]
    while len(fill):
        minutes, pos = fill.pop(0)
        for adj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ptr = pos[0] + adj[0], pos[1] + adj[1]
            if data3[ptr[0], ptr[1]] == 0:
                im.set_data(Image.fromarray(data3.astype('uint8')).convert('RGB'))
                fig.canvas.draw()
                data3[ptr[0], ptr[1]] = 220
                fill.append((minutes+1, ptr))
    print(minutes)
    
spread_oxygen()
fig.show()

# %%
