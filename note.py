def female(integer, status):
    i=1
    num = integer
    t=[num-1]

    while True:
        before, after = num+i-1, num-i-1
        if after < 0 or before > len(status):
            break
        if status[before] == status[after]:
            t.extend([before,after])
        else:
            break
        
        i += 1

    for i in t:
        status[i] = action(status[i])

    return status

def action(num):
    if num == 0: return 1
    else: return 0

print(female(3,[0,1,1,1,0,1,0,1]))