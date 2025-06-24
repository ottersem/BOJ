# Backtracking
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
n,m = map(int,input().split())
nums = sorted(list(map(int, input().split())))

answers = []
crt = []

def bt(n,m,crt):
    if len(crt)==m:
        answers.append(crt[:])
        return
    
    for num in nums:
        crt.append(num)
        bt(n,m,crt)
        crt.pop()

bt(n,m,crt)

for ans in answers:
    print(*ans)