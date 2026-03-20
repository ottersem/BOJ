from sys import stdin
input = stdin.readline

# next = {0:(5,1,3), 1:(0,2,4), 2:(1,3,5), 3:(2,4,0), 4:(3,5,1), 5:(4,0,2)}

# for _ in range(int(input())):
#     n = int(input())
#     pigs = list(map(int,input().split()))
#     tmp = [0 for _ in range(6)]
#     day = 1

#     while sum(pigs) <= n:
#         day += 1
#         for i in range(6):
#             tmp[i] = next[i][0] + next[i][1] + next[i][2]


#         pigs = tmp

#     print(day)

for _ in range(int(input())):
    n = int(input())
    pigs = sum(list(map(int,input().split())))
    day = 1
    while pigs <= n:
        pigs *= 4
        day += 1
    print(day)
    