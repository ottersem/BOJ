import sys
input = sys.stdin.readline

n, m = map(int, input().split())

fee = 0

for _ in range(n):
    _ = input()

for _ in range(m):
    fee += int(input().split()[1])

print(fee/n)