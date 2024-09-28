from sys import stdin as sti

a = int(sti.readline())
n = 1
for i in range(a):
    if a == 1:
        print(1)
    elif n < a:
        n += 6*(i+1)
    elif n >= a:
        print(i+1)
        break
