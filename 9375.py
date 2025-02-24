import sys

input = sys.stdin.readline

for _ in range(int(input())):
    dic = dict()
    for _ in range(int(input())):
        wear = input().split()
        if wear[1] in dic:
            dic[wear[1]].append(wear[0])
        else:
            dic[wear[1]] = [wear[0]]
    
    cnt = 1
    for i in dic:
        cnt *= len(dic[i]) + 1
    print(cnt - 1)
    print(dic)