import numpy as np
from sympy.ntheory.modular import crt

def part1(earliest, buses):        
    print("Part 1: %s" % (min([(i, x, x*(earliest//x + 1) - earliest, x*(x*(earliest//x + 1) - earliest)) for i, x in buses], key=lambda x: x[2])[3]))

def part2(buses): 
    ids = np.array([b[1] for b in buses])
    inds = np.array([b[0] for b in buses])
    c = crt(ids, inds)
    print("Part 2: %s" % (c[1]-c[0]))

earliest = 0
with open('challenge.txt','r') as f:    
    lines = [line.strip() for line in f.readlines()]    
    earliest = int(lines[0])
    buses = [(i,int(bus)) for i, bus in enumerate(lines[1].split(",")) if bus != "x"]

part1(earliest, buses)
part2(buses)
