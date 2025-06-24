# Backtracking
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
## 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다

n, m = map(int, input().split())

results = []
crt = []

def bt(n,m,crt):
    if len(crt) == m:
        results.append(crt[:])
        return
    
    for i in range(1, n+1):
        if not crt or crt[-1] <= i:
            crt.append(i)
            bt(n,m,crt)
            crt.pop()

bt(n,m,crt)

for res in results:
    print(*res)