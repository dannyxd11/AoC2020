import copy
from itertools import repeat, product

ACTIVE   = "#"
INACTIVE = "."

cubes = {}
is_active = lambda cube: cube == ACTIVE 
filter_active_cubes = lambda cubes: dict((k, v) for k, v in cubes.items() if is_active(v))

def get_adjacent_cubes(cube):
    x, y, z, w = cube
    adjacent_cubes = list(product(range(x-1, x+2, 1), range(y-1, y+2, 1), range(z-1, z+2, 1), range(w-1, w+2, 1)))    
    adjacent_cubes.remove(cube)
    return adjacent_cubes

def get_active_cubes(cube, cubes):
    adjacent_cubes = set(get_adjacent_cubes(cube))
    active_cubes   = set(filter_active_cubes(cubes))
    return adjacent_cubes & active_cubes

def update_cubes(cube, cubes):
    adjacent_cubes = set(get_adjacent_cubes(cube))
    active_cubes   = set(filter_active_cubes(cubes))
    for coord in adjacent_cubes - set(cubes.keys()):
        cubes[coord] = cubes.get(coord, INACTIVE)
    return cubes
    
# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. 
# Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. 
# Otherwise, the cube remains inactive.

def process_click(cubes):
    ncubes = copy.deepcopy(cubes)
    for kcube, vcube in cubes.items():
        ncubes = update_cubes(kcube, ncubes)
    out = copy.deepcopy(cubes)
    for kcube, vcube in ncubes.items():             
        adjacent_active_cubes = get_active_cubes(kcube, ncubes)

        if is_active(vcube) and len(adjacent_active_cubes) not in [2, 3]:
            out[kcube] = INACTIVE
        if not is_active(vcube) and len(adjacent_active_cubes) == 3:
            out[kcube] = ACTIVE
    return out


#### 

with open('challenge.txt', 'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]
    cubes = {(item[0], item[1], 0, 0):item[2] for line in [list(zip(repeat(line[0]), line[1])) for line in enumerate(lines)] for item in [(ele[0], ele[1][0], ele[1][1]) for ele in enumerate(line)]}    

for step in range(1, 7): 
    cubes = process_click(cubes)        
    print("Part 1: Step %s - %s active cubes" % (step, len(filter_active_cubes(cubes).items())))


