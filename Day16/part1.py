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

for ticket in tickets:
    rules_applied = list(map( lambda v, rules=rule_ranges: v not in rules, ticket))
    if any(rules_applied):
        ticket_error_rate += sum([x[0] for x in list(filter(lambda v: v[1], zip(ticket, rules_applied)))])

print("Part 1:", ticket_error_rate)