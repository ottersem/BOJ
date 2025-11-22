import sys
import heapq
input = sys.stdin.readline


for _ in range(int(input())):
    min_h = []
    max_h = []
    counts = {}
    size = 0

    for _ in range(int(input())):
        line = input().split()
        ops=line[0]
        num = int(line[1])


        if ops == 'I':
            heapq.heappush(min_h, num)
            heapq.heappush(max_h, -num)

            counts[num] = counts.get(num, 0) + 1
            size += 1
        elif ops == 'D':
            if size == 0:
                continue

            if num == 1:
                while max_h:
                    max_val = -heapq.heappop(max_h)
                    if counts.get(max_val, 0) > 0:
                            counts[max_val] -= 1
                            size -= 1
                            break
            elif num == -1:
                 while min_h:
                      min_val = heapq.heappop(min_h)

                      if counts.get(min_val, 0) > 0:
                           counts[min_val] -= 1
                           size -= 1
                           break
                      
        while min_h and counts.get(min_h[0], 0) == 0:
            heapq.heappop(min_h)

        while max_h and counts.get(-max_h[0], 0) == 0:
            heapq.heappop(max_h)

    if size == 0:
        print("EMPTY")
    else:
        max_val = -max_h[0]
        min_val = min_h[0]
        print(f"{max_val} {min_val}")