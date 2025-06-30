from sys import stdin
input = stdin.readline

n, t = map(int,input().split())

table = [0 for _ in range(1000)]

for _ in range(n):
    k = int(input())
    for _ in range(k):
        a, b = map(int,input().split())
        for i in range(a,b):
            table[i] += 1

answer = 0
max_screen = 0

for i in range(len(table)-t):
    screen = sum(table[i:i+t])
    if screen > max_screen:
        answer = i
        max_screen = screen

print(f'{answer} {answer+t}')