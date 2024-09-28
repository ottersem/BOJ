from sys import stdin as sti

a, b = map(int, sti.readline().split())

# 소수 판별을 위한 boolean 리스트 생성 (True면 소수)
is_prime = [True] * (b + 1)
is_prime[0], is_prime[1] = False, False  # 0과 1은 소수가 아님

# 에라토스테네스의 체 알고리즘
for num in range(2, int(b**0.5) + 1):
    if is_prime[num]:
        for multiple in range(num * num, b + 1, num):  # num의 배수를 False로 마킹
            is_prime[multiple] = False

# 주어진 범위 [a, b]에서 소수 출력
for num in range(a, b + 1):
    if is_prime[num]:
        print(num)