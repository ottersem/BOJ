# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
n,m = map(int,input().split())
nums = sorted(list(set(map(int,input().split()))))

crt = []

def bt(n,m,crt):
    if len(crt) == m:
        print(*crt)
        return
    
    for num in nums:
        if not crt or crt[-1] <= num:
            crt.append(num)
            bt(n,m,crt)
            crt.pop()

bt(n,m,crt)