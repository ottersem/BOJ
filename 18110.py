from sys import stdin as sti
n = int(sti.readline())
ls = []

def ro(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)
    
r = int(ro(n*0.15))

for _ in range(n):
    ls.append(int(sti.readline()))

ls.sort()
if r > 0:
    ls = ls[r:-r]

if ls:
    average = sum(ls) / len(ls)
else:
    average = 0

print(ro(average))