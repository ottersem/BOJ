import sys
input = sys.stdin.readline

ls = []
k = int(input())

def ru(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    elif x - int(x) <= -0.5:
        return int(x) - 1
    else:
        return int(x)


for _ in range(k):
    ls.append(int(input()))

ls.sort()

fre = {}
for num in ls:
    if num in fre:
        fre[num] += 1
    else:
        fre[num] = 1
max_freq = max(fre.values())
most_common = [key for key, value in fre.items() if value == max_freq]

Q1 = ru(sum(ls) / k)
Q2 = ls[int(k/2)]
if len(most_common) > 1:
    Q3 = sorted(most_common)[1]
else:
    Q3 = most_common[0]
Q4 = ls[-1] - ls[0]

print(Q1)
print(Q2)
print(Q3)
print(Q4)
