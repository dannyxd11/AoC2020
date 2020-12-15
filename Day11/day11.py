import numpy as np
import itertools

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

def get_adjacent_seats(n, row, col):
    seat = n[row, col]  
    (height,width) = n.shape    
    row1 = max(0, row - 1)
    row2 = min(height, row + 2)
    col1 = max(0, col - 1)
    col2 = min(width, col + 2)  

    unique, counts = np.unique(n[row1:row2,col1:col2], return_counts=True)
    adjacent_counts = dict(zip(unique, counts))
    adjacent_counts[seat] = adjacent_counts.get(seat, 0) - 1
    return adjacent_counts

def get_visible_seats(n, row, col):
    seat = n[row, col]  
    (height,width) = n.shape

    counts = {OCCUPIED: 0, EMPTY: 0}
    modifiers = list(itertools.product([-1,0,1],repeat=2))
    modifiers.remove((0,0))
    for (rm, cm) in modifiers:
        r = row + rm
        c = col + cm
        while r >= 0 and r < height and c >= 0 and c < width:
            if n[r,c] != FLOOR:
                counts[n[r,c]] += 1
                break
            
            c += cm
            r += rm    
    return counts


def run_step(n, part, rules):
    (height,width) = n.shape    
    row = 0 
    new = np.copy(n)
    changed = False
    while row < height:
        col = 0

        while col < width:   
            seat = n[row, col]                     
        
            if part == 2:
                counts = get_visible_seats(n, row, col)
            else:
                counts = get_adjacent_seats(n, row, col)

            if seat == EMPTY:
                if counts.get(OCCUPIED, 0) == rules["empty2occ"]:
                    new[row, col] = OCCUPIED
                    changed = True
            elif seat == OCCUPIED:
                if counts.get(OCCUPIED, 0) >= rules["occ2empty"]:
                    new[row, col] = EMPTY
                    changed = True
            col+=1                  
        row+=1        
    unique, counts = np.unique(new, return_counts=True)
    counts = dict(zip(unique, counts))
    return (new, changed, counts)

def part1(n):
    tmp = np.copy(n)
    changed = True
    counts = {}
    while changed:    
        (tmp, changed, counts) = run_step(tmp, 1, {"empty2occ": 0, "occ2empty": 4})    
    print("Part 1: ", counts)


def part2(n):
    tmp = np.copy(n)
    changed = True
    counts = {}
    while changed:    
        (tmp, changed, counts) = run_step(tmp, 2, {"empty2occ": 0, "occ2empty": 5})    
    print("Part 2: ", counts)

with open("challenge.txt", "r") as f:
    m = [list(x.strip()) for x in f.readlines()]

n = np.array(m)

part1(n)
part2(n)