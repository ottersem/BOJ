import sys
input = sys.stdin.readline

n = int(input())
ls = []
time = list(map(int, input().split()))
time.sort()

for i in range(n):
    if i == 0:
        ls.append(time[i])
    else:
        add = ls[i-1] + time[i]
        ls.append(add)
print(sum(ls))
