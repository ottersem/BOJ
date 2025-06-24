# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

n,m = map(int, input().split())
nums = sorted(list(map(int,input().split())))

visited = [False] * n

def bt(depth, start, path):
    if depth == m:
        print(*path)
        return

    prev = -1
    for i in range(start, n):
        if not visited[i] and prev != nums[i]:
            visited[i] = True
            bt(depth + 1, i+1, path + [nums[i]])
            visited[i] = False
            prev = nums[i]
            
bt(0,0,[])