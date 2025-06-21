# Backtracking
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
n, m = map(int, input().split())

results = []
crt = []

def bt(n,m,crt,visited):
    if len(crt) == m:
        results.append(crt[:])
        return
    
    for i in range(1, n+1):
        if not visited[i]: #선택
            visited[i] = True
            crt.append(i)
            bt(n,m,crt,visited) #탐색
            crt.pop()
            visited[i] = False # 복구

visited = [False] * (n+1)
bt(n,m,crt,visited)

for res in results:
    print(*res)