import sys
input = sys.stdin.readline

n = int(input())
ls = [0,1,1,2]

while n != 1:
    if (n-1) % 3 == 0:
        n = (n-1)//3
        cnt += 2
    if 