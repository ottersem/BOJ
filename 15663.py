# N개의 자연수 중에서 M개를 고른 수열

n, m  = map(int, input().split())
nums = sorted(list(map(int,input().split())))

visited = [False] * n

def bt(depth, path):
    if depth == m:
        print(*path)
        return
    
    prev = -1
    for i in range(n):
        if not visited[i] and prev != nums[i]:
            visited[i] = True
            bt(depth+1, path+[nums[i]])
            visited[i] = False
            prev = nums[i]

bt(0,[])