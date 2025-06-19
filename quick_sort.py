A = [
    [0, 3, 4, 0, 0, 0, 0, 0, 0],  # 0
    [3, 0, 0, 5, 0, 0, 0, 0, 0],  # 1
    [4, 0, 0, 0, 0, 0, 2, 1, 0],  # 2
    [0, 5, 0, 0, 3, 6, 0, 0, 2],  # 3
    [0, 0, 0, 3, 0, 0, 0, 0, 1],  # 4
    [0, 0, 0, 6, 0, 0, 1, 2, 0],  # 5
    [0, 0, 2, 0, 0, 1, 0, 0, 0],  # 6
    [0, 0, 1, 0, 0, 2, 0, 0, 0],  # 7
    [0, 0, 0, 2, 1, 0, 0, 0, 0],  # 8
]

def dfs(A, start=0):
    n = len(A)
    neighbors = []
    for i in range(n):
        neighbors.append([])
        for j in range(n):
            if A[i][j] != 0:
                neighbors[i].append(j)

        neighbors[i].sort(key= lambda x: A[i][x], reverse = True)

    visited = list()
    stack = [start]
    while stack:
        i = stack.pop()
        if i not in visited:
            visited.append(i)
            stack.extend([x for x in neighbors[i] if x not in visited])

    
    print(visited)

dfs(A)