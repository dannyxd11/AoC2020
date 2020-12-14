import re

pwds = []
with open('challenge.txt', 'r') as f:
    pwds = f.readlines()
    pwds = [x.replace('\n','') for x in pwds]

def parse_line(line):
    m = re.match('(\d+)-(\d+) ([a-z]): (.*)$', line)    
    return {
        "apos": int(m.group(1)),
        "dpos": int(m.group(2)),
        "char": m.group(3),
        "pwd": m.group(4),
    }

def is_valid_rule(pwd):
    c = pwd["char"]
    apos = pwd["pwd"][pwd["apos"]-1]
    dpos = pwd["pwd"][pwd["dpos"]-1]
    return (c == apos and c != dpos) or (c == dpos and c != apos)

valid_count = 0
invalid_count = 0
hpwds = []
for i in pwds:
    pwd = parse_line(i)
    valid = is_valid_rule(pwd)
    pwd["is_valid"] = valid
    if valid:
        valid_count += 1
    else:
        invalid_count += 1

print ("Valid: %s, Invalid: %s" % (valid_count,invalid_count))