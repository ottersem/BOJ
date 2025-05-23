from collections import deque

dq = deque(n+1 for n in range(int(input())))
print(dq)
answer = []

while not len(dq) == 1:
    answer.append(str(dq.popleft()))
    dq.append(dq.popleft())

answer.append(str(dq.pop()))

print(' '.join(answer))