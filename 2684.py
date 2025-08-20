import sys
input = sys.stdin.readline

for _ in range(int(input())):
    sol = [0]*8
    coin = str(input())
    for i in range(38):
        match coin[i:i+3]:
            case 'TTT':
                sol[0] += 1
            case 'TTH':
                sol[1] += 1
            case 'THT':
                sol[2] += 1
            case 'THH':
                sol[3] += 1
            case 'HTT':
                sol[4] += 1
            case 'HTH':
                sol[5] += 1
            case 'HHT':
                sol[6] += 1
            case 'HHH':
                sol[7] += 1

    sol = list(str(i) for i in sol)
        
    print(' '.join(sol))