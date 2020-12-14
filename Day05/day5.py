import math

seats = [] 
rseats = [] 
seat_ids = []
with open("challenge.txt", "r") as f:
    rseats = [x.strip() for x in f.readlines()]

for seat in rseats:
    row = int(seat[0:7].replace("B","1").replace("F","0"),2)
    col = int(seat[7:10].replace("R","1").replace("L","0"),2)
    seat_id = row * 8 + col    
    seats.append({"row": row, "col": col, "seat_id": seat_id})
    seat_ids.append(seat_id)

print("Part 1:", max(seat["seat_id"] for seat in seats))
i = 0
seat_ids = sorted(seat_ids)
last = seat_ids[i] - 1
while i < len(seat_ids):    
    if seat_ids[i] != last + 1:
        print("Part 2: Seat missing - %s (%s, %s)" % (last + 1, math.floor((last + 1)/ 8), (last+1) % 8))
        break
    last = seat_ids[i]
    i += 1