# Backtracking
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

n, m = map(int, input().split())

results = []
visited = [False] * (n+1)
crt = []

def bt(n,m,crt,visited):
    if len(crt) == m:
        results.append(crt[:])
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            crt.append(i)
            if len(crt) == 1 or crt[-1] > crt[-2]:
                bt(n,m,crt,visited)
            crt.pop()
            visited[i] = False

bt(n,m,crt,visited)

for res in results:
    print(*res)
            