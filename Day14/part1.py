import re

def parse_mask(mask):
    m = { "0": [], "1": [] }
    for i, bit in enumerate(mask[::-1]):
        if bit == "0":
            m["0"].append(i)
        elif bit == "1":
            m["1"].append(i)        
    return m

def turnOffBit(n, i):
    return (n & ~(1 << i)) 

def turnOnBit(n, i):
    return (n | (1 << i)) 

def int_to_bitstring(num):
    return("{0:b}".format(num)).zfill(36)

def apply_mask(n, mask):    
    new_val = n
    m = parse_mask(mask)
    for ind in m["0"]:
        new_val = turnOffBit(new_val, ind)        
    for ind in m["1"]:
        new_val = turnOnBit(new_val, ind)              
    return new_val
    

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
        memory[address] = apply_mask(val, mask)

print("Part 1:",  sum(memory.values()))