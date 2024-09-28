from sys import stdin as sti

n = int(sti.readline())
m = int(sti.readline())
s = list(sti.readline().strip())
for _ in range(n):
    IO = ['I', 'O'] * n + ['I']

cnt = 0

for i in range(m-2*n):
    if s[i:2*n+1+i] == IO :
        cnt += 1

print(cnt)