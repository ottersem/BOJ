from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def D(num):
    return (num * 2) % 10000

def S(num):
    return 9999 if num == 0 else num - 1

def L(num):
    return (num % 1000) * 10 + num // 1000

def R(num):
    return (num % 10) * 1000 + num // 10

def bfs(start, target):
    if start == target:
        return ""
    
    q = deque([(start, "")])
    visited = [False] * 10000
    visited[start] = True
    
    operations = {'D': D, 'S': S, 'L': L, 'R': R}

    while q:
        current, path = q.popleft()
        
        for op in ['D', 'S', 'L', 'R']:
            next_num = operations[op](current)
            if not visited[next_num]:
                if next_num == target:
                    return path + op
                visited[next_num] = True
                q.append((next_num, path + op))

for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))