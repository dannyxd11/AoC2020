challenge = [5,1,9,18,13,8,0]

def play_n_times(challenge, n):
    last = challenge[1]    
    spoken = {number: (0, turn+1) for turn, number in enumerate(challenge)}
    for i in range(len(challenge) + 1, n + 1):        
        last = 0 if spoken[last][0] == 0 else spoken[last][1] - spoken[last][0]        
        spoken[last] = (0, i) if last not in spoken else (spoken[last][2], i)        
    return last

print("Part 1: %s" % (play_n_times(challenge,2020)))
print("Part 2: %s" % (play_n_times(challenge,30000000)))