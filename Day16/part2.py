from functools import reduce  # Required in Python 3
import numpy as np
import operator
import re

def parse_rule(line):        
    match = re.match("([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)", line)
    (name, c1l, c1h, c2l, c2h) = match.groups()
    return (name, int(c1l), int(c1h), int(c2l), int(c2h))
    
def determine_gaps(rules):
    return list(set([n for ns in [list(range(rule[1], rule[2]+1)) + list(range(rule[3], rule[4]+1)) for rule in rules] for n in ns]))

def load_file(filename):
    with open('challenge.txt', 'r') as f:
        lines = [x.strip() for x in f.readlines() if x.strip() != ""]

    sections = ["your ticket", "nearby tickets"]
    section = "rules"
    myticket = []
    tickets = []
    rules = []

    for line in lines:     
        if line.replace(":","") in sections:
            section = line.replace(":","")
            continue

        if section == "rules":
            rule = parse_rule(line)
            rules.append(rule)
        
        if section == "your ticket":        
            myticket = [int(x) for x in line.split(",")]

        if section == "nearby tickets" and line not in sections:
            tickets.append([int(x) for x in line.split(",")])

    return (rules, myticket, tickets)

(rules, myticket, tickets) = load_file('challenge.txt')
rule_ranges = determine_gaps(rules)
ticket_error_rate = 0
valid_tickets = []

for ticket in tickets:
    rules_applied = list(map( lambda v, rules=rule_ranges: v not in rules, ticket))
    if any(rules_applied):
        ticket_error_rate += sum([x[0] for x in list(filter(lambda v: v[1], zip(ticket, rules_applied)))])
    else: 
        valid_tickets.append(ticket)

print("Part 1:", ticket_error_rate)

def which_rules_fit(vals, rules):
    return [(rule[0], all(map( lambda v, rule=rule[1]: rule[1] <= v <= rule[2] or rule[3] <= v <= rule[4], vals))) for rule in enumerate(rules)]
    
arr = np.array(valid_tickets)
(height, width) = arr.shape
col = 0 

# Columns are rules in order, rows are columns of the tickets
match_matrix = []

while col < width:
    match_matrix.append([x[1] for x in which_rules_fit(arr[:,col], rules)])
    col += 1

mm = np.array(match_matrix)
solution_found = False
# print(np.array2string(mm, max_line_width=np.inf))

while not solution_found:
    for i in range(0, width):        
        unique, counts = np.unique(mm, return_counts=True)
        counts = dict(zip(unique, counts))  
        if counts[True] == width:
            solution_found = True
            break

        unique, counts = np.unique(mm[i, :], return_counts=True)
        counts = dict(zip(unique, counts))        
        if counts[True] == 1:
            col = np.where(mm[i, :] == True)[0][0]
            unique, counts = np.unique(mm[:, col], return_counts=True)
            counts = dict(zip(unique, counts))                    
            if counts[True] == 1: 
                continue # Already fixed
            mm[:, col] = False
            mm[i, col] = True
            break

rules2col = {}

for i in list(zip(*np.where(mm[:, :] == True))):
    rules2col[rules[i[1]][0]] = i[0]

print("Part 2:", reduce(operator.mul, [myticket[col] for key,col in rules2col.items() if key.startswith("departure")], 1))
        