import heapq

def dijkstra(start, n, graph):

    # 1. 거리 테이블 무한대로 초기화
    INF = int(1e9)
    distance = [INF] * (n+1)

    # 2. 우선순위 큐 생성 및 시작 노드 넣기
    # 큐에는 (비용, 노드 번호) 순서로 넣어야 비용 기준으로 정렬
    q = []
    heapq.heappush(q, (0,start)) # 거리 = 0, 시작점 = start
    distance[start] = 0

    while q:
        # 3. 가장 최단 거리인 노드 꺼내기
        dist, now = heapq.heappop(q)

        # 4. 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist : continue

        # 5. 인접 노드 확인
        for i in graph[now]:
            next_node = i[0]
            cost = dist + i[1] # 현재까지 거리 + 다음 노드로 가는 비용

            # 6. 더 짧은 경로 발견시 갱신
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance