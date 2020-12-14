import copy

def parse_instruction(line):
    tmp = line.split(" ")
    instruction = tmp[0]
    params = [int(p) for p in tmp[1:]]
    return {
        "instruction": instruction,
        "params": params
    }

def execute_instruction(program, ip, reg):    
    if program[ip]["instruction"] == "nop":
        return (program, ip + 1, reg)
    elif program[ip]["instruction"] == "acc":        
        reg["acc"] = reg.get("acc",0) + program[ip]["params"][0]
        return (program, ip + 1, reg)
    elif program[ip]["instruction"] == "jmp":
        return (program, ip + program[ip]["params"][0], reg)
    else:
        print("Unrecognised instruction...")
        exit(1)

def execute(program, ip = 0):   
    visited_ips = []
    reg = {} 
    while ip < len(program):        
        if ip in visited_ips:             
            break       
        visited_ips.append(ip)
        (program, ip, reg) = execute_instruction(program, ip, reg)
    return {"ip": ip, "reg": reg}

def fix_execute(program, ip = 0 ):        
    flippable_instructions = [(i, v["instruction"]) for i, v in enumerate(program) if v["instruction"] in ["nop", "jmp"]]    
    regs = {}    
    while len(flippable_instructions) > 0:       
        p = copy.deepcopy(program)     
        (i, v) = flippable_instructions.pop()        
        p[i]["instruction"] =  "nop" if v == "jmp" else "jmp"                 
        regs[i] = execute(p)
    return regs

program = []

with open('challenge.txt', 'r') as f:
    for line in [line.strip() for line in f.readlines()]:
        program.append(parse_instruction(line))

print("Part 1:", execute(program))
print("Part 2:", max([ v for k, v in fix_execute(program).items()], key=lambda x:x["ip"]))