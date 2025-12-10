import sys
from collections import deque

input = sys.stdin.readline

def solution(n):
    p1, p2 = map(int,input().split())
    m = int(input())
    family = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int,input().split())
        family[a].append(b)
        family[b].append(a)
    
    q = deque()
    q.append((p1,0))
    while q:
        crt, chon = q.popleft()
        visited[crt] = True
        if crt != p2:
            for person in family[crt]:
                if not visited[person]:
                    q.append((person, chon+1))
        else:
            print(chon)
            exit()

    print(-1)
    return 

solution(int(input()))