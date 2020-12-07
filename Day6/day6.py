import string

def process_groups_p1(groups):
    groups_responded = []    
    for group in groups:
        responded = dict.fromkeys(string.ascii_lowercase, False)
        for response in group:
            for q in response:
                responded[q.lower()] = True
        groups_responded.append(sum([1 for k, v in responded.items() if v == True]))        
    return sum(groups_responded)

def process_groups_p2(groups):
    groups_responded = []    
    for group in groups:
        responded = dict.fromkeys(string.ascii_lowercase, 0)
        for response in group:
            for q in response:
                responded[q.lower()] += 1
        groups_responded.append(sum([1 for k, v in responded.items() if v == len(group)]))
        
    return sum(groups_responded)

groups = []
with open('challenge.txt','r') as f:
    group = []   
    lines = f.readlines() 
    i = 0
    while i < len(lines):
        if lines[i] == "\n":
            groups.append(group)
            group = []
            i+=1
            continue

        group.append(lines[i].strip())    

        if i == len(lines) - 1: 
            groups.append(group)
        i+=1        
        
print("Part 1: ", process_groups_p1(groups))
print("Part 2: ", process_groups_p2(groups))