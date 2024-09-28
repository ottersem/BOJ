from sys import stdin as sti
a, b = map(int, sti.readline().split())
lines = []
n = False

for _ in range(a):
    lines.append(int(sti.readline()))

right = max(lines)
left = 1
result = 0

while left <= right:
    total = 0
    mid = (right + left)//2
    for line in lines:
        total += line//mid
    if total >= b:
        result = mid
        left = mid +1
    else:
        right = mid -1

    
print(result)






















#매개변수 탐색시의 변수 설정
# bot = 1
# top = max(lines)
# total = 0
# for line in lines:
#     total += line//(int((bot+top)/2))



# while True:
#     mid = int((bot+top)/2)
#     if total > b:
#         total = 0
#         bot = mid +1
#         for line in lines:
#             total += line//mid
#     elif total < b:
#         total = 0
#         top = mid -1
#         for line in lines:
#             total += line//mid
#     if total == b:
#         print(mid)
#         break


# if total > b:
#     while True:
#         mid = int((bot+top/2))
#         bot = mid + 1
#         if bot > top:
#             print(top)
#             break
# elif total < b:
#     while True:
#         mid = int((bot+top)/2)
#         top = mid - 1
#         if mid > top:
#             print(mid)
#             break

