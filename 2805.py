import sys
input = sys.stdin.readline

_, m = map(int, input().split())
trees = list(map(int,input().split()))

starting_point = max(trees)-1
def wood(h,t):
    return sum(t-h if t>h else 0 for t in trees)

l,r= 0,max(trees)
res = 0

while l<=r:
    mid = (l+r) // 2
    w = wood(mid,trees)

    if w>=m:
        res = mid
        l = mid+1
    else:
        r = mid-1

print(res)