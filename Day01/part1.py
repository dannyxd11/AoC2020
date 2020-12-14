accounts = []
with open('challenge.txt', 'r') as f:
    accounts = f.readlines()
    accounts = [int(x.replace('\n','')) for x in accounts]

i = 0
while i < len(accounts):
    j = len(accounts) - 1
    while j >= 0: 

        t = accounts[i] + accounts[j]
        if ( t < 2020):
            break
        if ( t == 2020 ):
            print("Found! [%s],[%s] %s * %s = %s" % (i,j, accounts[i], accounts[j], accounts[i] * accounts[j]))        
            exit(0)
        j -= 1
    i += 1 