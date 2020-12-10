from datetime import datetime
startTime = datetime.now()

def is_possible(preamble, signal):
    i = 0
    p = sorted(preamble, reverse = True)
    max_preamble = p[0] + p[1]
    
    if signal > max_preamble:
        return (False, signal)

    while i < len(preamble):         
        if p[i] >= signal: 
            i+=1 
            continue
        j = len(p) - 1        
        while j > 0:                              
            if p[i] + p[j] < signal or i == j or p[i] == p[j] : 
                j-=1
                continue            
            if p[i] + p[j] > signal: break
            if p[i] + p[j] == signal: 
                return (True, p[i], p[j], signal)
            j-=1            
        i+=1
    return (False, signal)

lines = []

with open('challenge.txt','r') as f:
    lines = [int(line.strip()) for line in f.readlines()]

p1 = 0
idx = 25
while idx < len(lines):
    possible = is_possible(lines[idx-25:idx], lines[idx])    
    if not possible[0]:
        p1 = possible[1]
        print("Part 1: %s" % (p1))
        break
    idx += 1

idx = 0
con = 1
while idx < len(lines):
    contiguous_sum = sum(lines[idx:idx+con])
    if contiguous_sum < p1:
        con += 1
    elif contiguous_sum > p1:
        idx += 1
        con = 1
    elif contiguous_sum == p1:
        tmp = sorted(lines[idx:idx+con])        
        print("Part 2: %s [%s + %s]" % (min(tmp) + max(tmp), min(tmp) , max(tmp)))
        break    
    else:
        print("err..")

print("Time Taken: %s" % (datetime.now() - startTime))