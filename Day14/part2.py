from itertools import product
import re

def parse_mask(mask):
    m = { "0": [], "1": [], "X": [] }
    for i, bit in enumerate(mask[::-1]):
        if bit == "0":
            m["0"].append(i)
        elif bit == "1":
            m["1"].append(i)   
        elif bit == "X":
            m["X"].append(i)
    return m

def turnOffBit(n, i):
    return (n & ~(1 << i)) 

def turnOnBit(n, i):
    return (n | (1 << i)) 

def int_to_bitstring(num):
    return("{0:b}".format(num)).zfill(36)

def apply_mask(n, mask):    
    new_val = n
    out = []
    m = parse_mask(mask)     
    for ind in m["1"]:
        new_val = turnOnBit(new_val, ind)     
    
    combinations = [x for x in product([0,1],repeat=len(m["X"]))]
    for comb in combinations:
        tmp = new_val
        for ind, val in zip(m["X"], comb):              
            tmp = turnOnBit(tmp, ind) if val == 1 else turnOffBit(tmp, ind)        
        out.append(tmp)
    return out
    

lines = [] 
with open('challenge.txt','r') as f:
    lines = [line.strip() for line in f.readlines()]

mask = ""

memory = dict()
for line in lines:
    match = re.match("mask = ([01X]+)", line)
    if match:
        mask = match.group(1) 
        continue
    
    match = re.match("mem\[(\d+)\] = (\d+)", line)    
    if match:
        address = int(match.group(1))
        val = int(match.group(2))
        addresses = apply_mask(address, mask)   
        for a in addresses:
            memory[a] = val


print("Part 2:",  sum(memory.values()))