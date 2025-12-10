import sys
input = sys.stdin.readline
import heapq

left_heap = []
right_heap = []

n = int(input())

for _ in range(n):
    num = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if right_heap and (-left_heap[0] > right_heap[0]):
        max_left = -heapq.heappop(left_heap)
        min_right = heapq.heappop(right_heap)

        heapq.heappush(right_heap, max_left)
        heapq.heappush(left_heap, -min_right)
    
    print(-left_heap[0])