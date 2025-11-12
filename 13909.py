import math
def solution(n):
    v = n
    h = 0
    answer = 0
    for i in range(0, n//2+1):
        answer += math.comb(v,h)
        v -= 1
        h += 1        
    return answer