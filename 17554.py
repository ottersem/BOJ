import sys, time
input = sys.stdin.readline

l = int(input())
lights = [True]*(l+1)
lights[0] = False
off = 0
cnt = 0

for _ in range(int(input())):
    n = int(input())

    for i in range(n,l+1,n):
        if lights[i]:
            cnt += 1
        else:
            cnt -= 1
        lights[i] = not lights[i]
        
    off = max(off, cnt)

print(off)
