from functools import reduce
import operator
import re

ops = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul }

def calc_expression_1(eq):
    neq = list(eq)
    matches = re.finditer(r"\(([^()]+)\)", eq)
    shift = 0
    for i, match in enumerate(matches, start=1):
        res = calc_expression_1(match.group(1))
        del neq[match.start()-shift:match.end()-shift]        
        shift += match.end() - match.start() - 1
        neq.insert(match.end()-shift-1 , res)        
    neq = "".join(neq)
    while re.findall(r"[\(\)]", neq):
        neq = calc_expression_1(neq)  

    neq = neq.strip().split(" ")    
    return str(reduce(lambda r,x: ops[x[0]](r, int(x[1])), [neq[i:i+2] for i in range(1, len(neq)-1,2 )], int(neq[0])))

def calc_expression_2(eq):
    neq = list(eq)
    matches = re.finditer(r"\(([^()]+)\)", eq)
    shift = 0
    for i, match in enumerate(matches, start=1):
        res = calc_expression_2(match.group(1))
        del neq[match.start()-shift:match.end()-shift]        
        shift += match.end() - match.start() - 1
        neq.insert(match.end()-shift-1 , res)        
    neq = "".join(neq)
    while re.findall(r"[\(\)]", neq):
        neq = calc_expression_2(neq)  

    return str(reduce(operator.mul, map(lambda part:reduce(operator.add, [int(num) for num in part.split(" + ")]), neq.split(" * "))))

with open ('challenge.txt', 'r') as f:
    expressions = [ " ".join(list(filter(lambda x: x.strip() != "", list(line)))) for line in [line.strip() for line in f.readlines()] ]

print("Part 1:", sum([int(calc_expression_1(expression)) for expression in expressions]))
print("Part 2:", sum([int(calc_expression_2(expression)) for expression in expressions]))
