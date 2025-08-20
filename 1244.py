# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 수위치의 상태를 바꾼다.
# 여학생을 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다. 구간에 속한 스위치 개수는 항상 홀수다.
from sys import stdin
input = stdin.readline

switch = int(input())
status = list(map(int,input().split()))

def action(num):
    return 1-num

def male(integer, status):
    for i in range(integer, len(status)+1, integer):
        status[i-1] = action(status[i-1])

    return status

def female(integer, status):
    center = integer -1
    left = right = center

    while left > 0 and right < len(status)-1:
        if status[left-1] == status[right + 1]:
            left -= 1
            right += 1
        else:
            break

    for i in range(left, right+1):
        status[i] = action(status[i])
    
    return status

for _ in range(int(input())):
    g, i = map(int, input().split()) # g: 1=m, 2=f
    if g == 1:
        status = male(i,status)
    else: # g==2
        status = female(i,status)

for i in range(0,switch, 20):
    print(*status[i:i+20])
