import re

pwds = []
with open('challenge.txt', 'r') as f:
    pwds = f.readlines()
    pwds = [x.replace('\n','') for x in pwds]

def parse_line(line):
    m = re.match('(\d+)-(\d+) ([a-z]): (.*)$', line)    
    return {
        "lower": int(m.group(1)),
        "upper": int(m.group(2)),
        "char": m.group(3),
        "pwd": m.group(4),
    }

def is_valid_rule(pwd):
    c = pwd["pwd"].count(pwd["char"])
    return c >= pwd["lower"] and c <= pwd["upper"]

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