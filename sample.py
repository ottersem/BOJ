def solution(arr, target):
    hash = [0]*(target+1)

    for num in arr:
        if num <= target:
            hash[num]=1

    print(hash)

    for num in arr:
        if num >= target:
            continue
        if (target-num) == num:
            continue
        if hash[target - num]:
            return True
        
    return False

arr = [1,2,3,4,8]
target = 6

solution(arr=arr, target=target)