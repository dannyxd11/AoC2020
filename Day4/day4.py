import re
rppts = []

with open('challenge.txt', 'r') as f:
    ppt = []
    for line in f.readlines():        
        if line == "\n": 
            rppts.append(ppt)
            ppt = []
            continue
        ppt += line.strip().split(" ")
    rppts.append(ppt)

class Passport():
    def __init__(self, attrs):
        for attr in attrs:
            (key, val) = attr.split(":")
            setattr(self, key, val)

    def isValidYear(self, attr, lower, upper):
        val = getattr(self, attr)
        try:
            ival = int(val)
            return ival <= upper and ival >= lower
        except:
            return False

    def isValidP1(self, ignore = []):        
        for attr in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]:
            if getattr(self, attr, None) == None and attr not in ignore:
                return False
        return True

    def isValidP2(self, ignore = []):  
        if not self.isValidP1(ignore):     
            return False

        if not self.isValidYear("byr", 1920, 2002) and "byr" not in ignore: return False
        if not self.isValidYear("iyr", 2010, 2020) and "iyr" not in ignore: return False
        if not self.isValidYear("eyr", 2020, 2030) and "eyr" not in ignore: return False
        
        hgt = re.search("(\d+)(cm|in)", getattr(self, "hgt", ""))                
        if not hgt and "hgh" not in ignore: return False        
        if hgt.group(2) == "cm" and not 150 <= int(hgt.group(1)) <= 193  and "hgh" not in ignore: return False
        if hgt.group(2) == "in" and not 59 <= int(hgt.group(1)) <= 76 and "hgh" not in ignore: return False
        
        hcl = re.search("#[0-9a-f]{6}$", getattr(self, "hcl", ""))                
        if not hcl and "hcl" not in ignore: return False
        
        if getattr(self, "ecl", "") not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]  and "ecl" not in ignore: return False
        
        pid = re.search("^[0-9]{9}$", getattr(self, "pid", "")) 
        if not pid and "pid" not in ignore: return False

        return True

    def __str__(self):
        out = ""
        for attr in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]:
            out += "%s: %s " % (attr, getattr(self, attr, ""))        
        return out

count_valid_1 = 0
count_valid_2 = 0
for i in rppts:
    p = Passport(i)
    if p.isValidP1(["cid"]):
        count_valid_1 += 1
    if p.isValidP2(["cid"]):
        print(p)
        count_valid_2 += 1

print ("Part 1: %s" % (count_valid_1))
print ("Part 2: %s" % (count_valid_2))