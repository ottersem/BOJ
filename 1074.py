N,r,c = map(int, input().split())

def solve(n,r,c):
    if n==0:
        return 0

    half = 2 ** (n-1)
    hh = half*half

    if r < half and c < half: #top-left
        return solve(n-1,r,c)
    elif r<half and c >= half: #top-right
        return solve(n-1,r,c-half) + hh
    elif r>=half and c<half: #bottom-left
        return solve(n-1, r-half, c) + 2*hh
    elif r>=half and c>=half: #bottom-right
        return solve(n-1, r-half, c-half) + 3*hh
    
print(solve(N,r,c))