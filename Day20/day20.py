from bitstring import BitArray
from collections import Counter, defaultdict
from functools import reduce
import itertools
import numpy as np
import operator
import re

## Numpy:
## flipud  Flip an array vertically (axis=0).
## fliplr  Flip an array horizontally (axis=1).

raw_tiles = []
processed_tiles = {}
rlookup = defaultdict(list)

def parse_edge(edge):
    i = BitArray(edge).uint
    inverse = BitArray(edge[::-1]).uint
    return (i, inverse)

def parse_tile(tile):
    match = re.match("Tile (\d+):", tile.pop(0))
    id = int(match.group(1))
    tile = [ list(map(lambda x: 1 if x == "#" else 0, list(row))) for row in tile]
    array = np.array(tile)        
    (top, bottom) = (array[0,:], array[-1,:])
    (left, right) = (array[:,0], array[:,-1])

    return {
        "id": id,
        "tile": array,
        "edges": {
            "top": parse_edge(top),
            "bottom": parse_edge(bottom),
            "left": parse_edge(left),
            "right": parse_edge(right)
        }
    }

with open("challenge.txt", "r") as f:
    raw_tiles = [[z.strip() for z in list(y)] for x, y in itertools.groupby(f.readlines(), lambda z: z == "\n") if not x]

for tile in raw_tiles:
    ptile = parse_tile(tile)
    for edge, value in ptile["edges"].items():
        rlookup[value[0]].append({"tile_id": ptile["id"], "edge": edge, "inverse": False })
        rlookup[value[1]].append({"tile_id": ptile["id"], "edge": edge, "inverse": True })
    processed_tiles[ptile["id"]] = ptile

corners = {k: v for k, v  in dict(Counter([n["tile_id"] for k, v in rlookup.items() for n in v if len(v) < 2])).items() if v == 4}

print("Part 1: ", reduce(operator.mul, corners.keys()))

# Actually reconstruct..
def get_tile_with_edge(processed_tiles, needle, exclude = []): 
    print([(key, v) for key, val in processed_tiles.items() for k, v in val["edges"].items() if needle in v])    
    return [(key, k, v) for key, val in processed_tiles.items() for k, v in val["edges"].items() if needle in v and key not in exclude]

start = list(corners.keys())[0]
print(get_tile_with_edge(processed_tiles, 480, [2693]))
print(get_tile_with_edge(processed_tiles, 480, []))

print(len(processed_tiles))