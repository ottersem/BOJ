from sys import stdin as sti

n = int(sti.readline())
counting = [0]*10000
for _ in range(n):
    x = int(sti.readline())
    counting[x-1] += 1

for i in range(10000):
    if counting[i] != 0:
        for _ in range(counting[i]):
            print(i+1)