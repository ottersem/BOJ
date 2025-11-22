import sys
input = sys.stdin.readline

def solution(n):
    triangle = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        if i == 0: continue
        for idx, num in enumerate(triangle[i]):
            if idx == 0:
                triangle[i][0] = triangle[i-1][0] + num
            elif idx == (i):
                triangle[i][idx] = triangle[i-1][idx-1] + num
            else:
                triangle[i][idx] = max(triangle[i-1][idx], triangle[i-1][idx-1]) + num
    
    print(max(triangle[-1]))

solution(int(input()))