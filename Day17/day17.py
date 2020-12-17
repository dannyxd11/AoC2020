import itertools

ACTIVE   = "#"
INACTIVE = "."

active_cubes = []

with open('challenge.txt', 'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]
    active_cubes = [item for line in [list(zip(itertools.repeat(line[0]), line[1])) for line in enumerate(lines)] for item in [(ele[0], ele[1][0], 0) for ele in enumerate(line) if ele[1][1] == ACTIVE]]