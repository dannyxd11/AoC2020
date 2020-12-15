from functools import reduce
from operator import mul

adapters = []
with open("challenge.txt", "r") as f:
    adapters = [int(adapter.strip()) for adapter in f.readlines()]

adapters.insert(0,0)
adapters = sorted(adapters)
chunked = [tuple(adapters[i : i + 2]) for i in range(0, len(adapters), 1)][:-1]
stepc = {3:1}
steps = []

for chunk in chunked:
    step = chunk[-1] - chunk[0]
    stepc[step] = stepc.get(step, 0) + 1
    steps.append(step)

print("Part 1:", stepc.get(1,0) * stepc.get(3,0))

x = []
nperms = [] 
for group in list(filter(lambda x: x != '', "".join([str(diff) for diff in steps]).split("3"))):
    p = pow(2,group.count('1')-1)
    nperms.append(7 if p == 8 else p)

print("Part 2:", reduce(mul, nperms, 1))