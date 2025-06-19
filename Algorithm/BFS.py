## DFS로 모든 그래프의 노드를 순회하는 함수 만들기.
## 입력 ie) graph = [['A','B'],['B','C'],['C','D']...], start = 'A'
## 출력 ['A','B','C'...]
from collections import defaultdict

def DFS(node, adj_list, visited, result):
    visited.add(node)
    result.append(node)
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            DFS(neighbor, adj_list, visited, result)

def solution(graph, start):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    visited = set()
    result = []
    DFS(start, adj_list, visited, result)
    return result

graph = [['A','B'],['B','C'],['C','D'], ['D','E']]
start = 'A'

print(solution(graph, start))