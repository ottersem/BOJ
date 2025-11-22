import sys
input = sys.stdin.readline

n,m = map(int,input().split())

s = set()
answer = 0
for _ in range(n):
    s.add(str(input().strip()))

for _ in range(m):
    crt = str(input().strip())
    if crt in s:
        answer += 1

print(answer)
