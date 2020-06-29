#%%
import math
import numpy as np
from multiprocessing import Process, Queue
from timeit import default_timer as timer

#%%
inp_str = "59728839950345262750652573835965979939888018102191625099946787791682326347549309844135638586166731548034760365897189592233753445638181247676324660686068855684292956604998590827637221627543512414238407861211421936232231340691500214827820904991045564597324533808990098343557895760522104140762068572528148690396033860391137697751034053950225418906057288850192115676834742394553585487838826710005579833289943702498162546384263561449255093278108677331969126402467573596116021040898708023407842928838817237736084235431065576909382323833184591099600309974914741618495832080930442596854495321267401706790270027803358798899922938307821234896434934824289476011"
# inp_str = "03036732577212944063491565474664"
inp_str = "12345678"
# inp_str = "80871224585914546619083218645595"
# inp_str = "19617804207202209144916044189917"
# inp_str = "69317163492948606335995924319873"

#%%
sig = np.array([int(x) for x in list(inp_str)], dtype='int8')
# sig = np.tile(sig, 10000)
input_len = sig.size

#%%
pat = np.array([0, 1, 0, -1], dtype='int8')
pat_full = np.zeros((input_len, input_len), dtype='int8')
# output = np.zeros(input_len)
sig = np.tile(sig, (input_len,1))

#%%
def popl_pat():
    global pat, sig, input_len
    for i in range (0, len(sig)):
        pat_temp = np.repeat(pat, i+1)
        padding_length = input_len - (pat_temp.size - 1)
        padding_length = 0 if padding_length < 0 else padding_length
        pat_temp = np.tile(pat_temp, 1 + math.ceil(padding_length/pat_temp.size))
        pat_full[i] = pat_temp[1:1+input_len]

cur_time = timer()
popl_pat()
print("Pat finished [{:.3f}]s".format(timer()-cur_time))
# print(pat_full)

def cal_output(sig, pat, out_idx):
    global output
#     out_len = sig.size
    pat_temp = np.repeat(pat, out_idx)
    padding_length = sig.size - (pat_temp.size - 1)
    padding_length = 0 if padding_length < 0 else padding_length
    pat_temp = np.tile(pat_temp, 1 + math.ceil(padding_length/pat_temp.size))
    pat_temp = pat_temp[1:1+sig.size]
    output[out_idx-1] = abs(np.sum(sig[pat_temp==1])-np.sum((sig[pat_temp==-1]))) % 10

def func1(a):
    global pat_full, sig
    return abs(np.sum(a)) % 10

phase_cnt = 0
while phase_cnt < 100:
    cur_time = timer()
    p = []
    t = {}
    sig = sig*pat_full
    output = abs(np.sum(sig, axis=1, dtype='int8'))%10 #np.apply_along_axis(func1, 1, sig)
    print("Phase: {}, output= {} [{:.3f}]s".format(phase_cnt, output, timer() - cur_time))
    sig = np.copy(output)
    phase_cnt += 1
print(output[0:8])
offset = int(inp_str[0:8])
print(output[offset:offset+8])

# %%
