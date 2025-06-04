from collections import deque

a,b = map(int,input().split())

q = deque()
q.append((a, 1))

while q:
    curr, cnt = q.popleft()
    if curr == b:
        print(cnt)
        exit()
    
    case1 = curr*2
    case2 = int(str(curr)+'1')

    if case1 <= b:
        q.append((case1, cnt+1))
    if case2 <= b:
        q.append((case2, cnt+1))


print(-1)