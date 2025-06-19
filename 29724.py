from sys import stdin
input = stdin.readline

n = int(input())

weight = 0
price = 0

for _ in range(n):
    t,w,h,l = map(str, input().split())
    if t == 'A':
        w,h,l = int(w), int(h), int(l)
        apples = (w//12) * (h//12) * (l//12)
        weight += 1000 + (500 * apples)
        price += apples * 4000
    else:
        weight += 6000

print(weight)
print(price)