equation = str(input())
nums = equation.split('-')

res = sum(map(int, nums[0].split('+')))

for i in range(1, len(nums)):
    res -= sum(map(int,nums[i].split('+')))

print(res)