# Backtracking
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

n, m = map(int, input().split())

results = []
crt = []

def bt(n,m,crt):
    if len(crt) == m:
        results.append(crt[:])
        return
    
    for i in range(1, n+1):
        crt.append(i)
        bt(n,m,crt)
        crt.pop()

bt(n,m,crt)

for res in results:
    print(*res)