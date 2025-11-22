import sys
input = sys.stdin.readline

def solution(n): # 접근은 맞는데 메모리 초과
    nums = list(map(int, input().split()))
    DP = [nums[:]] + [[-10e40] * n for _ in range(n-1)]

    max_sum = max(nums)

    for i, row in enumerate(DP):
        if i == 0:
            continue
        for j, num in enumerate(row):
            if (j+i) < n:
                DP[i][j] = DP[i-1][j] + nums[i+j]
        
        max_sum = max(max_sum, max(DP[i]))

    print(max_sum)

def solution2(n): #Kadane's Algorithm
    nums = list(map(int, input().split()))
    crt_max = nums[0]
    global_max = nums[0]

    for i in range(1,len(nums)):
        crt_max = max(nums[i], crt_max + nums[i])
        if crt_max > global_max:
            global_max = crt_max

    print(global_max)

solution2(int(input()))