n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))

results = []
crt = []

def bt(n,m,crt):
    if len(crt)==m:
        results.append(crt[:])
        return
    
    for num in nums:
        if not num in crt:
            if not crt or crt[-1] <= num:
                crt.append(num)
                bt(n,m,crt)
                crt.pop()

bt(n,m,crt)

for res in results:
    print(*res)