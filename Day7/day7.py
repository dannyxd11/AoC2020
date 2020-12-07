import re

def parse(line):
    pattern = re.compile('^([\w\s]+)(?: bags contain )([\w\s,]+)(?=.)')
    match = pattern.match(line)

    container = match.group(1)
    contains_str = [x.strip() for x in match.group(2).replace(" bags","").replace(" bag","").split(",")]
    contains_str = [] if "no other" in contains_str else contains_str
    contains = []
    for bag in contains_str:
        pattern = re.compile('(\d+) ([\w\s]+)')
        match = pattern.match(bag)        
        contains.append({"name": match.group(2), "quant": int(match.group(1))})

    return (container, {
        "raw" : contains_str,        
        "contains_str": [x["name"] for x in contains],
        "contains": contains
    })

def filter_bags(bags, bag):
    ret = {}
    for k, v in bags.items():
        if bag in v["contains_str"]:
            ret[k] = v
    return ret
    
def get_allowed_containers(bags, bag, done = set()):   
    search = set(filter_bags(bags, bag).keys())  
    searched = search | done
    to_search = search - done    
    for b in to_search:        
        searched.update(get_allowed_containers(bags, b, searched))        
    return searched

def get_number_of_children(bags, bag):
    count = 0
    for b in bags[bag]["contains"]:        
        count += b["quant"] * (1 + get_number_of_children(bags, b["name"]))
    return count

bags = []
with open('challenge.txt', 'r') as f:    
    bags = {k: v for k,v in [parse(x.strip()) for x in f.readlines()]}

print("Part 1: %s" % (len(get_allowed_containers(bags, "shiny gold"))))
print("Part 2: %s" % (get_number_of_children(bags, "shiny gold")))
        