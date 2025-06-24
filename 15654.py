# Backtracking
# N개의 자연수 중에서 M개를 고른 수열

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))

result = []
crt = []

def bt(n,m,crt):
    if len(crt) == m:
        result.append(crt[:])
        return
    
    for num in nums:
        if not num in crt:
            crt.append(num)
            bt(n,m,crt)
            crt.pop()

bt(n,m,crt)

for res in result:
    print(*res)