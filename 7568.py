from sys import stdin
input = stdin.readline

n = int(input())
ls = []
rating = []

for _ in range(n):
    w, h = map(int, input().split())
    ls.append([w, h])

for i in range(n):
    count = 1
    for j in range(n):
        if ls[i][0] < ls[j][0] and ls[i][1] < ls[j][1]:
            count += 1
    rating.append(str(count))

print(" ".join(rating))

    


