import sys
input = sys.stdin.readline

_ = input()
a = int(input())
b = int(input())

res = 0
while b > 0:
    if b&1:
        res += a
    
    a <<= 1
    b >>= 1
print(res)