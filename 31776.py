from sys import stdin
input = stdin.readline

n = int(input())

cnt = 0

for _ in range(n):
    t = list(map(int, input().split()))

    if all(x == -1 for x in t):
        continue

    valid = True
    for i in range(3):
        if t[i] == -1:
            continue
        for ii in range(i):
            if t[ii] == -1 or t[ii] > t[i]:
                valid = False
                break
        for ii in range(i+1, 3):
            if t[ii] != -1 and t[ii] < t[i]:
                valid = False
                break
        if not valid:
            break

    if valid:
            cnt += 1

print(cnt)