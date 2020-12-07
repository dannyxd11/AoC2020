accounts = []
with open('challenge.txt', 'r') as f:
    accounts = f.readlines()
    accounts = [int(x.replace('\n','')) for x in accounts]


saccounts = sorted(accounts)

a = []
i = 0
while i < len(saccounts):
    tmp = []
    j = 0
    while j < len(saccounts):
        if i == j or saccounts[i] + saccounts[j] >= 2020:  break
        if saccounts[i] + saccounts[j] < 2020: 
            tmp.append(saccounts[j])
        j += 1
    a.append((saccounts[i], tmp))
    i += 1
    

i = 0
while i < len(saccounts):
    print(i)
    for j in a:
        first_two = j[0] + saccounts[i]
        if first_two < 2020:
            k = 0
            while k < len(j[1]):
                if first_two + j[1][k] > 2020: break
                if first_two + j[1][k] == 2020: 
                    print("Found! [%s],[%s],[%s] %s * %s * %s = %s" % (i,j[0],k, saccounts[i], j[0], j[1][k], saccounts[i] * j[0] * j[1][k]))        
                    exit(0)
                k += 1
    i += 1

