# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))

crt = []

def bt(n,m,crt):
    if len(crt) == m:
        print(*crt)
        return
    
    for num in nums:
        crt.append(num)
        bt(n,m,crt)
        crt.pop()

bt(n,m,crt)
