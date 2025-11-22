import sys
input = sys.stdin.readline

def answer(n):
    answer = 0
    hello = set()
    for _ in range(n):
        hi = str(input().strip())
        if hi == 'ENTER':
            answer += len(hello)
            hello = set()
        else:
            hello.add(hi)
    answer += len(hello)
    return answer

print(answer(int(input())))